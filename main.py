import socket
import color
import sys
from queue import Queue
import threading
from datetime import datetime
import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
clear()

print("\n")

os.system('figlet -f small "  PORT SCAN"|lolcat\n')

print(color.BOLD+color.LIGHT_CYAN+color.BOLD+"\n  ___________________________________________\n")

host = socket.gethostbyname(input(color.BOLD+color.YELLOW+color.BOLD+"\n  [+] Enter Your IP/Domain :  "+color.LIGHT_CYAN))

normalPortStart = 1
normalPortEnd = 1024
allPort = 1
allPortEnd = 65535
customPortStart = 0
customPortEnd = 0

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(color.BOLD+color.RED+color.BOLD+"\n  [+] Select Your Scan Type : \n")
print(color.BOLD+color.YELLOW+color.BOLD+"  [+] Select 1 for 1 to 1024 port scaning\n")
print(color.BOLD+color.LIGHT_WHITE+color.BOLD+"  [+] Select 2 for 1 to 65535 port scaning\n")
print(color.BOLD+color.GREEN+color.BOLD+"  [+] Select 3 for custom port scaning\n")
print(color.BOLD+color.LIGHT_WHITE+color.BOLD+"  [+] Select 4 for exit \n")

print(color.BOLD+color.LIGHT_CYAN+color.BOLD+"  ___________________________________________\n")

mode = int(input(color.BOLD+color.GREEN+color.BOLD+"  [+] Select Any Option: "+color.LIGHT_CYAN))
print()

if mode == 3:
    customPortStart = int(input(color.BOLD+color.GREEN+color.BOLD+"  [+] Enter starting port number: \n"+color.LIGHT_CYAN))
    customPortEnd = int(input(color.BOLD+color.YELLOW+color.BOLD+"  [+] Enter ending port number: \n"+color.LIGHT_CYAN))

#print("-"*50)
print(color.BOLD+color.YELLOW+"\n  Target IP : "+color.BOLD+color.LIGHT_CYAN+host)
print(color.BOLD+color.RED+color.BOLD+"\n  Scanning Started At : " + color.BOLD+color.GREEN+str(datetime.now()))
#print("-"*50)
def scan(port):
    s = socket.socket()
    s.settimeout(5)
    result = s.connect_ex((host, port))
    if result == 0:
       print(color.BOLD+color.YELLOW+"\n  (+) Port Open : "+color.BOLD+color.LIGHT_CYAN+str(port))
    s.close()

queue = Queue()
def get_ports(mode):
    if mode == 1:
        print("\n  [+] Scaning"+color.BOLD+color.YELLOW+"."+color.BOLD+color.RED+"."+color.BOLD+color.GREEN+"."+"\n")
        for port in range(normalPortStart, normalPortEnd+1):
            queue.put(port)
    elif mode == 2:
        print("\n  [+] Scaning"+color.BOLD+color.YELLOW+"."+color.BOLD+color.RED+"."+color.BOLD+color.GREEN+"."+"\n")
        for port in range(allPort, allPortEnd+1):
            queue.put(port)
    elif mode == 3:
        print("\n  [+] Scaning"+color.BOLD+color.YELLOW+"."+color.BOLD+color.RED+"."+color.BOLD+color.GREEN+"."+"\n")
        for port in range(customPortStart, customPortEnd+1):
            queue.put(port)
    elif mode == 4:
        print(color.BOLD+color.RED+"  [-] Exiting... \n")
        sys.exit()

open_ports = [] 
def worker():
    while not queue.empty():
        port = queue.get()
        if scan(port):
            print(color.BOLD+color.LIGHT_CYAN+"\n  [+] Port {} is open \n".format(port))
            open_ports.append(port)

def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

run_scanner(1021, mode)
print(color.BOLD+color.GREEN+"\n  [+] Scanning Compleate In : "+color.BOLD+color.YELLOW+current_time)
print("\n")
