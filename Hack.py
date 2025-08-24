import re
import subprocess
import os
import sherlock
import time

wsl = subprocess.Popen("wsl -d kali-linux", stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
social_sites = [
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://x.com/",
    "https://www.linkedin.com/in",   
    "https://www.tiktok.com/@",      
    "https://www.snapchat.com/add",  
    "https://www.reddit.com/user",
    "https://www.pinterest.com",
    "https://www.youtube.com/@",     
    "https://discord.com/users",     
    "https://www.tumblr.com",        
    "https://www.quora.com/profile", 
    "https://t.me",                  
    "https://wa.me",                 
    "https://mastodon.social/@"
    ]
results = []
choice = ""
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
globals(choice)
globals(results)
def rstage1():
    print("Stage 1: OSINT")
    time.sleep(1)
    print("Enter any amount of usernames that the target normally likes to use in their social media accounts")
    while name != "Done":
        name = input("Username")
        names.append(name)
    choice = input("Would you like to scan the usernames for common social media websites only(y/n): ")
    return choice
    return names
def rstage2():
    print("Stage 2: Network Scanning")
    network = input("Target's Network's IP: ")
    return network
def rstage3(network, choice):
    
    print("Stage 3: Execute")
    time.sleep(1)
    print("This stage takes lots of time to finish")
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
    if choice.lower() == "y":
        for name in names:
            for website in social_media
    elif choice.lower() == "n":
        for name in names:
            command = "sherlock --timeout 4 " + name
            wsl.stdin.write(command)
            wsl.stdin.flush()
            result = wsl.communicate()
            results.append(result)
        
def recon():
    print("Entering Recon Mode")
    time.sleep(1)
    rstage1()
    rstage2()
    rstage3(network, choice)
print("Starting ")
time.sleep(1)
print("What would you like to do:")
print("[1] Recon")
print("[2] Attack")
print("[3] Crack")
choice = input("Choose any option(1,2,3): ")
if choice == "1" or choice.lower() == "recon":
    recon()
