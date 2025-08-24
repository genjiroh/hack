import re
import subprocess
import os
import sherlock
import time

wsl = subprocess.Popen("wsl -d kali-linux", stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
 
 
ip_scan = []
network = ""
social = ""
name = ""
networkscan = ""
names = []
globals(social)
globals(name)
globals(network)
globals(networkscan)
globals(names)
globals(ip_scan)

def rstage1():
    print("Stage 1: OSINT")
    time.sleep(1)
    print("Enter any amount of usernames that the target normally likes to use in their social media accounts")
    while name != "Done":
        name = input("Username")
        names.append(name)
    return names
def rstage2():
    print("Stage 2: Network Scanning")
    network = input("Target's Network's IP: ")
    return network
def rstage3(network):
    
    print("Stage 3: Device Scanning")
    command = "nmap -sn" + network
    networkscan = wsl.stdin.write(command)
    wsl.stdin.flush()
    output = wsl.communicate()
    output = re.findall(r'\d+\.\d+\.\d+\.\d+', output)
    for ip_address in output:
        command = "nmap -A " + ip_address
        wsl.stdin.write(command)
        wsl.stdin.flush()
        result = wsl.communicate()
        ip_scan.append(result)
   

def recon():
    print("Entering Recon Mode")
    time.sleep(1)
    rstage1()
    rstage2()
    rstage3()


    command = "nmap -sn " + network
    networkscan = os.system(command)
    social = sherlock(name)




print("Starting ")
time.sleep(1)
print("What would you like to do:")
print("[1] Recon")
print("[2] Exploit")
print("[3] Crack")
choice = input("Choose any option(1,2,3): ")
if choice == "1" or choice.lower() == "recon":
    recon()