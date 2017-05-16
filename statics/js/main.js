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


	// Go to next section
	var gotToNextSection = function(){
		var el = $('.fh5co-learn-more'),
			w = el.width(),
			divide = -w/2;
		el.css('margin-left', divide);
	};

	// Loading page
	var loaderPage = function() {
		$(".fh5co-loader").fadeOut("slow");
	};



	// Scroll Next
	var ScrollNext = function() {
		$('body').on('click', '.scroll-btn', function(e){
			e.preventDefault();

			$('html, body').animate({
				scrollTop: $( $(this).closest('[data-next="yes"]').next()).offset().top
			}, 1000, 'easeInOutExpo');
			return false;
		});
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

	// Animations

	var contentWayPoint = function() {
		var i = 0;
		$('.animate-box').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('animated') ) {
				i++;
				$(this.element).addClass('item-animate');
				setTimeout(function(){
					$('body .animate-box.item-animate').each(function(k){
						var el = $(this);
						setTimeout( function () {
							el.addClass('fadeInUp animated');
							el.removeClass('item-animate');
						},  k * 200, 'easeInOutExpo' );
					});

				}, 100);

			}

		} , { offset: '95%' } );
	};


	var moreProjectSlider = function() {
		$('.flexslider').flexslider({
			animation: "slide",
			animationLoop: false,
			itemWidth: 310,
			itemMargin: 20,
			controlNav: false
		});
	}


	// Document on load.
	$(function(){

		gotToNextSection();
		loaderPage();
		ScrollNext();
		moreProjectSlider();
		styleToggle();

		// Animate
		contentWayPoint();

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

// add markdown attr
$(function(){
Dropzone.autoDiscover = false;
	$(".container .col-md-12 .writingform p textarea").markdown(
		{
			autofocus:true,
			savable:false,
			additionalButtons: [
				[{
					name: "groupCustom",
					data: [{
						name: "cmdBeer",
						toggle: true,
						title: "upload",
						icon: "glyphicon glyphicon-user",
						callback: function(e){
							// Replace selection with some drinks
							var chunk, cursor,
								selected = e.getSelection(), content = e.getContent(),
								drinks = ["Heinekken", "Budweiser",
									"Iron City", "Amstel Light",
									"Red Stripe", "Smithwicks",
									"Westvleteren", "Sierra Nevada",
									"Guinness", "Corona", "Calsberg"],
								index = Math.floor((Math.random()*10)+1)

							// Give random drink
							chunk = drinks[index]

							// transform selection and set the cursor into chunked text
							e.replaceSelection(chunk)
							cursor = selected.start

							// Set the cursor
							e.setSelection(cursor,cursor+chunk.length)
						}
					}]
				}]
			]
		});

});



