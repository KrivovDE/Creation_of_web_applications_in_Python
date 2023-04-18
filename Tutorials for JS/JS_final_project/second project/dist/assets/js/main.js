/*-----------------------------ALL-------------------------------------*/
/*-------------------------------------------------------------------------------*/
//анимация для всех

$('.place__main-block:not(:eq(3))').click(function () {
    $(this).siblings('.place__choose').slideToggle()
})
$('.place__main-block:eq(3)').click(function () {
    $(this).siblings('.place__choose').slideDown()
})
$('.place__main-block').on('mouseenter', function () {
    if ($(this).siblings('.place__choose').css('display') === 'none') {
        $('.place__choose').slideUp()
    }
})
$('.place__choose').on('mouseleave', function () {
    $(this).slideUp()
})
// Каталог недвижимости
$('.menu__item.catalog').click(function () {
    $('.header__choose-container').fadeToggle().css({'display': 'flex'})
})
$('.header__choose-container').on('mouseleave', function () {
    $(this).slideUp()
})
//hamburger
$('#menu__toggle-start').click(function () {
    if ($(this).is(':checked')) {
        $('.block-main__menu').css({'display': 'flex'})
    } else {
        $('.block-main__menu').css({'display': 'none'})
    }
})
//районы живой поиск
let inputs = $('.main-block__click > input')
inputs.on('input', function () {
    let value = this.value.trim().toLowerCase()
    let list = document.querySelectorAll('.section__address-sublist li')
    if (value !== '') {
        list.forEach(elem => {
            if (elem.innerText.toLowerCase().search(value) === -1) {
                elem.classList.add('hide')
            } else {
                list.forEach(elem => {
                    elem.classList.remove('hide')
                })
            }
        })
    } else {
        document.querySelectorAll('.section__address-sublist-link').forEach(elem => {
            elem.classList.remove('hide')
        })
    }
})

$('.section__address-sublist-link').click(function (){
    inputs.val(this.innerText)
})

$('.carousel-info_button-lb').click(function (e){
    e.preventDefault()
    $(this).toggleClass('active')
})
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
/*-----------------------------PLACE-TYPE-------------------------------------*/
/*-------------------------------------------------------------------------------*/

//жилая коммерческая
$('.click-radio__type-radio > input').click(function () {
    if ($(this).is(':checked')) {
        $('.click-radio__type-radio').removeClass('active')
        $(this).parent().addClass('active')
    } else {
        $(this).parent().removeClass('active')
    }
})

/*-----------------------------PLACE-TYPE-------------------------------------*/
/*-------------------------------------------------------------------------------*/
/*-----------------------------PLACE-roominess-------------------------------------*/
/*-------------------------------------------------------------------------------*/

//чекбоксы в новостройке и комнатность
$('.click-ch-bx__type-ch-bx > input, .click-ch-bx__roominess-ch-bx > input').click(function () {
    if ($(this).is(':checked')) {
        $(this).parent().addClass('active')
        $(this).siblings('.click-ch-bx__svg').addClass('active')
    } else {
        $(this).parent().removeClass('active')
        $(this).siblings('.click-ch-bx__svg').removeClass('active')
    }
})

//комнатность количество
$('.click-radio__roominess-radio > input').click(function () {
    if ($(this).is(':checked')) {
        $('.click-radio__roominess-radio').removeClass('active')
        $(this).parent().addClass('active')
    } else {
        $(this).parent().removeClass('active')
    }
})