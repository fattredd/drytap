function PINctrl(q,t) {
    var json = null;
    $.ajax({
	'async': false,
	'global': false,
	'url': "cgi-bin/hello.py/swapPIN?q="+q+"&t="+t,
	'dataType': "json",
	'success': function (data) {
	    json = data;
	}
    });
    return json.currentStatus;
}

function updateBttn(q,t) {
    var bttn = $("button[pin="+q+"]");
    var cStatus = PINctrl(q,t);
    if (cStatus == 1) {
	//bttn.text("ON");
	bttn.css({
	    "background-color":"green"
	});
    } else {
	//bttn.text("OFF");
	bttn.css({
	    "background-color":"red"
	});
    }
}

window.setInterval(function(){
    $("button").each(function () {
	updateBttn($(this).attr("pin"),0);
    });    
}, 100);

$(document).ready(function() {
    $("button").css({
	"width":230, // use 465 as max width
	"height":150,
	"font-size":"50px",
	"background-color":"cyan"
    });
    $(".fullw").css({
	"width":465
    });
    //$("h2").text(window.screen.width+"x"+window.screen.height);
    $("button").click(function() {
	var q = $(this).attr("pin");
	updateBttn(q,1);
    });
});

