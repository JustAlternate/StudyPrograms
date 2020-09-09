#!/usr/bin/python

import socket
import cgitb
import cgi
cgitb.enable()

demande=None

def URL2IP(val):

	return(socket.gethostbyname(demande))
   
donnees=cgi.FieldStorage()
demande=donnees.getvalue("demande")


print("""
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>ULR2IP</title>
    <link rel="stylesheet" type="text/css" href="http://144.91.84.212/Convertisseur.css">
</head>
<body>
<header>Convertisseur IP FINDER</header>
<p>Url vers IP</p>
<form method="GET" action="Url2IP.py">
    <label for="demande"></label>
    <input class="buttons3" type="text" name="demande" id="demande" required>

<input class="buttons2"   type='submit' value='Jouer'>\n</form>
""")
if demande!=None:
	print("""<p>L'ip : {} ! <p>""").format(URL2IP(demande))
print("""
</body>
</html>
""")
