'use strict';
// setTimeout позволяет выполнять произвольную функцию через определенный период времени и останавливается,
// и setInterval. – многократно выполняет функцию через указанный интервал.

// function createMsg() {
//     let msg = "Hello";
//     console.log(msg);
// }
//
// // setTimeout(createMsg, 2000);
// ////////////////////////////////
// function createMsg(msg) {
//     console.log(msg);
// }
//
// setTimeout(createMsg, 2000, "timeout hello");
// ////////////////////////////////
// function downloadMsg() {
//     let idLoading = setTimeout(function() {
//          console.log("Идет загрузка данных...");
//     }, 500);
//
//     setTimeout(function() {
//          clearTimeout(idLoading); //останавливаем setTimeout после загрузки данных
//          console.log("Данные загружены");
//     }, 2000);     //задержка: имитация загрузки с сервера
// }
//
// downloadMsg();
// ////////////////////////////////

// function createClock(seconds) {
//     let sec = seconds;
//
//     return function() {
//          sec++;
//          console.log("Прошло " + sec + " секунд(а)");
//     }
// }
//
// let clock = createClock(0);
// setInterval(clock, 1000);
//
// // let idClock = setInterval(clock, 1000);
// // setTimeout(function() {
// //     clearInterval(idClock)
// // }, 10000);
// ////////////////////////////////

// alert(Math.PI);
// alert(Math.E);

// var res = Math.random();
// // псевдослучайное число
// alert(res);
// res = Math.random();
// // псевдослучайное число
// alert(res);

// // случайное значение от 0 до 9
// alert(Math.floor(Math.random()*10));
// // случайное значение от 0 до 11
// alert(Math.floor(Math.random()*11));
// // случайное значение от 1 до 10
// alert(Math.floor(Math.random()*10)+1);
// ////////////////////////////////


// const today = new Date();
// console.log(today);
//
// let date2 = new Date("05/26/1989");
// console.log(date2);





