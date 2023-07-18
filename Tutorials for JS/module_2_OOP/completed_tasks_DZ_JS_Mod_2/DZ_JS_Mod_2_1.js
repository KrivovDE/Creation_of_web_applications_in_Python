'use strict';

// Задание 1
// Создать объект, описывающий автомобиль (производитель,
// модель, год выпуска, средняя скорость), и следующие функции
// для работы с этим объектом.
// 1. Функция для вывода на экран информации об автомобиле.
// 2. Функция для подсчета необходимого времени для пре-
// одоления переданного расстояния со средней скоростью.
// Учтите, что через каждые 4 часа дороги водителю необхо-
// димо делать перерыв на 1 час.

// let auto = {                    //создаем объект машина
//     brand: 'Lada',
//     model: 'Kalina',
//     yearOfManufacture: 2010,
//     averageSpeed: 60
// };
// for (let propertyCar in auto) {     //выводим свойства машины на консоль циклом for in
//     console.log(propertyCar);
//     console.log(auto[propertyCar]);
// }
// function tripTime(km) {               //считаем время в пути
//     let t=0;
//     t = km/auto.averageSpeed;
//     if (t>4) t = t+Math.floor(t / 4);   //учитываем остановки каждые 4 часа
//     return t;
// }
// let km = +prompt('Enter distance');
// console.log(tripTime(km).toFixed(2) + ' hours'); //выводим результат функции

// Задание 2
// Создать объект, хранящий в себе отдельно числитель и знаменатель дроби,
// и следующие функции для работы с этим объектом.
// 1. Функция сложения 2-х объектов-дробей.
// 2. Функция вычитания 2-х объектов-дробей.
// 3. Функция умножения 2-х объектов-дробей.
// 4. Функция деления 2-х объектов-дробей.
// 5. Функция сокращения объекта-дроби.

// let fraction1 = {
//     numerator: 1,
//     denominator: 1
// };
// let fraction2 = {
//     numerator: 1,
//     denominator: 1
// };
// let num1 = fraction1.numerator = +prompt('Enter numerator for 1st fraction');
// let den1 = fraction1.denominator = +prompt('Enter denominator for 1st fraction');
// let num2 = fraction2.numerator = +prompt('Enter numerator for 2st fraction');
// let den2 = fraction2.denominator = +prompt('Enter denominator for 2st fraction');
// let resNum=1;
// let resDen=1;
// function fractionAddition() { //1.функция сложения
//     if (den1===den2) {
//         resNum=num1+num2;
//         resDen=den1;
//     }
//     else resDen=den1*den2; resNum=num1*den2+num2*den1;
//     return [resNum, resDen];
// }
// function fractionSubtraction() {  //2.функция вычитания
//     if (den1===den2) {
//     resNum=num1-num2;
//     resDen=den1;
//     }
//     else resDen=den1*den2; resNum=num1*den2-num2*den1;
//     return [resNum, resDen];
// }
// function fractionMultiply() {  //3.функция умножения
//     resNum=num1*num2;
//     resDen=den1*den2;
//     return [resNum, resDen];
// }
// function fractionDivision() {   //4.функция деления
//     resNum=num1*den2;
//     resDen=num2*den1;
//     return [resNum, resDen];
// }
// function nod(n1, n2) {              //5.Сокращение дроби
//     if (n2 === 0) return n1;        //Используем рекурсивную функцию из прошлого ДЗ для поиска
//     return nod(n2, n1 % n2);    //наибольшего общего делителя (НОД) числителя и знаменателя
// }
// function fractionReduction(num,den) { //сокращаем дроби
//     if (nod(num, den)===1) return 'fraction ' + num + '/' + den + ' is not reduced'; //дробь не сокращается
//     else return num/nod(num,den) + '/' + den/nod(num,den);           //делим числитель и знаменатель на НОД
// }
// let resAdd = num1 + '/' + den1 + ' + ' + num2 + '/' + den2 + " = "; //выводим результаты на экран
// console.log(resAdd + fractionAddition()[0] + '/' + fractionAddition()[1]);
// let resSub = num1 + '/' + den1 + ' - ' + num2 + '/' + den2 + " = ";
// if (fractionSubtraction()[0]<0) console.log(resSub + fractionSubtraction()[0]*(-1) + '/' + fractionSubtraction()[1]);
// else console.log(resSub + fractionSubtraction()[0] + '/' + fractionSubtraction()[1]);
// let resMul = num1 + '/' + den1 + ' * ' + num2 + '/' + den2 + " = ";
// console.log(resMul + fractionMultiply()[0] + '/' + fractionMultiply()[1]);
// let resDiv = num1 + '/' + den1 + " : " + num2 + '/' + den2 + " = ";
// console.log(resDiv + fractionDivision()[0] + '/' + fractionDivision()[1]);
// console.log(num1 + '/' + den1 + ' = ' + fractionReduction(num1,den1));
// console.log(num2 + '/' + den2 + ' = ' + fractionReduction(num2,den2));


// Задание 3
// Создать объект, описывающий время (часы, минуты, секун-
// ды), и следующие функции для работы с этим объектом.
// 1. Функция вывода времени на экран.
// 2. Функция изменения времени на переданное количество
// секунд.
// 3. Функция изменения времени на переданное количество
// минут.
// 4. Функция изменения времени на переданное количество
// часов.
// Учтите, что в последних 3-х функциях, при изменении одной
// части времени, может измениться и другая. Например: если ко
// времени «20:30:45» добавить 30 секунд, то должно получиться
// «20:31:15», а не «20:30:75».

// let clock = {                      //создаем объект со встроенными методами
//     hours: 0,
//     minutes: 0,
//     seconds: 0,
//     watchClock(h=this.hours, m=this.minutes, s=this.seconds) {   //показываем введенное время
//         if (s>=60) {m += Math.floor(s/60); s = s % 60}
//         if (m>=60) {h += Math.floor(m/60); m = m % 60}
//         if (s<10) s = '0' + s;
//         if (m<10) m = '0' + m;
//         if (h<10) h = '0' + h;
//         console.log(h + ':' + m + ':' + s);
//     },                                                                            //прибавляем часы, минуты, секунды
//     plusSeconds(h=this.hours, m=this.minutes, s=this.seconds) {
//         this.watchClock(h=this.hours, m=this.minutes, s=this.seconds + deltaSec)
//     },
//     plusMinutes(h=this.hours, m=this.minutes, s=this.seconds) {
//         this.watchClock(h=this.hours, m=this.minutes + deltaMin, s=this.seconds)
//     },
//     plusHours(h=this.hours, m=this.minutes, s=this.seconds) {
//         this.watchClock(h=this.hours + deltaHou, m=this.minutes, s=this.seconds)
//     }
// }
// clock.hours = +prompt('Enter hours');
// clock.minutes = +prompt('Enter minutes');
// clock.seconds = +prompt('Enter seconds');
// clock.watchClock();                                               //обращаемся к методам из объекта
// let deltaSec = +prompt('Enter difference in seconds');
// clock.plusSeconds();
// let deltaMin = +prompt('Enter difference in minutes');
// clock.plusMinutes();
// let deltaHou = +prompt('Enter difference in hours')
// clock.plusHours();
