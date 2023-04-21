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