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