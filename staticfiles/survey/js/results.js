$(document).ready(function(){
	var ctx = $("#ageChart");
	var agePie = new Chart(ctx, {
		type: 'pie',
		data: data,
		options: {},
	})
});

