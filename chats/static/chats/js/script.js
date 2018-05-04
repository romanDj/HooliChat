$(document).ready(function(){

	

	$("#backBtn").click(function(){
		$("#message").parent().css({'display':'none'});
		$("#listChats").css({'display':'block'});			
	});

	$("#listChats>div>a").click(function(){
		if($(window).width()<992){
			$("#message").parent().css({'display':'block'});
			$("#listChats").css({'display':'none'});
		}
			
	});

	$(window).resize(function(){
		if($(window).width()>992){
			$("#listChats").css({'display':'block'});
		}else{
			$("#message").parent().css({'display':'block'});
			$("#listChats").css({'display':'none'});
		}
	});
});