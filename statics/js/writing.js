$(function(){
	$(".writingform #id_title").addClass("form-control")
	$(".writingform #id_category").addClass("form-control")
	$(".writingform #id_tag").addClass("form-control")

})
$(function(){
	$(".writingform p textarea").markdown(
		{
			autofocus:false,
			savable:false,
			hiddenButtons:"cmdPreview",
			disabledButtons:"cmdPreview",
		});
});
