window.addEventListener("load",addListener);

function addListener()
{
	document.getElementById("btnmiddleschool").addEventListener("click",gomiddlehtml);
	document.getElementById("btnhighschool").addEventListener("click",gohighhtml);
}

function gohighhtml()
{
	window.location.href = "piinputhard.html";
}

function gomiddlehtml()
{
	window.location.href = "piinputmiddle.html";
}