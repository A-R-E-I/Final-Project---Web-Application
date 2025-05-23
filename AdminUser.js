window.addEventListener("load",addListener);

function addListener()
{
	document.getElementById("entAct").addEventListener("click",selectAct);
	document.getElementById("entExit").addEventListener("click",Exit);
}

function selectAct()
{
	numAct = document.getElementById("WhatAccount").value;
	if(numAct == ""):
		window.location.href="AdminUser.html";
}

function Exit()
{
	window.location.href = "RUsure.html";
}