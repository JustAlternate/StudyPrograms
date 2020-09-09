#!/usr/bin/python


#A realy heavy code, one of my 1st school project in python 



"""
Au dessus je donne a mon serveur python httpd.server le path de lenvironement python pour qu'il puissent executer mon script en .py
Jai au prealable donner tout les droits pour que tout fonctionne jai fait un screen pour qu'il tourne meme lorsque putty (mon ssh) est fermer
"""

#Dans ce programme tout les accents et les carractere speciaux ont ete retire puisque quelque pars on a un changement d'encodage (cote serveur) apres avoir tout essayer je n'ai
#pas reussi a resoudre le probleme nous somme donc prive des accents.
diff="" #Pour pouvoir faire des test sur quelle difficulte on choisit on initialise la valeur diff="" (voir l 166-175)
from sys import path, exc_info, settrace
import threading
import cgitb
import cgi     #Bibliotheque pour voir les erreurs et  nous permettre de recuperer les donnees des formulaire
cgitb.enable()
from random import randint #Evidement la fonction randint nous permettra de simuler des valeurs aleatoire.
# Un damier est une liste de "X", "O" ou "" qui correspondent au contenu des
# cases. Les cases sont numerotees par ligne 0 1 2 puis 3 4 5 puis 6 7 8.
def construireDamier(L) :
    dam="<table border=0>\n<tr>\n"
    for k in range(9) :
        if L[k]=="" :
            dam+="<td><input class='btn' type='radio' name='coup' value="+str(k)+"></td>\n"
        else :
            dam+="<td>"+L[k]+"</td>\n"
        if k==2 or k==5 :
            dam+="</tr>\n<tr>\n"
    dam+="</tr>\n</table>"
    return dam
# Le fichier damier.txt permet d'avoir une memoire des coups joues (rappel, a chaque appui sur les boutons du formulaire et donc appel de damier.py, la fonction est relancee)
def sauverGrille(L) :
    monF=open("/tmp/damier.txt","w") #Afin de charger la grille on utilise une base de donnee grace a un .txt stocke sur le serveur dans le fichier /tmp/ car celui ci possede
    for k in range(len(L)) :		#les droits pour etre lu et modifier meme par un utilisateur non root (interne au serveur)
        monF.write(L[k]+"\n")
    monF.close()
def chargerGrille() :
    damiertxt=["","","","","","","","",""]
    f=open("/tmp/damier.txt","r")
    for i in range(9):
        lignes=f.readline()
        if lignes==("\n")or(""):
            damiertxt[i]=("")
        elif lignes==("X\n"):	
            damiertxt[i]=("X")	#Pour charger la grille on lit tout simplement notre fichier damier.txt puis pour chaque lignes (maximum 9 car 9 cases) on regarde quelle
        elif lignes==("O\n"):	#carractere ce trouve sur la ligne avec (f.readline() a chaque lecture, readline() avancera de 1, un peut comme "for i in range")
            damiertxt[i]=("O")  #Les carractere possible sont : "\n" (un retour a la ligne), "" (rien),"X\n" (lettre X puis un retour a la ligne) et "O\n" (lettre O puis un retour a la ligne)
	f.close						#On reecrit ce damier dans la valeur damiertxt puis on la "return" La fonction analyse donc lignes par lignes le damier.txt
    return damiertxt
def casesPossibles(L) :
    CP=[]
    for i in range(len(L)):	#Ici on analyses les cases possibles a jouer (cote ordinateur) on initialise une liste puis pour chaque entree du damier on regarde si il y a un espace vide
        if L[i]=="":		#Si c'est le cas alors on indique a la liste (grace a append) que en cette indice (i) on peut jouer un "O"
		CP.append(i)
    return CP
def jouerCoup1(L) :							#"jouerCoup1" est la version "facile" de notre ordinateur
    r=randint(0,len(casesPossibles(L))-1)	#La fonction "jouerCoup1" est assez simple on genere une valeur aleatoire entre 0 et le nombres de cases possible a jouer puis
    coup=casesPossibles(L)[r]				#On lit la valeur de l'indice aleatoire genere et on regarde la valeur correspondant dans la liste L (du damier)
    return coup
def completerAlignement(L,indices,car) :
	if L[indices[0]]=="" and L[indices[1]]==car and L[indices[2]]==car:
		return 0
	elif L[indices[0]]==car and L[indices[1]]=="" and L[indices[2]]==car:	#Afin de trouver des alignements on va regarder si 3 carractere peuvent s'aligner horizontalement, verticalement
		return 1															#ou dans les diagonales
	elif L[indices[0]]==car and L[indices[1]]==car and L[indices[2]]=="":	#en fonction de l'alignement trouver on "return" 0 ,1 ou 2 et si aucun alignement n'est trouver on "return" -1
		return 2
	else:
		return -1
def jouerCoup2(L):
        coupgagnant=False
        IngagnableOuPresque=False
        compteur=0
        coup=jouerCoup1(L)
        alignements=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        while coupgagnant==False or IngagnableOuPresque==False: #Ici "jouerCoup2" est la version "Normal" de notre ordinateur, on definit deux boolean "coupgagnant" et "IngagnableOuPresque"
                aligne=randint(0,7)								#on prend au debut un coup aleatoire puis on prend un alignement aleatoire entre ceux possibles et on le test dans completerAlignement
                compteur=compteur+1							    #si l'alignement est possible alors on le joue sinon on recommence en ajoutant +1 au compteur on recherche un alignement
                if compteur==5:									#que l'on analyse de nouveau ainsi de suite maximum 5 fois au bout de 5 fois soit l'ordinateur a trouver un coup interessant dans les alignements soit il joue random
                        IngagnableOuPresque=True			
                        return coup
                elif completerAlignement(damier,alignements[aligne],"O")!= -1:
                        coupgagnant=True
                        return alignements[aligne][completerAlignement(damier,alignements[aligne],"O")]
                elif completerAlignement(damier,alignements[aligne],"X")!= -1:
                        coupgagnant=True
                        return alignements[aligne][completerAlignement(damier,alignements[aligne],"X")]
def jouerCoup3(L) :
    alignements=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #on initialise la liste des alignements possibles.
    for i in range(0,len(alignements)):
        if completerAlignement(L,alignements[i],"O")!= -1:						#jouerCoup3 est la version "Impossible" de notre Ordinateur
            return alignements[i][completerAlignement(damier,alignements[i],"O")] #On teste si l'alignement est possible pour l'ordinateur dans chaque alignements, si il l'est alors on joue le coup
    for k in range(0,len(alignements)):
        if completerAlignement(damier,alignements[k],"X")!= -1:
            return alignements[k][completerAlignement(damier,alignements[k],"X")] #On teste si l'alignement est possible pour le joueur, si il l'est alors on le block
	if L==["","","","","X","","","",""]:
		caseAJouerPourNePasPerdreTour1=[0,2,6,8]	#Petite amelioration pour rendre l'ordinateur inbattable on lui explique qu'il faut jouer dans les coins si le joueur lors du  premier 
		r=randint(0,3)								#tour decide de jouer au millieu
		return caseAJouerPourNePasPerdreTour1[r]
    if L!=["","","","","X","","","",""] and (len(casesPossibles(L)))==(8):
		return (4)	#Et si le joueur ne joue pas au millieu tour 1 alors on joue au millieu
    if L==["X","","","","O","","","","X"] or L==["","","X","","O","","X","",""]:
		caseAJouerPourNePasPerdreTour3=[1,3,5,7]
		r=randint(0,3)
		return caseAJouerPourNePasPerdreTour3[r]
    else:
        return jouerCoup1(L)
def jeuGagne(L,car) :
    """Renvoie un booleen qui precise si il y a 3 symboles car alignes sur
    le damier L. On teste tous les cas favorables l'un apres l'autre..."""
    gagne=[car]*3
    # On commence par les lignes
    if L[:3]==gagne :
        res=True
    elif L[3:6]==gagne :
        res=True
    elif L[6:]==gagne :
        res=True
    # puis les colonnes
    elif [L[0],L[3],L[6]]==gagne :
        res=True
    elif [L[1],L[4],L[7]]==gagne :
        res=True
    elif [L[2],L[5],L[8]]==gagne :
        res=True
    # et enfin les diagonales
    elif [L[0],L[4],L[8]]==gagne :
        res=True
    elif [L[2],L[4],L[6]]==gagne :
        res=True
    else :
        res=False
    return res

def jeuGagne1(L,car) :
    # On definit les alignements possibles
    alignements=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    onContinue=True
    n=0
    gagne=[car]*3
    # On les passe en revue comme dans jeuGagne() en arretant si l'on trouve un alignement gagnant
    while onContinue and n<8 :
        indices=alignements[n]
        if [L[indices[0]],L[indices[1]],L[indices[2]]]==gagne :
            onContinue=False
        n+=1
    return not onContinue
     
def jeuGagne2(L,car) :
    """Ecriture alternative a jeuGagne()"""
    gagne=[car]*3
    return (L[:3]==gagne or L[3:6]==gagne or L[6:]==gagne or [L[0],L[3],L[6]]==gagne or [L[1],L[4],L[7]]==gagne or [L[2],L[5],L[8]]==gagne or [L[0],L[4],L[8]]==gagne or [L[2],L[4],L[6]]==gagne) 


## Recuperation des valeurs du formulaire
donnees=cgi.FieldStorage()
nouvJeu=donnees.getvalue("rejouer")
caseJouee=donnees.getvalue("coup")
diff=donnees.getvalue("difficulte") #Ici on recupere la difficulte enregistre
furtif="furtif" #Pour ligne 162
## Gestion des differentes situations
etatBoutonJeu="" # Par defaut, le bouton de jeu est actif, on le desactivera en cas de victoire ou de match nul
complementAffichage="" # Par defaut on se contente d'afficher le damier
if nouvJeu==None or nouvJeu=="vrai" : # On est en debut de partie ou on demande a recommencer
    damier=["","","","","","","","",""]
    sauverGrille(damier)
elif caseJouee==None : # Le joueur a appuye sur Jouer mais n'avait pas selectionne de case, on lui propose la meme grille
    damier = chargerGrille()
else : 
	# Un coup a ete joue, le jeu s'active !
    # On charge le damier puis on le met a jour, on verifie si le joueur a gagne, on regarde si
    # le damier est plein (c'est le joueur qui commence donc c'est lui qui termine)
    # l'ordinateur joue, on verifie s'il a gagne, on sauvegarde la damier et
    # on renvoie le damier vers le joueur.
    # A la fin de chaque situation on construit le damier a afficher.
    damier = chargerGrille()
    damier[int(caseJouee)]="X"
    if jeuGagne1(damier,"X") :
        etatBoutonJeu=furtif #desactivation du bouton de jeu
        complementAffichage="\n<a title='VICTOIRE !!!' href='http://144.91.84.212/cgi-bin/hello.py'><p class='scale-effect'>|>>>> Bien Joue Victoire ! <<<<|</p>" #Petit changement du message de victoire.
    elif casesPossibles(damier)==[] :
        etatBoutonJeu='furtif'
        complementAffichage="\n<p>La partie se termine sur un nul</p>"
    else :
		if diff=="Impossible":
			pos=jouerCoup3(damier)		#Donc ici c'est la que l'ordinateur vas jouer sont coup 
			damier[pos]="O"				#Il joue en fonction de la difficulte recuperee
		elif diff=="Normal":			#Impossible correspond a jouerCoup3
			pos=jouerCoup2(damier)		#Normal correspond a jouerCoup2
			damier[pos]="O"				#Et si ce n'est ni impossible ni normal alors on est en facile = jouerCoup1
		else:
			pos=jouerCoup1(damier)
			damier[pos]="O"
		if jeuGagne(damier,"O") :
			etatBoutonJeu='furtif'
			complementAffichage="\n<p>Vous perdez mais l'ordinateur etait vraiment trop fort !</p>"
		sauverGrille(damier)
    # Creation de la page du jeu
    # On met deux <input> non affiches pour gerer les differentes situations
    # Ces input renvoie toujours quelque chose, ainsi quand la variable est
    # vide on sait que la page vient de s'ouvrir
    # Les imput contiennent la variable rejouer qui vaut faux dans le formulaire associe
    # au bouton Jouer et vrai dans le formulaire associe au bouton Recommencer une partie
print("""
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>morpion</title>
    <link rel="stylesheet" type="text/css" href="http://144.91.84.212/morpion.css">
</head>
<body>""")
if diff==None:
	print("""<header>Morpion </header>""")
else:
	print("""<header>Morpion {} </header>""").format(diff) 	#J'ai rajouter le nom de la difficulte au titre.
print("""<p>On joue avec les X, l'ordinateur joue avec les O. Il y a un bouton pour jouer le coup selectionne et un bouton pour recommencer la partie au depart</p>""")
print("""<form method="GET" action="morpionAcompleter2.py">
<select class="buttons3 scale-effect"  name="difficulte">""")
if diff=="Impossible":
	print("""<option value="Impossible">Impossible</option>""")
elif diff=="Facile":
	print("""<option value="Facile">Facile</option>""")		#Ici on desactive le choix de la difficulte apres le 1er coup
elif diff=="Normal":										#Ainsi le joueur ne peux plus changer de difficulte (sauf dans l'url)
	print("""<option value="Normal">Normal</option>""")		#Et si le programme ne trouve aucune difficulte dans "diff" alors
else:														#cela veux dire qu'on est au debut de la partie et on laisse le choix
	print("""<option value="Facile">Facile</option>
			 <option value="Normal">Normal</option>""")
	print("""<option value="Impossible">Impossible</option>""")
print("""
			 </select>		 
			 <input type="texte" class="furtif" name="rejouer" value="faux">""")
print(construireDamier(damier)+complementAffichage)
print("""<input class="scale-effect buttons2 {}"   type='submit' value='Jouer'>\n</form>""".format(etatBoutonJeu))
print("""<form method="GET" action="morpionAcompleter2.py">
             <input class="furtif" type="texte" name="rejouer" value="vrai">
             <input class="scale-effect buttons" type="submit" value="Recommencer une nouvelle partie">
             </form>
</body>
</html>
""")
