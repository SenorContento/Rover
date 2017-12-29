/*var jQuery = document.createElement('script');
jQuery.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js";
document.head.appendChild(jQuery);*/ /*Could Work, but Not Tested */

var getStr = window.location.search.substr(1);
var getArray = getStr.split ("&");
var get = {};

for (var i = 0; i < getArray.length; i++) {
    var tmpArray = getArray[i].split("=");
    get[tmpArray[0]] = tmpArray[1];
}

if (screen.width <= 800) { 
    if (get.m == "no") {
	//alert("Mobile Phone on PC");
	$(document).ready(function(){
		$("#mobile-style").attr("href", "/sitedata/stylesheets/stylesheet.css");
		$("a").each(function() {
   			var _href = $(this).attr("href"); 
   			$(this).attr("href", _href + '?m=no');
		});
		$("#desktop-site").text("Show Mobile Site");
		$("#desktop-site").css("display","inline");
		$('#desktop-site').click(function(){
			window.location = window.location.href.split("?")[0];
		});
	});
    }
    else {
	//alert("Mobile Phone" + " SW: " + screen.width);
	$(document).ready(function(){
		$('head').append("<meta content='width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=yes' name='viewport' />");
		$('#desktop-site').click(function(){
			var location = window.location.href.split("#")[0];
			location = location.split("?")[0];
			window.location = location + "?m=no";
		});
	});
    }
}
else {
    if (get.m == "yes") {
	//alert("PC on Mobile Phone");
	$("#pc-style").attr("href", "/sitedata/stylesheets/mobile-stylesheet.css");
	$(document).ready(function(){
		$("a").each(function() {
   			var _href = $(this).attr("href"); 
   			$(this).attr("href", _href + '?m=yes');
		});
		$('head').append("<meta content='width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=yes' name='viewport' />");
		$('#desktop-site').click(function(){
			window.location = window.location.href.split("?")[0] + "?m=no";
		});
	});
    }
    else {
	//alert("PC " + screen.width);
    }
}

/* This file is used to allow the user to override the settings that were set by the lines
<link id="mobile-style" rel="stylesheet" type="text/css" href="/sitedata/stylesheets/mobile-stylesheet.css" media="screen and (max-device-width: 800px)"/>
<link id="pc-style" rel="stylesheet" type="text/css" href="/sitedata/stylesheets/stylesheet.css" media="screen and (min-device-width: 800px)">
*/
