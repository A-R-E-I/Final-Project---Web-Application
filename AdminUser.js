window.addEventListener("load",addListener);

function addListener()
{
	document.getElementById("entAct").addEventListener("click",selectAct);
	document.getElementById("entExit").addEventListener("click",Exit);
}

function selectAct()
{
	numAct = document.getElementById("WhatAct").value;
}

function Exit()
{
	window.location.href="ExtractUser.html";
}