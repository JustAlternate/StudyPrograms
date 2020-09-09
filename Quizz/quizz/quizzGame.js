//Le jeux (scores)
var n=0;
var score=0;
var HighestScore=0;
const SAVE_KEY_SCORE ="highestscore";
const Last_JOUEUR="lastjoueur"
var joueurStr=localStorage.getItem(Last_JOUEUR);
var scoreStr=localStorage.getItem(SAVE_KEY_SCORE);
if(scoreStr==null){
	HighestScore=0;
}
else{
	HighestScore=parseInt(scoreStr);
}
if(joueurStr==null){
	LastJoueur=0;
}
else{
	LastJoueur=joueurStr;
}

// Reset own top score boiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiis

function ResetTopScore(){
	var v = prompt("Es-tu sur de vouloir effacer à jamais ton meilleur score ? oui ou non :", "");
	if (v=="oui"){
		HighestScore=0
		localStorage.setItem(SAVE_KEY_SCORE,HighestScore)
		LastJoueur="none"
		localStorage.setItem(Last_JOUEUR,LastJoueur)
	}
	else {window.location.href = "http://justalternate.pw/cedricexplosesatetedanssonclavier.mp4";}
}

//fonction verification

function questionRandom(nbrRep){
  if (nbrRep!=0){ //on test si on est pas au lancement du script
    if(n<Questions.length-1){ //on test si on est pas au bout des questions
          var nbr=nbrRep.toString(); //on transorme nbrRep en string
          var reps="Rep"+nbr; //on concatenne les deux pour obtenir l'id du bouton presse (Rep1/Rep2/Rep3/Rep4)
          var pass=document.getElementById("pass");
          var fail=document.getElementById("fail");
          if (document.getElementById(reps).value==Reponsegagnante[n]){ //si la reponse est la bonne
                  score+=1 //on ajoute un
                  pass.style.display="block";
                  fail.style.display="none";
                  document.getElementById("Reponse").style.display="none";
                }
          else{
                  score-=1
                  fail.style.display="block";
                  pass.style.display="none";
                  document.getElementById("Reponse").style.display="block"; //on affiche la reponse attendu
                  document.getElementById("Reponse").innerHTML="La reponse attendu etait '" + Reponsegagnante[n] + "'";
                }
          n+=1; //compteur pour savoir a quelle question on en est
    }
    else{
      n=0 //on a fait le tour des questions on revient au debut
    }
  }
  //on affiche les question et reponses + le personal_Best_Score
        document.getElementById("score-number").innerHTML=score;
        document.getElementById("Question").innerHTML=Questions[n];
        document.getElementById("Rep1").value=(Reponses[4*n]);
        document.getElementById("Rep2").value=(Reponses[4*n+1]);
        document.getElementById("Rep3").value=(Reponses[4*n+2]);
        document.getElementById("Rep4").value=(Reponses[4*n+3]);
		document.getElementById("Rep1").style.display="block";
        document.getElementById("Rep2").style.display="block";
        document.getElementById("Rep3").style.display="block";
        document.getElementById("Rep4").style.display="block";  //on affiche toutes les réponses dans le cas ou le 50/50 a ete active
  return(score,n)
}





//Le timer adapter de : https://gist.github.com/steveosoule/5053007 (merci a lui)

var mins = 1.1;
var secs = mins * 60;

// On n'utilise plus le ResetTime mais on le garde sous le coude.

function ResetTime(){
      mins = 1.1;
      secs = mins * 60;
      return(secs)
}

function countdown() {
  setTimeout('Decrement()', 60);
}

function cinquante_cinquante(){
	var p=0 
	var questionRandomRestante=Math.floor(Math.random() * Math.floor(4)); 
		
	if(Reponsegagnante[n]!=Reponses[4*n]){
		while (Reponses[4*n+p]!=Reponsegagnante[n]){
			p+=1
		}
	}
	
	while(questionRandomRestante==p){
		questionRandomRestante=Math.floor(Math.random() * Math.floor(4));
	}
	questionRandomRestante+=1; //on s'aligne avec le nombre des questions (si l'indice est 0 alors la question sera la première donc Rep1)
	p+=1;
	
	document.getElementById("moitmoit").style.display="none"; //on cache le bouton pour ne plus le réutilisez
	document.getElementById("Rep1").style.display="none"; //on cache tout
	document.getElementById("Rep2").style.display="none";
	document.getElementById("Rep3").style.display="none";
	document.getElementById("Rep4").style.display="none";
	var nbr1=questionRandomRestante.toString(); //on transorme nbrRep en string
	var rep1="Rep"+nbr1;
	var nbr2=p.toString(); //on transorme nbrRep en string
	var rep2="Rep"+nbr2;
	document.getElementById(rep1).style.display="inline"; //on réaffiche les deux réponses
	document.getElementById(rep2).style.display="inline";
}

function Decrement() {
	minutes = document.getElementById("minutes");
	seconds = document.getElementById("seconds");
	document.getElementById("LastJoueur").innerHTML=LastJoueur // On affiche le personal_Best_Score

	if(score>=HighestScore){
		HighestScore=score;
		localStorage.setItem(SAVE_KEY_SCORE,HighestScore)
	}

	if (seconds < 59) {
		seconds.value = secs;
	}

	else {
		minutes.value = getminutes();
		seconds.value = getseconds();
	}
	if (mins < 1) {
		minutes.style.color = "red";
		seconds.style.color = "red";
	}
	
	if (mins < 0) {
		minutes.value = 0;
		seconds.value = 0;
		alert("Timer fini")
		if (score>=HighestScore){
		var v = prompt("GG tu viens de PETER ton meilleur score !, c'est quoi ton petit nom ?:", "");
		var x=new Date().toLocaleString();
		var g=v+" : "+score+" [ "+x+" ] "
		LastJoueur=g
		localStorage.setItem(Last_JOUEUR,LastJoueur)
		document.getElementById("LastJoueur").innerHTML=LastJoueur
		}
	}
	
	else {
		secs--;
		setTimeout('Decrement()', 1000);
	}
}

function getminutes() {
    mins = Math.floor(secs / 60);
    return mins;
}

function getseconds() {
    return secs - Math.round(mins * 60);
}


//Le lancement du quizz, on initialize tout et on lance la fonction questionRandom avec en parametre 0 (debut)

function quizz(){
    return(
    questionRandom(0),
    document.getElementById("User").style.display="block",
    document.getElementById("Question").style.display="block",
    document.getElementById("Rep1").style.display="inline",
    document.getElementById("Rep2").style.display="inline",
    document.getElementById("Rep3").style.display="inline",
    document.getElementById("Rep4").style.display="inline",
    document.getElementById("Reponse").style.display="none",
    document.getElementById("startingButton").style.display="none",
    document.getElementById("titre").innerHTML="Repondez au questions avant la fin du timer !",
    document.getElementById("seconds").style.display="inline",
    document.getElementById("minutes").style.display="inline",
    document.getElementById("commalike").style.display="inline",
    document.getElementById("compteur").style.display="block",
	document.getElementById("moitmoit").style.display="block",
    countdown())
}

//fonction de redirection
function redirect(){
  alert("error");
  window.location.href = "http://justalternate.pw/quizz/QuizzLogin.html";
}
