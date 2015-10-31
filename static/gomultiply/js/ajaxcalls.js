

$('document').ready(function (){
	console.log('ready!');
	$('#signup-form').submit(function(event){
		event.preventDefault();
		return false;
	})
})

