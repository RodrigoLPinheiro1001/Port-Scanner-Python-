
import pyfiglet
import sys
import socket
import time
import ipaddress
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.progress import track
from pages.home import home_page

console = Console()

# Chama a home page quando o script é executado diretamente
if __name__ == "__main__":
    home_page()
    
