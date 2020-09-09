#!/usr/bin/env python

import cgitb
import cgi
cgitb.enable()

#Libraries :

import os
import socket
import threading

#Load all ip discovered :

Iptxt=open("/var/www/html/ip.txt","r")
Iptxt.readline()

AllIp=[]

for ligne in Iptxt:
    val=ligne.rstrip("\n")
    AllIp.append(val)
Iptxt.close()

#Check if the user IP is new

def isThisANewIP(IP):
	return (IP in AllIp)
	
	
#Write down new IP into IPtxt :

def writeIP(IP):
	Iptxt=open("/var/www/html/ip.txt","a")
	Iptxt.write(IP+"\n")
	Iptxt.close()
	

#Ip logger :

IP=os.environ['REMOTE_ADDR'] #if this dont work replace this line by : IP=os.environ['HTTP_X_REAL_IP']

if isThisANewIP(IP):
	a=0
else:
	writeIP(IP)

print("""
Merci pour votre visite ;) {}""").format(IP)
print("""
""")
