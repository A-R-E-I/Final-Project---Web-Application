window.addEventListener("load",addListener);

function addListener()
{
	document.getElementById("btnmiddleschool").addEventListener("click",gohtml);
	document.getElementById("btnhighschool").addEventListener("click",gohtml);
}

function gohtml()
{
	window.location.href = "piinput.html";
}