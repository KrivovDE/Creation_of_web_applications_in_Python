'use strict';

// Задание
// 1. Написать функцию, которая принимает строку и выводит
// статистику о ней: количество букв, количество цифр и
// количество других знаков.

// function statString() {
//     let str = prompt('Enter string','a2b4m5M^h@j35Lk*(g_');
//     const reg1 = /[a-z]/i;
//     const reg2 = /[0-9]/;
//     let letterSum = 0;
//     let digitSum = 0;
//     for (let i=0; i<str.length; i++) {
//         if (reg1.test(str.charAt(i))) {letterSum++; continue}
//         if (reg2.test(str.charAt(i))) digitSum++;
//     }
//     console.log('Letters is ' + letterSum + ' pcs');
//     console.log('Digits is '+ digitSum +' pcs');
//     console.log('Another symbol is '+ (str.length-letterSum-digitSum) +' pcs');
// }
// let f = 'ds'
// statString(f);

// 2. Написать функцию, которая принимает двузначное число
// и возвращает его в текстовом виде.
// Например: 35 – тридцать пять, 89 – восемьдесят девять,
// 12 – двенадцать.

// function numInText(num) {
//     let res='';
//     let arr1 = ['one', 'two', 'three', 'four', 'five','six','seven','eight', 'nine'];
//     let arr10 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty','seventy', 'eighty','ninety'];
//     let arr11 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen'];
//     if (num < 10 || num > 99) return('Enter TWO-digit number!')
//     if (num > 20 && num%10 !== 0) {res = arr10[Math.floor(num/10)-2] + ' ' + arr1[num%10-1]; return(res)}
//     if (num%10 === 0 && num !== 10) {res = arr10[num/10-2]; return(res)}
//     if (num > 10 && num <= 15) {res = arr11[(num%10) - 1]; return(res)}
//     if (num >= 16 && num <= 19) {res = arr1[num%10-1]+'teen'; return(res)}
//     else {res = 'ten'; return(res)}
// }
// let num = +prompt('Enter 2-digit number');
// console.log(numInText(num));

// 3. Написать функцию, которая заменяет в полученной строке
// большие буквы на маленькие, маленькие – на большие, а
// цифры – на знак нижнего подчеркивания.

// function caseString() {
//     let str = prompt('Enter string','hELLoW123wORlD');
//     const reg1 = /[a-z]/;
//     const reg2 = /[A-Z]/;
//     const reg3 = /[0-9]/;
//     let arr =[];
//     for (let i=0; i<str.length; i++) {
//         if (reg1.test(str[i])) {arr.push(str[i].toUpperCase()); continue}
//         if (reg2.test(str[i])) {arr.push(str[i].toLowerCase()); continue}
//         if (reg3.test(str[i])) arr.push('_');
//         else arr.push(str[i])   //если в строке еще какие-то знаки
//     }
//     console.log(str +' >>> '+ arr.join(''));
// }
// caseString();


// 4. Написать функцию, которая преобразует названия css-
// стилей с дефисом в название в СamelСase стиле: font-size
// в fontSize, background-color в backgroundColor, textalign
// в textAlign.

// function cssToLCC() {
//     let newStr ='';
//     for (let i=0; i<str.length; i++) {
//         if (str[i] === '-') {
//             newStr += str[i+1].toUpperCase();
//             i++;
//         }
//         else newStr += str[i];
//     }
//     console.log(newStr);
// }
// let str = prompt('Enter string');
// cssToLCC();

// 5. Написать функцию, которая принимает словосочетание
// и превращает его в аббревиатуру.
// Например: cascading style sheets в CSS, объектно-
// ориентированное программирование в ООП.

// function abbrFunc() {
//     let newStr = '';
//     for (let i=1; i<str.length; i++) {
//         if (str[i] === ' ') newStr += str[i+1].toUpperCase();
//     }
//     console.log(str[0].toUpperCase() + newStr);  //добавляем первую букву первого слова к аббревиатуре
// }
// let str = prompt('Enter phrase').trim();
// abbrFunc();

// 6. Написать функцию, которая принимает любое коли-
// чество строк, объединяет их в одну длинную строку и
// возвращает ее.

// function strConcat() {
//     let str = prompt('Enter string');
//     arrStr.push(str);
//     console.log(arrStr.join(' '));
//     if (confirm('Do You want to enter next phrase?')) return strConcat();
// }
// let arrStr = [];
// strConcat();

// 7. Написать функцию – калькулятор. Функция принимает
// строку с примером, определяет, какое действие необходимо
// выполнить (+ - * /), переводит операнды в числа, решает
// пример и возвращает результат.

// function calculator(str) {
//     const reg = /\d/;
//     let index=0;
//     for (let i=0; i<str.length; i++) {
//         if (!reg.test(str[i])) {index = i; break;}  //находим индекс знака арифметического действия
//     }
//     let num1 = Number(str.substring(0,index));  //разбиваем строку на числа 1 и 2
//     let num2 = Number(str.substring(index+1));
//     let res;
//     switch(str[index]) {
//         case '+': res = num1+num2;
//             break;
//         case '-': res = num1-num2;
//             break;
//         case '*': res = num1*num2;
//             break;
//         case '/': res = num1/num2;
//             break;
//         default: res = 'Enter operation correctly'
//     }
//     console.log(res);
// }
// let str = prompt('Enter operation', '42/14');
// calculator(str);

// 8. Написать функцию, которая получает url и выводит под-
// робную информацию о нем.
// Например: url “https://itstep.org/ua/about”, информация
// “протокол: https, домен: itstep.org, путь: /ua/about”.

// function urlInfo() {
//     let str = prompt('Enter url');
//     let newStr = '';
//     let index = str.indexOf('://');
//     newStr = str.substring(0, index);
//     console.log('protocol: ' + newStr);
//     newStr = str.substring(index+3, str.indexOf('/', index+3)); //выводим строку от :// до /
//     console.log('domain name: ' + newStr);
//     newStr = str.substring(str.indexOf('/', index+3));     // выводим строку от /, начиная поиск в строке позже ://
//     console.log('way: ' + newStr);
// }
// urlInfo();

// 9. Написать функцию, которая принимает строку и раздели-
// тель и возвращает массив подстрок, разбитых с помощью
// указанного разделителя.
// Например: строка “10/08/2020”, разделитель “/”, результат:
// “10”, “08”, “2020”.
// Выполняя задание, не используйте функцию split().

// function splitStr() {
//     let str = prompt('Enter string');
//     let sep = prompt('Enter separator');
//     let index = str.indexOf(sep);
//     let startSep = 0;
//     let arrStr = [str.substring(startSep,index)];
//     while (index !== -1) {
//         startSep = (index+sep).length;
//         index=str.indexOf(sep,index+1);
//         if (index !== -1) arrStr.push(str.substring(startSep,index)); //если число последнее, то продолжаем дополнять массив
//         else arrStr.push(str.substring(startSep));                    //иначе дополняем его до конца введенной строки
//     }
//     let res=arrStr.join(`", "`);
//     console.log(`"` + res + `"`);
// }
// splitStr();

// 10. Написать функцию вывода текста по заданному шаблону.
// Функция принимает первым параметром шаблон, в тексте
// которого может использоваться %, после символа % ука-
// зывается индекс входного параметра. При выводе вместо
// %индекс необходимо вывести значение соответствующего
// входного параметра.
// Например: print(“Today is %1 %2.%3.%4”, “Monday”, 10,
// 8, 2020) должна вывести “Today is Monday 10.8.2020”.

// function countParameter(sample) {             //функция для подсчета количества параметров
//     let index = sample.indexOf('%');
//     let counter = 0;
//     while (index !== -1) {
//         counter++;
//         index = sample.indexOf('%', index+1);
//     }
//     return (counter);
// }
// function strBySample2() {
//     let sample = prompt('Enter sample', '“Today is %1 %2.%3.%4”');
//     let re = /%\d+/;
//     let qPar = countParameter(sample);
//     for (let i =0; i<qPar; i++) {
//         let par = prompt('Enter next parameter', 'M');
//         sample = sample.replace(re, par);
//     }
//     console.log(sample);
// }
// strBySample2();