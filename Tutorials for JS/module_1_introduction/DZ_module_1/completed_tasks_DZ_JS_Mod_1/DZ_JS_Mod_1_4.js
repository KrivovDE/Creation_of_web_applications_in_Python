'use strict';

//1. Написать функцию, которая принимает 2 числа и возвра-
//щает -1, если первое меньше, чем второе; 1 – если первое
//больше, чем второе; и 0 – если числа равны.

// function numReturn(x1, x2) {
// if (x1 > x2) return -1;
// if (x2 > x1) return 1;
// else return 0;
// }
// let x1 = +prompt('Enter first number');
// let x2 = +prompt('Enter second number');
// let res = numReturn(x1, x2);
// console.log(res);

//2. Написать функцию, которая вычисляет факториал пере-
//данного ей числа.

// function factorial(x) {
//     let res = 1;
//     for (let i=1; i<x; i++) {
//         res *= (i + 1);
//     }
//     return res;
// }
// let x = +prompt('Enter number (not so much!)');
// let fact = factorial(x);
// console.log(fact);

//3. Написать функцию, которая принимает три отдельные
//цифры и превращает их в одно число. Например: цифры
//1, 4, 9 превратятся в число 149.

// function numGen(a, b, c) {
// return a*100 + b*10 + c;
// }
// let a = +prompt('Enter first number');
// let b = +prompt('Enter second number <10');
// let c = +prompt('Enter third number <10');
// let res = numGen(a, b, c);
// console.log(res);

//4. Написать функцию, которая принимает длину и ширину
//прямоугольника и вычисляет его площадь. Если в функцию
//передали 1 параметр, то она вычисляет площадь квадрата.

// function area(a, b) {
//     if (a === 0) return b*b;
//     if (b === 0) return a*a;
//     else return a*b;
// }
// let a = +prompt('Enter first side');
// let b = +prompt('Enter second side');
// let res = area(a, b);
// console.log(res);

//5. Написать функцию, которая проверяет, является ли пере-
//данное ей число совершенным. Совершенное число – это
//число, равное сумме всех своих собственных делителей.

// function checkPerfect(n) {
//     let sum = 0;
//     for (let i=1; i<n; i++) {
//         if (n % i === 0) sum +=i;
//     }
//     if (sum === n) return 'YES';
//     else return 'NO';
// }
// let n = +prompt('enter number');
// let res = checkPerfect(n);
// console.log(res);

//6. Написать функцию, которая принимает минимальное и
//максимальное значения для диапазона, и выводит только
//те числа из диапазона, которые являются совершенными.
//Используйте написанную ранее функцию, чтобы узнавать,
//совершенное число или нет.

// function checkPerfect(n) {
//     let sum = 0;
//     for (let i=1; i<n; i++) {
//         if (n % i === 0) sum +=i;
//     }
//     if (sum === n) return 'YES';
//     else return 'NO';
// }
// function checkPerfectNum(min, max) {
//     let res ='';
//     for (let n=min; n<=max; n++) {
//         res = checkPerfect(n);
//         if (res === 'YES') console.log(n);
//     }
// }
// let min = +prompt('Enter minimum of range');
// let max = +prompt('Enter maximum of range');
// checkPerfectNum(min, max);

//7. Написать функцию, которая принимает время (часы, мину-
//ты, секунды) и выводит его на экран в формате «чч:мм:сс».
//Если при вызове функции минуты и/или секунды не были
//переданы, то выводить их как 00.

// function clock(h,m,s) {
//     if (s>=60) {m += Math.floor(s/60); s = s % 60}
//     if (m>=60) {h += Math.floor(m/60); m = m % 60}
//     if (s<10) s = '0' + s;
//     if (m<10) m = '0' + m;
//     if (h<10) h = '0' + h;
//     console.log(h + ':' + m + ':' + s);
// }
// let h = +prompt('Enter hours');
// let m = +prompt('Enter minutes');
// let s = +prompt('Enter seconds');
// clock(h,m,s);

//8. Написать функцию, которая принимает часы, минуты и
//секунды и возвращает это время в секундах.

// function secondsCount(h,m,s) {
//     return h*60*60 + m*60 + s;
// }
// let h = +prompt('Enter hours');
// let m = +prompt('Enter minutes');
// let s = +prompt('Enter seconds');
// let res = secondsCount(h,m,s);
// console.log(res + ' seconds');

//9. Написать функцию, которая принимает количество секунд,
//переводит их в часы, минуты и секунды и возвращает в
//виде строки «чч:мм:сс».

// function time(sec) {
//     let h = Math.floor(sec/3600);
//     let m = Math.floor((sec-h*3600)/60);
//     let s = sec - m*60 - h*3600;
//     if (s<10) s = '0' + s;
//     if (m<10) m = '0' + m;
//     if (h<10) h = '0' + h;
//     return '<<' + h + ':' + m + ':' + s + '>>'
// }
// let sec = +prompt('Enter seconds');
// let res = time(sec);
// console.log(res);

//10. Написать функцию, которая считает разницу между датами.
//Функция принимает 6 параметров, которые описывают 2
//даты, и возвращает результат в виде строки «чч:мм:сс». При
//выполнении задания используйте функции из предыду-
//щих 2-х заданий: сначала обе даты переведите в секунды,
//узнайте разницу в секундах, а потом разницу переведите
//обратно в «чч:мм:сс».

// function secondsCount(h,m,s) {
//     return h*60*60 + m*60 + s;
// }
// function secondsToTime(sec) {
//     let h = Math.floor(sec/3600);
//     let m = Math.floor((sec-h*3600)/60);
//     let s = sec - m*60 - h*3600;
//     if (s<10) s = '0' + s;
//     if (m<10) m = '0' + m;
//     if (h<10) h = '0' + h;
//     return '<<' + h + ':' + m + ':' + s + '>>'
// }
// function dataInterval(h1, m1, s1, h2, m2, s2) {
//     let res1 = secondsCount(h1, m1, s1);
//     let res2 = secondsCount(h2, m2, s2);
//     let res = res1 - res2;
//     if (res<0) res = res*(-1);
//     return secondsToTime(res);
// }
// let h1 = +prompt('Enter hours');
// let m1 = +prompt('Enter minutes');
// let s1 = +prompt('Enter seconds');
// let h2 = +prompt('Enter hours');
// let m2 = +prompt('Enter minutes');
// let s2 = +prompt('Enter seconds');
// let time = dataInterval(h1,m1,s1,h2,m2,s2);
// console.log(time);