$(document).ready(function(){
	$("#message").animate( { scrollTop: $("#message").height()}, 700);
	var put = window.location.pathname;
	// alert( put);
	// var result = $(put).val();
	var result = put.split('/');
	var id = result[result.length-2];
	//alert(id);
});
