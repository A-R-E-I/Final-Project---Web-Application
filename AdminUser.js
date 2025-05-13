window.addEventListener("load",addListener);

function addListener()
{
	document.getElementById("btnadmin").addEventListener("click",Admin);
	document.getElementById("btnuser").addEventListener("click",User);
}

function Admin()
{
	window.location.href="ExtractAdmin.html";
}

function User()
{
	window.location.href="ExtractUser.html";
}