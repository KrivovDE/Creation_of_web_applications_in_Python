//hamburger
$('#menu__toggle-start').click(function () {
    if ($(this).is(':checked')) {
        $('.block-main__menu').css({'display': 'flex'})
    } else {
        $('.block-main__menu').css({'display': 'none'})
    }
})