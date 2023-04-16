//карусель
$(document).ready(function () {
    $(".owl-carousel").owlCarousel({
        items: 1,
        stagePadding: 90,
        loop: true,
        nav: true,
        navText: [
            '<img src="./assets/img/svg/left.svg" alt="service" class="owl-carousel-back">',
            '<img src="./assets/img/svg/right.svg" alt="service" class="owl-carousel-next">'
        ],
        dots: true,
        dotsContainer: '.dots'

    });
    $('.owl-stage').css({'padding-left': '0'})
    new WOW().init();
});




