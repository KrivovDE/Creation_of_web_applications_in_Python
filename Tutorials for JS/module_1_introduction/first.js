'use strict';

// alert('Академия ШАГ')

// let age = prompt('Возраст', 18);
// console.log(age)

// let is_car = confirm('Продолжить?');
// console.log(is_car)

// let z = '5',
//     v = 7;
//  console.log(typeof (z+v))
//  console.log(+z + +v)

// console.log(4**(1/2))

// let x = -5;
//
// if (x < 0)
//    console.log('отрицательное');
// else
//     if (x > 0)
//         console.log('положительное');
//     else
//         console.log('ноль');

// В ряде случаев конструкцию if else удобнее записывать через тернарный условный оператор,
// который имеет такой синтаксис:
// let result = условие ? значение1 : значение2;

// let age = 19;
// let access = (age > 18) ? true : false;  // можно упростить до let access = age > 18;
// console.log(access);


// //[Проверяем находится ли t в диапазоне от 2-7] (и-&& или-|| не-!)

// let t = 8;
//
// if(t >= 2 && t <= 7) console.log('попали');
// else console.log('промах');

// используется, когда из множества возможных вариантов нужно выбрать
// какой-то один.
// В круглых скобках оператора switch записывается переменная,
//     которая сравнивается со значениями (константами), указанными в case.
//     Далее, через двоеточие пишутся операторы, которые выполняются при
//     совпадении значения переменной с константой.

// let item = 3;
// switch (item) {
//     case 1: console.log('значение = 1');break;
//     case 2: console.log('значение = 2');break;
//     case 3: console.log('значение = 3');break;
//     case 4: console.log('значение = 4');break;
//     default: console.log('иное значение');
// }


 // let x = +prompt("Input x=");
 //             var str = "";
 //             switch(x){
 //                 case 1:  str += "1";
 //                 case 2:  str += "2";
 //                 case 3:  str += "3";
 //                 case 4:  str += "4";
 //                default: str += "5";
 //             }
 //             alert(str);



// Операторы циклов for, while, do while


// Общий синтаксис оператора довольно прост:
//  while(condition)
//      statement;
// За ключевым словом «while» в круглых скобках указывается условное выражение,
// после скобок — инструкция для выполнения (тело цикла).

// let i = 1;
// while(i < 11)
//     {
// console.log(i);
// i++; //сломать
//     }



// Вторая разновидность условных циклов, — цикл с постусловием,
//     создается при помощи оператора «do while» по следующей схеме:
//  do statement
//  while(condition)


// const PSW = 'admin'
// let psw = null;
//
// do {
//     psw = prompt('Введите пароль', '');
// }
// while (psw != PSW);
// console.log('Вы вошли в систему');


 //    For
 //    Цикл-счетчик (или цикл со счетчиком) организуется при помощи оператора «for».
 //    Синтаксис оператора, кроме тела цикла, содержит три декларативных блока:
 // for (initialization; condition; expression)
 //    statement
 //
 //    Первый блок «initialization» используется для началь- ной инициализации цикловой переменной.
 //    Этот блок выполняется один раз перед началом цикла. Второй блок «condition» содержит условие,
 //    при котором цикл продол- жается. Обычно это условие содержит ограничение на цикловую переменную.
 //    Третий блок «expression» задает выражение для изменения цикловой переменной.
 //    Второй и третий блоки выполняются на каждой итерации цикла.
//
// let i = 0
// for(i; i<5; i++)
//      console.log(i);

// For in, for of

// let arr=[1,4, true,3,7,55,888,34,0, 'hello']
// for(let i in arr) console.log(i)
// for(let i of arr) console.log(i)



// Напишите скрипт, который запрашивает у пользователя число N и выводит все
// четные числа от 2 до N или N-1, если N нечетное.
// Например: ввод 10, вывод 2 4 6 8 10; ввод 7, вывод 2 4 6.


// a = int(input('ff'))
//
// for i in range(1, a+1):
//     if i % 2 == 0:
//         print(i)

// ≈
// let N = 10
//
// while(Z < N)
//
//     { if (Z % 2 === 0) console.log(Z);
//       Z++;
//     }

// let Z = 1
// let userNumber = +prompt('Введите число')
//
// while(Z < userNumber)
//
//     { if (Z % 2 === 0) console.log(Z);
//       Z++;
//     }



// function out_log(msg) {
//     console.log(msg);
// }
// out_log('1 вызов');
// out_log( )
// //
// function showMessage(from, text) {
//          let msg = from + ": " + text;
//          console.log(msg);
// }
// showMessage("Аня", "Привет!");
// showMessage("Аня", "Как дела?");

// function abs(x) {
//          if(x < 0) x = -x;
//          return x;
// }
// let res = abs(-7);
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
//
// function agreeYes() {
//    console.log("Вы приняли соглашение о cookies");
// }
//
// function agreeNo() {
//    console.log("Вы отказались от использования cookies");
// }
//
// agreeCookies("Наш сайт использует cookies. Нам нужно ваше согласие", agreeYes, agreeNo);


//анoнимный вариант

// function agreeCookies(question, yes, no) {
//   if (confirm(question)) yes();
//   else no();
// }
// agreeCookies(
//     "Наш сайт использует cookies. Нам нужно ваше согласие",
//     function () { console.log("Вы приняли соглашение о cookies");},
//     function () { console.log("Вы отказались от использования cookies");})

















