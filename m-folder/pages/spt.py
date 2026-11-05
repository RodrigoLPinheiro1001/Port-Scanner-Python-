# Python program to test
# internet speed

import speedtest  
from rich.console import Console, Group

console = Console()

def speed_test_page():

    
    console.clear()
    print("Welcome to the Internet Speed Test Page !\n")
    print("This page will help you to test your internet speed.\n")
    print("Please wait while we are testing your internet speed...\n")
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