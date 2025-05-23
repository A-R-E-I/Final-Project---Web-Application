window.addEventListener("load",addListener);

function addListener()
{
	document.getElementById("btnmiddleschool").addEventListener("click",gohighhtml);
	document.getElementById("btnhighschool").addEventListener("click",gomiddlehtml);
}

function gohighhtml()
{
	window.location.href = "piinputhard.html";
}

function gomiddlehtml()
{
	window.location.href = "piinputmiddle.html";
}