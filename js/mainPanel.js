
$(document).ready(function() {
    $("button").css({
	"width":465, // use this as max width
	"height":150,
	"font-size":"50px",
	"background-color":"cyan"
    });
    $("h2").text(window.screen.width+"x"+window.screen.height);
    $("button").click(function() {
	var cStatus = (function () {
	    var json = null;
	    $.ajax({
		'async': false,
		'global': false,
		'url': "cgi-bin/hello.py/swapLED",
		'dataType': "json",
		'success': function (data) {
		    json = data;
		}
	    });
	    return json.currentStatus;
	})(); 
	console.log(cStatus);
	if (cStatus == 1) {
	    $(this).text("ON");
	    $(this).css({
		"background-color":"green"
	    });
	} else {
	    $(this).text("OFF");
	    $(this).css({
		"background-color":"red"
	    });
	}
    });
});

