import pyfiglet
from rich.console import Console
from pages.about_me import about_page
from pages.scanner import scanner_page
from pages.spt import speed_test_page

console = Console()


def home_page():
    # Limpar Consola
    console.clear()

    console.print(
        pyfiglet.figlet_format("TC Vision", font="slant"),
        style="bold cyan"
    )
    
    console.print("© 2026 Rodrigo  - Todos os direitos reservados\n", style="bold green")
    console.print("Versão: 0.1.0\n", style="bold yellow")
    console.print("Scanner de portas TCP simples\n", style="bold blue")
    console.print(
        "Nota: Este scanner só funciona para localhost "
        "(Qualquer outro host será recusado)\n",
        style="bold red"
    )
    
    console.print(
        "Comandos permitidos:\n",
        "1 - IP (Ex: 127.0.0.1)\n",
        "2 - \"ab\" (abre página Sobre mim)\n",
        "3 - \"speed\" (abre página de teste de velocidade)\n",
        style="bold blue"
    )


    while True:

        target = console.input(
            "[bold blue]Introduza o hostname, IP do alvo ou destino de página"
            "(ex: localhost): [/bold blue]"
        ).strip()


        # Verificação About us
        if target == "ab":
            console.print("[bold cyan]A abrir About Me...[/bold cyan]")
            about_page()
            return

        elif target in ["speed", "Speed"]:
            console.print(
                f"\n[bold green]A abrir a página de teste de velocidade ...[/bold green]"
            )

            speed_test_page()
            return
        
        # Validar target (Será localhost ou um host válido?)
        elif target in ["localhost", "127.0.0.1"]:
            console.print(
                f"\n[bold green]Target selecionado: {target}[/bold green]"
            )

            scanner_page(target)
            return

        # Target Inválido 
        else:
            console.print(
                "[bold red]Erro: Comando inválido ou host não suportado. "
                "Tente novamente.[/bold red]\n"
            )
