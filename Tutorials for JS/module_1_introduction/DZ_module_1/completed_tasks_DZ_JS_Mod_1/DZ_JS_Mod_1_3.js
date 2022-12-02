'use strict';
//1. Подсчитать сумму всех чисел в заданном пользователем
//диапазоне.

// var i = +prompt('enter first number');
// var max = +prompt('enter last number');
// let res = 0;
// while (i <= max) {
// res += i;
// i++
// }
// console.log(res);

//2. Запросить 2 числа и найти только наибольший общий
//делитель.

//var a = +prompt('enter first number');
//var b = +prompt('enter second number');
//while (a != b) {
//if (a > b) a = a - b;
//else b = b - a;
//}
//console.log('NOD: ' + a);


//3. Запросить у пользователя число и вывести все делители
//этого числа.

//var a = +prompt('enter number');
//var res;
//var i;
//for (i = 1; i <= a; i++) {
//    res = a % i;
//    if (res == 0) console.log(i);
//    }

//4. Определить количество цифр в введенном числе.

// var num = +prompt('enter number');
// var i = 0;
// do {
//    i++;
//    num = num / 10;
//    }
// while (num >= 1)
// console.log(i);

//5. Запросить у пользователя 10 чисел и подсчитать, сколько
//он ввел положительных, отрицательных и нулей. При этом
//также посчитать, сколько четных и нечетных. Вывести
//статистику на экран. Учтите, что достаточно одной пере-
//менной (не 10) для ввода чисел пользователем.

// var i;
// var num;
// var pos = 0;
// var neg = 0;
// var even = 0;
// for (i = 1; i <= 10; i++) {
// num = +prompt('enter number');
// if (num > 0) pos++;
// if (num < 0) neg++;
// if (num % 2 == 0) even++;
// }
// console.log('Positive: ' + pos);
// console.log('Negative: ' + neg);
// console.log('Zero: ' + (10-pos-neg));
// console.log('Even: ' + even);
// console.log('Odd: ' + (10-even));

//6. Зациклить калькулятор. Запросить у пользователя 2 числа
//и знак, решить пример, вывести результат и спросить, хо-
//чет ли он решить еще один пример. И так до тех пор, пока
//пользователь не откажется.

//var num1 = 0;
//var num2 = 0;
//var act = '';
//var cont = 'Y';
//do {
//    num1 = +prompt('enter number 1');
//    act = prompt('enter action: + or - or * or /');
//    num2 = +prompt('enter number 2');
//    if (act == '+') num1 += num2;
//    if (act == '-') num1 -= num2;
//    if (act == '*') num1 *= num2;
//    if (act == '/') num1 /= num2;
//    console.log(num1);
//    cont = prompt('Do You want to continue?: Y - yes, N - no');
//}
//while (cont == 'Y')

//7. Запросить у пользователя число и на сколько цифр его
//сдвинуть. Сдвинуть цифры числа и вывести результат (если
//число 123456 сдвинуть на 2 цифры, то получится 345612).

//var num = +prompt('enter number');
//var shift = +prompt('enter shift');
//var dig = 0;
//var res = num;
//do { //считаем количество знаков
//    dig++;
//    res = res / 10;
//    }
//while (res >= 1)
//var i; //делаем сдвиг
//res = num;
//for (i = 1 ; i <= (dig - shift); i++) {
//    res = String(res % 10) + String(Math.floor(res / 10));
//    res = +res;
//    }
//console.log(res);

//8. Зациклить вывод дней недели таким образом: «День недели.
//Хотите увидеть следующий день?» и так до тех пор, пока
//пользователь нажимает OK.

// var con = true;
// var i = 1;
// var res = '';
// while (con === true) {
//    switch (i) {
//        case 1: res = 'Monday';
//            break;
//        case 2: res = 'Tuesday';
//            break;
//        case 3: res = 'Wednesday';
//            break;
//        case 4: res = 'Thursday';
//            break;
//        case 5: res = 'Friday';
//            break;
//        case 6: res = 'Saturday';
//            break;
//        case 7: res = 'Sunday';
//                i=0;
//                break;
//        }
//    con = confirm(res + '. Do You want to see next Day of Week?');
//    i++;
// }

//9. Вывести таблицу умножения для всех чисел от 2 до 9.
//Каждое число необходимо умножить на числа от 1 до 10.

// var num = 2;
// var i;
// var res;
// while (num <= 9) {
//    i = 1;
//    do {
//    res = num * i;
//    console.log(num + '*' + i + '=' + res);
//    i++;
//    }
//    while (i <= 10);
//    num++;
// }

//10. Игра «Угадай число». Предложить пользователю загадать
//число от 0 до 100 и отгадать его следующим способом:
//каждую итерацию цикла делите диапазон чисел пополам,
//записываете результат в N и спрашиваете у пользователя
//«Ваше число > N, < N или == N?». В зависимости от того
//что указал пользователь, уменьшаете диапазон. Начальный
//диапазон от 0 до 100, поделили пополам и получили 50.
//Если пользователь указал, что его число > 50, то изменили
//диапазон на от 51 до 100. И так до тех пор, пока пользова-
//тель не выберет == N.
//
// alert('Choose number from 0 to 100');
// var min = 0;
// var max = 100;
// var N;
// var res = '';
// while (res != '==N') {
//    N = Math.floor((max + min) / 2);
//    res = prompt('N = ' + N + ' Your number >N or <N or ==N ?');
//    if (res == '>N') min = N + 1;
//    if (res == '<N') max = N;
// }
// alert('Your number: ' + N);