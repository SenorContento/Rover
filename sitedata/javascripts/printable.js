var print = false;

function printable() {
var _style;
    if(print == false) {
	print = true;
	$("#pc-style").attr("href", "/sitedata/stylesheets/print.css");
	$("#mobile-style").attr("href", "/sitedata/stylesheets/print.css");
	$("#printable-link").text("Normal Version");
	$("div").each(function() {
		_style = $(this).attr("style");
   		$(this).attr("style", 'color:black');
	});
	$("span").each(function() {
		_style = $(this).attr("style");
   		$(this).attr("style", 'color:black');
	});
	$("#comment-hr").hide();
	$("#comment-br").hide();
        $("#social-br").hide();
	$("#disqus_thread").hide();
	$("#general").hide(); /* This is the Navigation Menu */
	$("#desktop-site").hide(); /* This is the Show Desktop Site Link */
    }
    else {
	/*print = false;
	$("#pc-style").attr("href", "/sitedata/stylesheets/stylesheet.css");
	$("#mobile-style").attr("href", "/sitedata/stylesheets/mobile-stylesheet.css");
	$("#printable-link").text("Printable Version");
	$("#social-hr").show();
	$("#social-br").show();
	$("#like-share").show();
	$("#like-share").hide();*/
	
	window.location = "";
	/* I would record the text colors and reverse them, but that means I have to keep track of arrays. Maybe in the future I will change the code to do that, but right now, refreshing the page is all I have time to do right now */
    }
}
