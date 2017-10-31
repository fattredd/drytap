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
    if (json == null) {
	console.log("Error with pin "+q+" and toggle="+t);
	return false;
    } else {
	return json.currentStatus;
    }
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

function Auto(t) {
    var bttn = $("#auto")
    var json = null;
    $.ajax({
	'async': false,
	'global': false,
	'url': "cgi-bin/hello.py/Auto?t="+t,
	'dataType': "json",
	'success': function (data) {
	    json = data;
	    console.log(json.currentStatus)
	}
    });
//    console.log(json.currentStatus)
    if (json.currentStatus == 1) {
	bttn.css({
	    "background-color":"green"
	});
    } else {
	bttn.css({
	    "background-color":"red"
	});
    }
}

window.setInterval(function(){
    $("button").each(function () {
	if ($(this).attr("pin")) {
	    //console.log("Updating pin "+$(this).attr("pin"));
	    updateBttn($(this).attr("pin"),0);
	}
    });
    Auto(0);
}, 500);

$(document).ready(function() {
    $("button").css({
	"width":210, // use 465 as max width
	"height":150,
	"font-size":"50px",
	"background-color":"cyan"
    });
    $(".fullw").css({
	"width":465
    });
    $("button").click(function() {
	console.log("Clicked "+$(this).attr("pin"));
	updateBttn($(this).attr("pin"),1);
    });
    $("#auto").click(function() {
	Auto(1);
    });
});

