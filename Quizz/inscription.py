#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
donnees=cgi.FieldStorage()
pseudo=str(donnees.getvalue("pseudo"))
mdp=str(donnees.getvalue("mdp"))

user=open("/var/www/html/quizz/pseudo.txt","a")
password=open("/var/www/html/quizz/password.txt","a")


trouve=False


def usernameAlreadyUsed():
	Luser=[]
	pseudo=str(donnees.getvalue("pseudo"))
	user=open("/var/www/html/quizz/pseudo.txt","r") #oblige de le reouvrir en "read" sinon impossible de faire un realines
	Luser=user.readlines()
	user.close()
	for i in range(len(Luser)):
		if pseudo == Luser[i].rstrip('\n'):
			return False
	return True

def PasDeSpace():
	if (" ") in pseudo:
		return False
	else:
		return True


if len(mdp) > 7 and usernameAlreadyUsed()==True and len(pseudo) >= 1 and PasDeSpace()==True and len(mdp)<100 and len(pseudo)<100:
	user.write(pseudo+"\n")
	password.write(mdp+"\n")
	user.close()
	password.close()
	trouve=True

if trouve == True:
	print("""
    	<html>
    	<head>
		<title>Quizz register success</title>
        <meta http-equiv="refresh" content="2; URL=http://justalternate.pw/quizz/"/>
		</head>
		<body>
		<p> Success, your username {} has been registered. You will be redirected in 2 second </p>
		</body>
		""").format(pseudo)


else:
	print("""
	<html>
		<head>
			<script>
				function redirect(){
					alert("Mot de passe invalide, Username invalide ou deja pris");
					window.location.href = "http://justalternate.pw/quizz/QuizzRegister.html";
				}
			</script>
			<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
			<title>Quizz login failed</title>
				<p> Failed </p>
		</head>
		<body onload="redirect()">
		</body>
	""")
