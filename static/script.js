let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
	menu.classList.toggle('bx-x');
	navbar.classList.toggle('open');
}

var swiper = new Swiper('.blog-slider', {
	spaceBetween: 30,
	effect: 'fade',
	loop: true,
	mousewheel: {
	  invert: false,
	},
	// autoHeight: true,
	pagination: {
	  el: '.blog-slider__pagination',
	  clickable: true,
	}
  });