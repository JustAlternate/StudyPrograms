#!/usr/bin/python

#On importe tout ce dont on a besoin
from random import randint
import random
import cgitb
import cgi
cgitb.enable()

#On ouvre le fichier et stock les questions/reponses dans une liste
Question=open("/var/www/html/quizz/questions.txt","r")
Reponse=open("/var/www/html/quizz/reponses.txt","r")
Lquestions=Question.readlines()
Lreps=Reponse.readlines()
Question.close()
Reponse.close()

#On obtient les logins et mdp precedemment entres
donnees=cgi.FieldStorage()
pseudo=str(donnees.getvalue("pseudo"))
mdp=str(donnees.getvalue("mdp"))

#On verifie le mdp
def authME(pseudo,mdp):
	user=open("/var/www/html/quizz/pseudo.txt","r")
	password=open("/var/www/html/quizz/password.txt","r")
	Luser=user.readlines()
	Lmdp=password.readlines()
	user.close()
	password.close()
	n=0
	trouve=False
	while not(trouve) and n<len(Luser):
		if pseudo == (Luser[n]).rstrip('\n'):
			if mdp == (Lmdp[n]).rstrip('\n'):
				trouve=True
		n+=1
	return trouve

#On enleve les retours a la ligne dans les listes
for i in range(len(Lreps)):
    Lreps[i]=Lreps[i].rstrip('\n')

for k in range(len(Lquestions)):
    Lquestions[k]=Lquestions[k].rstrip('\n')

#On creer nos listes
QuestionsRandoms=[]
ReponsesRandoms=[]
ReponsesGagnantes=[]
ReponsesFinales=[]
r=0

#On a fait ce systeme pour que la meilleure question apparaisse toujours en premier et que les autres soient aleatoires
for l in range(len(Lquestions)): #on fait une boucle pour mettre toutes les reponses et questions dans des listes
    ReponsesAssociees=[]
    while Lquestions[r] in QuestionsRandoms: #on choisit un indice random et une question qui n'est pas dedans sauf la premiere par consequent
	    r=(randint(0,(len(Lquestions))-1))
    QuestionsRandoms.append(Lquestions[r]) #on ajoute les questions
    for m in range(4):	#boucle pour les reponses associees
	    ReponsesAssociees.append(Lreps[r*4+m])
    random.shuffle(ReponsesAssociees) #on melange les reponses
    ReponsesGagnantes.append(Lreps[r*4]) #on definit la reponse gagnante etant donne notre organisation dans le fichier texte
    ReponsesFinales=ReponsesFinales+ReponsesAssociees #on ajoute les reponses



if authME(pseudo,mdp): # si l'autenthification est reussi on execute le quizz
    print("""
<html style="background-image:url('http://justalternate.pw/quizz/wallpaper.png');"> <!-- Code HTML -->
	    <head>
	      <meta http-equiv="Content-Type" content="text/html;" charset="ANSI" />
	      <link rel="stylesheet" type="text/css" href="http://justalternate.pw/quizz/css.css"/> <!-- CSS -->
	      	<script type="text/javascript" src="http://justalternate.pw/quizz/quizzGame.js"></script> <!-- Javascript -->
	      	<script charset="ANSI"> <!-- Nouveau script js pour inserer les valeurs precedemment creer en python (on utilisera le .format) -->
	      		Reponses={}
	      		Questions={}
	      		Reponsegagnante={}
	      	</script>
	      <title>QuizzTime!</title>
	    </head>

	     <header id="titre" class="titre"> Bienvenue </header>

      <body>
        <button class="scale-effect startingButton" id="startingButton" onclick="quizz()"> Start Quizz ! </button> <!-- On lance le quizz -->
	      <p id="Question" class="question"> </p>

	    <score>
	      <h1 class="inline" id="h1game">Ton Score :</h1>
	      <h2 class="inline" id="score-number">0</h2>
	    </score>

		<personal_Best_Score>
			<h3 class="inline"> Ton Best Score : </h3>
			<h4 class="inline" id=LastJoueur> </h4>
		</personal_Best_Score>

			<TimeLeft id="compteur" class="compteur_class">
	            <p class="temps">Temps Restant</p>
	            <input id="minutes" type="text" class="minutes_class">
	            <font id="commalike" color="#ffaf40" size="5"> : </font>
	            <input id="seconds" type="text" class="seconds_class">
	       </TimeLeft>

		   <Reset>

		  		<button class="buttons reset scale-effect" onclick="ResetTopScore()">RESET</button>

		   </Reset>
		   
		   	<moitmoit>

		  		<button id="moitmoit" class="buttons moitmoit scale-effect" onclick="cinquante_cinquante()">50/50</button>

		   </moitmoit>

   	  <form method="POST" action="/cgi-enabled/quizzGame.py">

        <Ligne1 style="display:inline;">
	              <input onclick="questionRandom(1)" id="Rep1" name="rep1" class="scale-effect rep1" type="button" value=" "> <!-- Chaque bouton a son parametre pour la fonction questionRandom() permettant de verifier les reponses -->
	              <input onclick="questionRandom(2)" id="Rep2" name="rep2" class="scale-effect rep2" type="button" value=" ">
	    </Ligne1>

        <Ligne2 style="display:inline;">
	              <input onclick="questionRandom(3)" id="Rep3" name="rep3" class="scale-effect rep3" type="button" value=" ">
	              <input onclick="questionRandom(4)" id="Rep4" name="rep4" class="scale-effect rep4" type="button" value=" ">
	    </Ligne2>
        
        

		<p id="Reponse" class="reponse"> test</p> <!-- Reponse attendu si erreur -->
		<p id="User" class="user"> Connecte(e) en tant que {} </p>
        <div style="display:none;">

        <input type="texte" name="pseudo" value="{}">
	    <input type="password" name="mdp" value="{}">

        <p style= margin-top:5vh;> </p>
	    <input class="scale-effect entrer" type="submit" value="Entrer dans la partie">
	    </div>
	  </form>

	        <img id="fail" class="fail" src="http://justalternate.pw/quizz/section-fail.png">
	        <img id="pass" class="pass" src="http://justalternate.pw/quizz/section-pass.png">

	 </body>
</html>
""".format(ReponsesFinales,QuestionsRandoms,ReponsesGagnantes,pseudo,pseudo,mdp)) #on insere les variables python

else: #si l'authentification n'est pas verifiee on redirige
    print("""
	    	<html>
	    		<head>
					<title>Quizz register success</title>
	        			<meta http-equiv="refresh" content="2; URL=http://justalternate.pw/quizz/QuizzLogin.html"/>
				</head>
				<body>
					<p> Your username or your password is not accepted (did you already registered ?). You will be redirected in 2 second </p>
				</body>
			</html>
	""")
