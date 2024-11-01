"use strict";
//1. Запросите у пользователя его имя и выведите в ответ:
//«Привет, его имя!».

// name = 'Hello,' + prompt("What's your name?") + '!';
// alert(name);

//2. Запросите у пользователя год его рождения, посчитайте,
//сколько ему лет и выведите результат. Текущий год укажите
//в коде как константу.

// let birthYear = +prompt("In what year were you born?");
// const x = 2022;
// let age = x - birthYear;
// alert(age);

//3. Запросите у пользователя длину стороны квадрата и вы-
//ведите периметр такого квадрата.

// let a = +prompt("side of a square:");
// let per = 'Square perimetr: ' + (a * 4);
// alert(per);

//4. Запросите у пользователя радиус окружности и выведите
//площадь такой окружности.

//let radius = +prompt('Circle radius?');
//const pi = 3.14;
//let area = pi*(radius**2);
//alert('area of a circle: ' + area);

//5. Запросите у пользователя расстояние в км между двумя
//городами и за сколько часов он хочет добраться. Посчи-
//тайте скорость, с которой необходимо двигаться, чтобы
//успеть вовремя.

//var distance = +prompt('Distance between cities: km');
//var interval = +prompt('Time interval: hours');
//var speed = distance/interval;
//alert(speed + 'km/h');

//6. Реализуйте конвертор валют. Пользователь вводит долла-
//ры, программа переводит в евро. Курс валюты храните в
//константе.

// var dollar = +prompt('dollar amount');
// const rate = 1.07;
// dollar = dollar / rate;
// alert('Euro=' + dollar.toFixed(2));

//7. Пользователь указывает объем флешки в Гб. Программа
//должна посчитать сколько файлов размером в 820 Мб по-
//мещается на флешку.

//var vol = +prompt('Enter flash-volume in GB');
//vol = Math.floor(vol * 1000 / 820) + 'files';
//alert(vol);

//8. Пользователь вводит сумму денег в кошельке и цену одной
//шоколадки. Программа выводит сколько шоколадок может
//купить пользователь и сколько сдачи у него останется.

//var money = +prompt('How much money do You have?');
//var price = +prompt('Chocolate price');
//let res = Math.floor(money/price);
//money = 'money left:' + (money - res*price);
//res = res + 'bar of chocolate';
//alert(res);
//alert(money);

//9. Запросите у пользователя трехзначное число и выведите
//его задом наперед. Для решения задачи вам понадобится
//оператор % (остаток от деления).

// var x = +prompt('Enter three-digit number');
// alert(String((x%10)) + String(((x%100) - (x%10))/10) + String((x - (x%100))/100));

//10. Запросите у пользователя целое число и выведите в ответ,
//четное число или нет. В задании используйте логические
//операторы. В задании не надо использовать if или switch.

var x = +prompt("Enter whole number");
x = x % 2 == 0;
alert(x + "  *: true - chetnoe, false - nechetnoe");
