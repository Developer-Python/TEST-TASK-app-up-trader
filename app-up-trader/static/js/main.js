jQuery(document).ready(function( $ ) {

	// Variables
	var url = window.location.pathname;
	var len_category = $('.sub-category').length
	var len_links = document.getElementsByClassName('url_on_category').length
	var len_menu = $('.menu').length

	// Recount class for dynamic numbers of category	
	$('div.accordion').each(function(i,elem) {
		$(elem).addClass('menu'+i);
	}); 

	for (let m = 0; m <= len_menu; m++) {

		$('div.menu'+m+' .collapse').each(function(i,elem) {
			$(elem).addClass('collapse'+i);
		});

		$('div.menu'+m+' .btn').each(function(i,elem) {
			$(elem).addClass('btn'+i);
		});

		$('div.menu'+m+' .url_on_category').each(function(i,elem) {
			$(elem).addClass('url_on_category'+i);
		});
		
	}
	
	// Activation of a link clicked in the past
	for (let m = 0; m <= len_menu; m++) {
		for (var i = 0; i < len_links; i++) {
			if ($("div.menu"+m+" .collapse"+i+" .url_on_category"+i).attr('href') == url) {
				$("div.menu"+m+" .collapse"+(i)).addClass('in show')
			}
			
		};
	}

	// Logic behaviors of elements
	for (let m = 0; m <= len_menu; m++) {
		
		for (let i = 0; i <= len_category; i++) {
			
			// Click on this button
			$("div.menu"+m+" .btn"+i).click(function(){
				
				if ($("div.menu"+m+" .collapse"+i).hasClass('in show')) { 
					
					for (let c = 0; c < len_category; c++) {
						$("div.menu"+m+" .collapse"+(i+c)).removeClass('in show')
					}
				} else {
					
					for (let c = 0; c < len_category; c++) {
						$("div.menu"+m+" .collapse"+(i-c)).addClass('in show')
					}
				}

			})
			
		
		}
		
	}
	
	




});















































// len_category = $('.sub-category').length


// for (let i = 0; i < len_category; i++) { 

	
// 	$(".btn"+i ).click(function(){
		
// 		for (let c = 0; c <= i; c++) {

// 			if (i <= c) {
				
// 				$('#collapse'+c).removeClass('in show')
				
// 				if (i == (len_category-2)) {

// 					$('#collapse'+(len_category-1)).removeClass('in show')
// 				}
				
// 				if (i+1 == len_category) {
					
// 					$('#collapse'+c).toggleClass('in show')
// 				}

// 			} else if (i >= c) {
// 				$('#collapse'+c).addClass('in show')
				
// 			}
// 		}

// 	});


//   }