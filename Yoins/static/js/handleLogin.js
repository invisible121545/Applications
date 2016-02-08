(function () {
	$(document).on('submit','form.login_form',function(e){
		e.preventDefault();
		var username = $("input[name=username]").val(),
			admin_pass = $("input[name=admin_pass]").val();
		console.log(admin_pass);
		$.ajax({
			type:"post",
			url:"/Yoins/checkSign/",
			data:{
				admin_name:username,
				admin_pass:admin_pass
			},
			async:true,
			success:function(res){
				console.log(res);
				if(!res){					
					$("small.msg").text('Wrong Email or password')
				}
			}
		});
	})
})();