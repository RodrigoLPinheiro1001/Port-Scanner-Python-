import speedtest  
from rich.console import Console, Group
import pyfiglet
console = Console()

def speed_test_page():

    
    console.clear()
    console.print(
        pyfiglet.figlet_format("Speed Test", font="slant"),
        style="bold cyan"
    )
    console.print("© 2026 Rodrigo  - Todos os direitos reservados\n", style="bold green")


    st = speedtest.Speedtest()

    option = int(input('''What speed do you want to test:  

    1) Download Speed  

    2) Upload Speed  

    3) Ping 

    Your Choice: '''))


    if option == 1:
        print(f"{st.download() / 1000000:.2f} Mbps")

    elif option == 2: 

        print(st.upload())  

    elif option == 3:  

        servernames =[]  

        st.get_servers(servernames)  

        print(st.results.ping)  

    else:

        print("Please enter the correct choice !")