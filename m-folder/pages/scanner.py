import pyfiglet
import socket
from datetime import datetime

from rich.console import Console, Group
from rich.table import Table
from rich.live import Live
from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    TaskProgressColumn,
    TimeRemainingColumn
)

console = Console()


def scanner_page(target):

    # Validar destino
    if target not in ["localhost", "127.0.0.1"]:
        console.print(
            "[bold red]Erro: Apenas localhost é permitido![/bold red]"
        )
        return

    console.clear()

    console.print(
        pyfiglet.figlet_format("Scanner TCP", font="slant"),
        style="bold cyan"
    )
    console.print("© 2026 Rodrigo  - Todos os direitos reservados\n", style="bold green")
    console.print(f"[bold blue]Target:[/bold blue] {target}")
    console.print(f"[bold blue]Esta ação pode demorar alguns minutos, por favor aguarde . . .[/bold blue]\n")
    console.print(
        f"[dim]Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}[/dim]\n"
    )

    # Configuração do scan
    start_port = 1

    # Porta a 1024 para testes
    end_port = 1024
    timeout = 0.1

    open_ports = []
    last_ports = []

    # Criar tabela dinâmica
    def create_table():

        table = Table(title="Últimas 5 portas analisadas")

        table.add_column("Porta", style="cyan", justify="center")
        table.add_column("Estado", justify="center")
        table.add_column("Serviço", style="yellow")

        for port, status, service in last_ports:

            if status == "OPEN":
                color = "green"
            elif status == "CLOSED":
                color = "red"
            else:
                color = "yellow"

            table.add_row(
                str(port),
                f"[{color}]{status}[/{color}]",
                service
            )

        return table

    # Criar barra de progresso
    progress = Progress(
        TextColumn("[cyan]A analisar portas TCP..."),
        BarColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        console=console,
        auto_refresh=False
    )

    task = progress.add_task(
        "Scan",
        total=end_port - start_port + 1
    )

    # Iniciar interface dinâmica
    with Live(
        Group(create_table(), progress),
        console=console,
        refresh_per_second=8
    ) as live:

        for port in range(start_port, end_port + 1):

            try:
                with socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                ) as sock:

                    sock.settimeout(timeout)

                    result = sock.connect_ex((target, port))

                    if result == 0:

                        status = "OPEN"
                        open_ports.append(port)

                        try:
                            service = socket.getservbyport(
                                port,
                                "tcp"
                            )
                        except OSError:
                            service = "Desconhecido"

                    else:
                        status = "CLOSED"
                        service = "-"

            except socket.error:

                status = "ERROR"
                service = "-"

            # Guardar resultado
            last_ports.append((port, status, service))

            # Manter apenas as últimas 5 portas
            if len(last_ports) > 5:
                last_ports.pop(0)

            # Atualizar progresso
            progress.update(task, advance=1)

            # Atualizar tabela e barra de progresso
            live.update(
                Group(create_table(), progress),
                refresh=True
            )

    # Resultados finais
    console.print("\n[bold green]Scan concluído![/bold green]\n")

    results = Table(title="Portas TCP abertas")

    results.add_column("Porta", style="cyan", justify="center")
    results.add_column("Estado", style="green", justify="center")
    results.add_column("Serviço", style="yellow")

    for port in open_ports:

        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "Desconhecido"

        results.add_row(
            str(port),
            "OPEN",
            service
        )

    if open_ports:
        console.print(results)
    else:
        console.print("[yellow]Nenhuma porta aberta encontrada.[/yellow]")

    console.print(
        f"\n[bold blue]Portas analisadas:[/bold blue] "
        f"{end_port - start_port + 1}"
    )

    console.print(
        f"[bold green]Portas abertas:[/bold green] "
        f"{len(open_ports)}"
    )

    console.input("\n[dim]Pressione ENTER para continuar...[/dim]")
