//on n'utilise plus c'est function mais on les gardes au cas ou

function GoToLogin(){
	window.location.href="http://justalternate.pw/quizz/QuizzLogin.html";
}
function GoToRegister(){
	window.location.href="http://justalternate.pw/quizz/QuizzRegister.html";
}
function GoToTitle(){
	window.location.href="http://justalternate.pw/quizz/";
}
function GoToAdd(){
	window.location.href="http://justalternate.pw/quizz/QuizzAdd.html";
}

//Effets stylés sur le register

function indicationMdp(){
	var DocInputMdp=document.getElementById("inputMdp")
	return(
	DocInputMdp.value="",
	DocInputMdp.type="password",
	DocInputMdp.style.fontStyle="normal",
	DocInputMdp.style.color="black",
	DocInputMdp.style.textAlign="left",
	DocInputMdp.style.borderColor="black",
	DocInputMdp.style.borderWidths="10px"
	)
}


function indicationLogin(){
	var DocInputLog=document.getElementById("inputLogin")
	return(
	DocInputLog.value="",
	DocInputLog.style.fontStyle="normal",
	DocInputLog.style.color="black",
	DocInputLog.style.textAlign="left",
	DocInputLog.style.borderColor="black",
	DocInputLog.style.borderWidths="10px"
	)
}

//Ici la partie qui vous interesse


//Test lorsque l'utilisateur tape le mot de passe

function mdpvalide(){
	var a=document.getElementById("inputMdp").value;
	var b=document.getElementById("inputLogin").value;

	if (a.length<=8){
		return(
		document.getElementById("inputMdp").style.borderColor="red",
		document.getElementById("inputMdp").style.borderWidths="10px"
		)
	}
	else{
		return(
		document.getElementById("inputMdp").style.borderColor="black",
		document.getElementById("inputMdp").style.borderWidths="10px"
		)
	}
}

//Test apres validation

function verif(){
	var DocInputMdp=document.getElementById("inputMdp")
	var DocInputLog=document.getElementById("inputLogin")
	var a=document.getElementById("inputMdp").value;
	var b=document.getElementById("inputLogin").value;
	if (a.length<=8){
		alert("Mot de passe trop court, tu veux te faire hacker ou quoi ?")
		DocInputMdp.value="";
		DocInputMdp.style.borderColor="red";
		DocInputMdp.style.borderWidths="10px";
		return false
	}
	if ((b.indexOf(" "))!=-1){
		alert("Il ne peut pas avoir d'espace dans ton pseudo")
		DocInputLog.value="";
		DocInputLog.style.borderColor="red";
		DocInputLog.style.borderWidths="10px";
		return (false)
	}
	if ((b.length)==0){
		alert("trouve un pseudo stp")
		DocInputLog.value="";
		DocInputLog.style.borderColor="red";
		DocInputLog.style.borderWidths="10px";
		return false
	}
	if (b==" "){
		alert("trouve un pseudo stpe")
		DocInputLog.value="";
		DocInputLog.style.borderColor="red";
		DocInputLog.style.borderWidths="10px";
		return false
	}
	else{
		return true
	}
}
