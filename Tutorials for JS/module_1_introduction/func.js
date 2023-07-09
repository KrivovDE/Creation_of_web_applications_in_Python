






// function out_log(msg) {
//     console.log(msg);
// }
// out_log('1 вызов');
// out_log(5)
// //
// function showMessage(from, text) {
//          let msg = from + ":" + text;
//          console.log(msg);
// }
// showMessage("Аня", "Привет!");
// showMessage("Аня", "Как дела?");
//
// function abs(x) {
//          if(x < 0) x = -x;
//          return x;
// }
// let res = abs(-8);
// console.log(res);

//Function Expression, анонимные и callback-функции

// let showMsg = function() {
//          console.log("Hello!");
// };
//
// showMsg();



//
// function agreeCookies(question, yes, no) {
//   if (confirm(question)) yes();
//   else no();
// }
// //
// function agreeYes() {
//    console.log("Вы приняли соглашение о cookies");
// }
//
// function agreeNo() {
//    console.log("Вы отказались от использования cookies");
// }
//
// agreeCookies ("Наш сайт использует cookies. Нам нужно ваше согласие", agreeYes, agreeNo);
//

// анoнимный вариант
//
// function agreeCookies(question, yes, no) {
//   if (confirm(question)) yes();
//   else no();
// }
//
// agreeCookies(
//     "Наш сайт использует cookies. Нам нужно ваше согласие",
//     function () { console.log("Вы приняли соглашение о cookies");},
//     function () { console.log("Вы отказались от использования cookies");})



// function cube(x) {return x*x*x;}
//
// let CuB = cube(3)
// console.log(CuB)



// область видимости

//
// let x = 99090
// function logX(){
//      console.log(x);
//  }
//
//  logX()
//
// if (true) {
//   var test = true; // используем var вместо let
// }
//
// alert(test); // true, переменная существует вне блока if
//
//
// // А если бы мы использовали let test вместо var test,
// // тогда переменная была бы видна только внутри if:
//
//
// if (true) {
//   let test = true; // используем let
// }
//
// alert(test); // Error: test is not defined

// Рекурсия
//
// 1! = 1
// 2! = 2 * 1 = 2
// 3! = 3 * 2 * 1 = 6
// 4! = 4 * 3 * 2 * 1 = 24
// 5! = 5 * 4 * 3 * 2 * 1 = 120


// n! = n * (n - 1) * (n - 2) * ...*1


// function factorial(n) {
//   return (n != 1) ? n * factorial(n - 1) : 1;
// }
//
// alert( factorial(120) ); // 120
