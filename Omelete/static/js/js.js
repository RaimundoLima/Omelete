	$(window).on('load', function () {
	$('#pesquisar').focus();
    $('#preloader .inner').fadeOut();
    $('#preloader').delay(5).fadeOut('slow'); 
    $('body').delay(5).css({'overflow': 'visible'});
});
	  M.AutoInit();
	//M.updateTextFields();
  $(document).ready(function(){
    $("a").click(function(){
    $(this).toggleClass("yellow");
    });
});