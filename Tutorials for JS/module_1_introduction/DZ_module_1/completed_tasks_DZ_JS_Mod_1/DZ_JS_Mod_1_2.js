'use strict';
//Запросить у пользователя его возраст и определить, кем он
//является: ребенком (0–2), подростком (12–18), взрослым
//(18_60) или пенсионером (60– ...).
//
// let men = '';
// let x = +prompt('User age');
// if (x < 60 && x >= 18)
//    men = 'adult';
// else {
//    if (x >=0 && x < 12)
//    men = 'child';
//    else {
//        if (x >= 12 && x < 18)
//        men = 'teen';
//        else men = 'pensioner';
//    }
// }
// alert(men);

//Запросить у пользователя число от 0 до 9 и вывести ему
//спецсимвол, который расположен на этой клавише (1–!,
//2–@, 3–# и т. д).

// let x = +prompt('number 0-9');
// switch (x) {
//    case 0: x = ')';
//        break;
//    case 1: x = '!';
//        break;
//    case 2: x = '@';
//        break;
//    case 3: x = '#';
//        break;
//    case 4: x = '$';
//        break;
//    case 5: x = '%';
//        break;
//    case 6: x = '^';
//        break;
//    case 7: x = '&';
//        break;
//    case 8: x = '*';
//        break;
//    case 9: x = '(';
//        break;
//    default: x = 'enter number from 0 to 9';
// }
// alert(x);

//Запросить у пользователя трехзначное и число и проверить,
//есть ли в нем одинаковые цифры.
//
// var y = +prompt('Enter three-digit number');
// if ((y - y%100)/100 === (y%100 - y%10)/10)
//    alert('yes');
// else {
//    if ((y%100 - y%10)/10 === y%10)
//    alert('yes');
//    else {if ((y - y%100)/100 === y%10)
//    alert('yes')
//        else alert('no')
//        }
//    }

//4. Запросить у пользователя год и проверить, високосный он
//или нет. Високосный год либо кратен 400, либо кратен 4 и
//при этом не кратен 100.

// var y = +prompt('Enter year');
// if (y % 400 == 0) alert('yes');
// else {
//    if (y % 4 == 0 && y % 100 != 0) alert('yes');
//    else alert('no');
//    }

//5. Запросить у пользователя пятиразрядное число и опреде-
//лить, является ли оно палиндромом.

// var x = +prompt('Enter 5-digital number');
// if (Math.floor(x / 10000) === x % 10 && Math.floor((x % 10000)/ 1000) === Math.floor((x % 100)/ 10)) alert('yes');
// else alert('no');

//6. Написать конвертор валют. Пользователь вводит количе-
//ство USD, выбирает, в какую валюту хочет перевести: EUR,
//UAN или AZN, и получает в ответ соответствующую сумму.
//
// var moneyIn = +prompt("Enter dollar's sum");
// var moneyOut = prompt('Enter currency: EUR, UAN or AZN');
// const eur = 0.9;
// const uan = 5;
// const azn = 10;
// switch (moneyOut) {
//    case 'EUR': alert('total: ' + (moneyIn * eur));
//        break;
//    case 'UAN': alert('total: ' + (moneyIn * uan));
//        break;
//    case 'AZN': alert('total: ' + (moneyIn * azn));
//        break;
//    default: alert('check enter of currency');
//    }

//7. Запросить у пользователя сумму покупки и вывести сумму
//к оплате со скидкой: от 200 до 300 – скидка будет 3%, от 300
//до 500 – 5%, от 500 и выше – 7%.

//var pay = +prompt('Enter sum of pay');
//if (pay >=200  &&  pay < 300) pay *= 0.97;
//else {
//    if (pay >= 300  &&  pay < 500) pay *= 0.95;
//    else {
//        if (pay >= 500) pay *= 0.93;
//        }
//    }
//alert(pay.toFixed(2));

//8. Запросить у пользователя длину окружности и периметр
//квадрата. Определить, может ли такая окружность поме-
//ститься в указанный квадрат.

//var len = +prompt('Enter length of circle');
//var per = +prompt('Enter square perimetr');
//var res;
//res = ((per / 4) > (len / 3.14)) ? 'yes' : 'no';
//alert(res);

//9. Задать пользователю 3 вопроса, в каждом вопросе по 3 ва-
//рианта ответа. За каждый правильный ответ начисляется 2
//балла. После вопросов выведите пользователю количество
//набранных баллов.

//var res = 0;
//var ques = prompt('Capital of Scotland is: 1.Glasgow 2.Edinburgh 3.Aberdeen ENTER NUMBER');
//if (ques == 2) res += 2;
//ques = prompt('First football world cup winner is: 1.Uruguay 2.Germany 3.Brazil ENTER NUMBER');
//if (ques == 1) res += 2;
//ques = prompt('Which mountain is higher: 1.Everest 2.Dzhomolungma 3.It is the same mountain ENTER NUMBER');
//if (ques == 3) res +=2;
//alert(res)

//10. Запросить дату (день, месяц, год) и вывести следующую
//за ней дату. Учтите возможность перехода на следующий
//месяц, год, а также високосный год.
//
// var d = +prompt('enter day of the month');
// var m = +prompt('enter month number');
// var y = +prompt('enter year');
// //проверяем високосность года
// let abnormalYEAR = '';
// if (y % 400 == 0) abnormalYEAR ='yes';
// else {
//    if (y % 4 == 0 && y % 100 != 0) abnormalYEAR ='yes';
//    else abnormalYEAR ='no';
//    }
// //перебираем крайние дни месяцев
// if (m == 12 && d == 31) d = 1, m = 1, y++;
// else {
//    if ((m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m ==10 || m == 12) && d == 31) m++, d = 1;
//    else {
//        if ((m == 4 || m == 6 || m == 9 || m == 11) && d == 30) m++, d = 1;
//        else {
//            if (abnormalYEAR != 'yes' && m == 2 && d == 28) m++, d = 1;
//            else {
//                if (abnormalYEAR == 'yes' && m == 2 && d == 29) m++, d = 1;
//                else d++;
//                }
//            }
//        }
//    }
// alert(d + '.' + m + '.' + y)
