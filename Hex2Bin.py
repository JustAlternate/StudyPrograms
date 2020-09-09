#!/usr/bin/python

import cgitb
import cgi
cgitb.enable()
demande=None

#Python part :---------------------------------------------------------------------------------------------------------------------------------------------------------------

dico={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
def HexVersBinDico(val):
    L=""
    for i in range (0,(len(val))):
        for c in dico:
            if val[i]==c:
                L=L+(dico.get(c))
    return L

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

donnees=cgi.FieldStorage()
demande=donnees.getvalue("demande")

print("""
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>Hex2Bin</title>
    <link rel="stylesheet" type="text/css" href="http://144.91.84.212/Convertisseur.css">
</head>
<body>
<header>Convertisseur HextoBin</header>
<p>Hexadecimal vers Binaire</p>
<form method="GET" action="HextoBin.py">
    <label for="demande"></label>
    <input class="buttons3" type="text" name="demande" id="demande" required>
<input class="buttons2"   type='submit' value='Jouer'>\n</form>""")
if demande!=None:
	print("""<p>Resultat : {} ! <p>""").format(HexVersBinDico(demande))
print("""
</body>
</html>""")
