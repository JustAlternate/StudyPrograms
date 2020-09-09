#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()

#Libraires

import os
import socket
import threading

 #Scan : the user agent (web browser) ; the user ip address ; the server ip address ; and the server name.

val=os.environ
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

#Printing

print("""
	<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
		<link rel="stylesheet" type="text/css" href="http://144.91.84.212/style2.css"/>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	</head>
	<body>
		<p style="font-size:20px;">navigateur : {} !</p>""").format(val['HTTP_USER_AGENT'])
print("""
	<p style="font-size:20px;">User IP : {} !</p>""").format(val['REMOTE_ADDR'])
print("""
	<p style="font-size:20px;">Server : {} !</p>""").format(host_name)
print("""
	<p style="font-size:20px;">Server ip : {} !</p>""").format(host_ip)
print("""
	</body>
	</html>
""")
