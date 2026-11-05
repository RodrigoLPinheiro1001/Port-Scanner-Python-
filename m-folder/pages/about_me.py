import pyfiglet
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

def about_page() :
    console.clear()
    console.print(
        pyfiglet.figlet_format("about me", font="slant"), 
        style="bold cyan"
        )
    console.print("Este é um scanner de portas TCP simples, desenvolvido por [bold green]Rodrigo Lopes[/bold green].\n", style="bold blue")
   