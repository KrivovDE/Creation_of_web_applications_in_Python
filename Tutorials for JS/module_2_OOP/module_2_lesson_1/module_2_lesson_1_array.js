'use strict';

let ar1 = [];  //пустой массив
let ar2 = [1, 30, 0, -2]; //одномерный массив чисел
let ar3 = ["Яблоко", "Апельсин", "Слива"];

// console.log( ar2[0] );
// console.log( ar3[0] );

// ar2[1] = 'Груша';
ar3[3] = 'Лимон';
// console.log( ar3[3] );

//
// for(let i=0;i < ar3.length;++i)
//     console.log( ar3[i] );

// // Но можно это сделать и так:
// console.log( ar3 );

//
// let ar = [ 'Яблоко', { name: 'Джон' }, true,
//             function() { alert('привет'); } ];
//
// console.log( ar[1].name );
//
// let digits = [];
// digits[99999] = 1;
// console.log(digits)

// let fruits = ["Яблоко", "Апельсин", "Груша"];
// for(let i=0;i < fruits.length; ++i)
//     console.log( fruits[i] );
// console.log('------------------------------')
// for(let i of fruits)
//     console.log(i);

// let price = [2, 4, 6, 8, 10];
// for(let i = 0; i < price.length; ++i)
//     console.log(price[i] = price[i]**2);


// Методы push/pop, shift/unshift и многомерные массивы
//
// let ar = [ "Яблоко", "Слива" ];
//
//
// // ar[2] = "Груша";
//
// ar.push("Груша");
//
// ar.pop()
//
// ar.shift()
//
// for(let i of ar)
//     console.log(i);
// Метод shift удаляет первый элемент массива:
// метод unshift добавляет элемент в начало массива:



// Многомерные массивы
//
// let matrix = [
//   [1, 2, 3],
//   [4, 5, 6],
//   [7, 8, 9]
// ];
//
// // console.log( matrix );
// // console.log( matrix[2][1] );
//
// for(let row of matrix) {
//     let cols = "";
//     for(let val of row)
//        cols += val;
//
//     console.log(cols);
// }
let a = [600]
console.log(a.reverse())
