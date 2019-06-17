var loginNameIsOk = true
var pwdIsOk = true

$(document).ready(function(){
   
   var pos = $(".loginbox .head a").eq(1).position();
   var width = $(".loginbox .head a").eq(1).width();
    
   $(".loginbox .bottomline").css({'left':pos.left+'px','width':width+'px'});
   $(".loginbox .ct .item").eq(1).show();

  
   $(".loginbox .head a").click(function(){
   	   var index = $(this).index();
   	  
   	   $(".loginbox .ct .item").hide();
   
   	   $(".loginbox .ct .item").eq(index).show();
   	
   	   pos = $(this).position();
       width = $(this).width();       
       $(".loginbox .bottomline").animate({'left':pos.left+'px','width':width+'px'},300);
       
       $(this).addClass('sel').siblings().removeClass("sel");
   });
 
   $(".delusername").click(function(){
   		$("input[name='username']").val('');
   });

 
   $(".outbox").click(function(){
   	   $(this).find(".checkbox").toggleClass('sel');
   });

   $(".loginBtn").click(function(){
   	   var password = $("input[name='password']").val().trim();
      /* var patrn_0 = /^[1-9][0-9]{5,12}$/;//验证手机号或qq号*/

     /*  var patrn_1= /^[1-9][0-9]{4,}@qq\.com$/;//验证邮箱  */
	   if(!loginNameIsOk){
	   	return;
	   }

        if(password.length<8)
        {
        	$(".logintip").html('请正确输入密码');
			 alert("请输入正确密码");
   	   	   return;
        }
		if(event.keyCode==13){
			alert(event)
			return;
			
			}
		else{
			$("#myform2").submit();
			}

   });

   //清空
   $(".loginbox .inputbox input").focus(function(){
   	   $(".logintip").html('');
   });

});




