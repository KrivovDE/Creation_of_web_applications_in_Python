// Каталог недвижимости
$('.menu__item.catalog').click(function () {
    $('.header__choose-container').fadeToggle().css({'display': 'flex'})
})
$('.header__choose-container').on('mouseleave', function () {
    $(this).slideUp()
})