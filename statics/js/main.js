;(function () {

	'use strict';

	// iPad and iPod detection	
	var isiPad = function(){
		return (navigator.platform.indexOf("iPad") != -1);
	};

	var isiPhone = function(){
		return (
			(navigator.platform.indexOf("iPhone") != -1) || 
			(navigator.platform.indexOf("iPod") != -1)
		);
	};


	// Loading page
	var loaderPage = function() {
		$(".fh5co-loader").fadeOut("slow");
	};






	var styleToggle = function() {


		if ( $.cookie('styleCookie') !== undefined ) {
			if ( $.cookie('styleCookie') === 'style-light.css'  ) { 

				$('.js-style-toggle').attr('data-style', 'light');
			} else  {
				$('.js-style-toggle').attr('data-style', 'default');
			}
			$('#theme-switch').attr('href', '/static/css/' + $.cookie('styleCookie'));
		} 
		if ( $.cookie('btnActive') !== undefined ) $('.js-style-toggle').addClass($.cookie('btnActive'));
		// $('.js-style-toggle').on('click', function(){
		$('body').on('click','.js-style-toggle',function(event){
			var data = $('.js-style-toggle').attr('data-style'), style = '', $this = $(this);
			if ( data === 'default') {

				// switch to light
				style = 'style-light.css';
				$this.attr('data-style', 'light');

				// add class active to button
				$.cookie('btnActive', 'active', { expires: 365, path: '/'});
				$this.addClass($.cookie('btnActive'));
			} else {
				// switch to dark color
				style = 'style.css';
				$this.attr('data-style', 'default');

				// remove class active from button
				$.removeCookie('btnActive', { path: '/' });
				$(this).removeClass('active'); 

				// switch to style
				$.cookie('styleCookie', style, { expires: 365, path: '/'});

			}

			// switch to style 
			$.cookie('styleCookie', style, { expires: 365, path: '/'});

			// apply the new style
			$('#theme-switch').attr('href', '/static/css/' + $.cookie('styleCookie'));


			event.preventDefault();

		});

	}

	$(function(){
		// gotToNextSection();
		loaderPage();
		// ScrollNext();
		styleToggle();
		// contentWayPoint();
	});


}());


$(document).ready(function() {

	$("body").css("display", "none");

	$("body").fadeIn(2000);
	$("body").stop().animate({
		opacity: 1
	});


	$("a.transition").click(function(event){

		event.preventDefault();
		linkLocation = this.href;
		$("body").fadeOut(1000, redirectPage);		

	});

	function redirectPage() {
		window.location = linkLocation;
	}

});

