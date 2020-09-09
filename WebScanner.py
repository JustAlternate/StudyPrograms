#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()

#Libraires

import os
import socket
import threading

 #Scan : the user agent (web browser) and the user ip address

val=os.environ

#Printing

print("Web brower : "+val['HTTP_USER_AGENT'])
print("Web brower : "+val['REMOTE_ADDR'])
