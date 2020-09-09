#Taking a random line into a .txt file

from random import randint

dico=open("dicos/dictionary.txt","r")

AllWords=[]

dico.readline()

for ligne in dico:
    val=ligne.rstrip("\n")
    AllWords.append(val)
    
randomword=AllWords[randint(0,len(AllWords)]

dico.close()

print(randomword)
