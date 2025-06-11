window.addEventListener("load",addListener);

function addListener()
{
	document.getElementById("entyes").addEventListener("click",Exit);
	document.getElementById("entno").addEventListener("click",Stay);
}

function Exit()
{
	window.location.href = "EndPro.html";
}

function Stay()
{
	window.location.href = "AdminUser.html";
}