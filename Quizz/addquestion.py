#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
donnees=cgi.FieldStorage()

question=str(donnees.getvalue("question"))

rep1=str(donnees.getvalue("rep1"))
rep2=str(donnees.getvalue("rep2"))
rep3=str(donnees.getvalue("rep3"))
rep4=str(donnees.getvalue("rep4"))

addquestion=open("/var/www/html/quizz/questionprovisoire.txt","a")
addanswer=open("/var/www/html/quizz/reponseprovisoire.txt","a")

addquestion.write(question+"\n")
addquestion.close()
addanswer.write(rep1+"\n")
addanswer.write(rep2+"\n")
addanswer.write(rep3+"\n")
addanswer.write(rep4+"\n")
addanswer.close()
print("""
    	<html>
    	<head>
		<title>Quizz register success</title>
        <meta http-equiv="refresh" content="2; URL=http://justalternate.pw/quizz/"/>
		</head>
		<body>
		<p> Success, your question has been registered. You will be redirected in 1 second </p>
		</body>
""")
