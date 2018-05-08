$(document).ready(function(){
	

	//получение выбранного собеседника
	var put = window.location.pathname;
	var result = put.split('/');
	var id = result[result.length-2];

	var recipientNow = 0;
	//загрузка диалога с ним
	if($.isNumeric(id) == true){
		recipientNow = id;
		$(".all_messages").html("<div class='mb-3  rounded p-2'>vdfd</div><div class='date-wrapper clear mb-3 rounded'><p class='date p-3'>23 апреля 2018</p></div><div class='mb-3 rounded float-right p-3'>"+
						"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"+

						"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse"+
						"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non"+
						"proident, sunt in culpa qui officia deserunt mollit anim id est laborum."+
					"</div>"+
					"<div class='clear'></div>"+
					"<div class='mb-3 p-3  rounded float-left'>"+
						"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"+
						"tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"+
						"quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"+
						"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse"+
						"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non"+
						"proident, sunt in culpa qui officia deserunt mollit anim id est laborum."+
					"</div>"+
					"<div class='clear'></div>"+
					"<div class='mb-3 p-3  rounded float-left'>"+
						"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"+
						"tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"+
						"quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"+
						"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse"+
						"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non"+
						"proident, sunt in culpa qui officia deserunt mollit anim id est laborum."+
					"</div>"+
					"<div class='date-wrapper clear mb-3 rounded'><p class='date p-3'>23 апреля 2018</p></div>"+
					"<div class='mb-3 p-3  rounded float-right'>"+
						"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"+
						"tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"+
						"quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"+
						"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse"+
						"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non"+
						"proident, sunt in culpa qui officia deserunt mollit anim id est laborum."+
					"</div>"+
					"<div class='clear'></div>");
		$("#message").scrollTop( $(".all_messages").height());
	}

	$(".nickname").click(function(){
		recipientNow = $(this).attr('data-id');
	});

	$("#listChats div a").click(function(event){
		event.preventDefault();
		$(".all_messages").html("<div class='mb-3  rounded p-2'>vdfd</div><div class='date-wrapper clear mb-3 rounded'><p class='date p-3'>23 апреля 2018</p></div><div class='mb-3 rounded float-right p-3'>"+
						"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"+

						"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse"+
						"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non"+
						"proident, sunt in culpa qui officia deserunt mollit anim id est laborum."+
					"</div>"+
					"<div class='clear'></div>"+
					"<div class='mb-3 p-3  rounded float-left'>"+
						"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"+
						"tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"+
						"quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"+
						"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse"+
						"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non"+
						"proident, sunt in culpa qui officia deserunt mollit anim id est laborum."+
					"</div>"+
					"<div class='clear'></div>"+
					"<div class='mb-3 p-3  rounded float-left'>"+
						"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"+
						"tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"+
						"quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"+
						"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse"+
						"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non"+
						"proident, sunt in culpa qui officia deserunt mollit anim id est laborum."+
					"</div>"+
					"<div class='date-wrapper clear mb-3 rounded'><p class='date p-3'>23 апреля 2018</p></div>"+
					"<div class='mb-3 p-3  rounded float-right'>"+
						"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"+
						"tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"+
						"quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"+
						"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse"+
						"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non"+
						"proident, sunt in culpa qui officia deserunt mollit anim id est laborum."+
					"</div>"+
					"<div class='clear'></div>");
		$("#message").scrollTop( $(".all_messages").height());
	});

	$("#submitBtn").click(function(){
		if($("#messageContent").val()!=""){
			$.ajax({
				type:'GET',
				url:'/addmessage',
				data: {'recipient': recipientNow, 'text': $("#messageContent").val()},
			});
			$(".all_messages").append("<div class='mb-3 p-3  rounded float-right'>"+
							$("#messageContent").val()+
						"</div>"+
						"<div class='clear'></div>");
			
			$("#messageContent").val('');
			$("#message").scrollTop( $(".all_messages").height());
			console.log($(".all_messages").height());
		}
	});

});
