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