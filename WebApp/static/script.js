function getBotResponse() {
	var rawText = $("input:text").val().trim();
	var userHtml = '<p class="text-right"><img src="../static/messenger.png" height="31" width="27">&nbsp;&nbsp;<span class="bg-success text-white rounded p-1">' + rawText + '</span></p>';
	$("input:text").val("");
	$("#chatbox").append(userHtml);
	document.getElementById('formInput').scrollIntoView({
		block : 'start',
		behavior : 'smooth'
	});
	$.get("/get", {
		msg : rawText
	}).done(function(data) {
		var botHtml = '<p class="text-left"><img src="../static/chatbot.jpg" height="31" width="27">&nbsp;&nbsp;<span class="bg-info text-white rounded p-1">' + data + '</span></p>';
		$("#chatbox").append(botHtml);
		document.getElementById('formInput').scrollIntoView({
			block : 'start',
			behavior : 'smooth'
		});
	});
}
$("input:text").keypress(function(e) {
	if (e.which == 13 && $("input:text").val().trim() != "") {
		getBotResponse();
	}
});
$("input:submit").click(function() {
	if ($("input:text").val().trim() != "") {
		getBotResponse();
	}
});