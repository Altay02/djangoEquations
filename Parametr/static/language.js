/*eslint-env browser*/
//"use strict";
var navEng = document.getElementsByClassName("eng"),
	navRu = document.getElementsByClassName("ru"),
	langBtn = document.getElementsByClassName("checkbox");
langBtn.onclick = function () {
	if (navEng.style.display === "none") {
		navEng.style.display = "inline";
		navRu.style.display = "none";
	} else {
		navEng.style.display = "none";
		navRu.style.display = "inline";
	}
};

function changeLang() {
	if (navEng.style.display === "none") {
		navEng.style.display = "inline";
		navRu.style.display = "none";
	} else {
		navEng.style.display = "none";
		navRu.style.display = "inline";
	}
}