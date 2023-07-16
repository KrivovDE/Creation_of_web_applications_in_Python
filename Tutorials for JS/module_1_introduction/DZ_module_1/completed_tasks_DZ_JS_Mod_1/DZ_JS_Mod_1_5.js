'use strict';

// * Во всех заданиях обязательно использовать рекурсию.

// 1. Написать функцию возведения числа в степень.

// function exponent(n) {
//     if (n===0) return 1;
//     return num*exponent(n-1);
// }
// let num = +prompt('Enter number');
// let n = +prompt('Enter exponent degree');
// let res = exponent(n);
// console.log(res);

// 2. Написать функцию поиска наибольшего общего делителя.

// function nod(num1, num2) {
//     if (num2 === 0) return num1;
//     return nod(num2, num1 % num2);
// }
// let num1 = +prompt('Enter number 1');
// let num2 = +prompt('Enter number 2');
// let res = nod(num1, num2);
// console.log(res);

// 3. Написать функцию для поиска максимальной цифры в числе.

// function maxNumberSearch(num) {
//     if (num===0) return max;
//     if (num % 10 > max) max = num % 10;
//     return maxNumberSearch(Math.floor(num/10));
// }
// let max=0;
// let num = +prompt('Enter number');
// let res = maxNumberSearch(num);
// console.log(res);

// 4. Написать функцию, которая определяет простое ли пере-
// данное число.

// function primeNumber(num,del) {
//     if (del===1) return 'YES';
//     if (num % del===0) return 'NO';
//     return primeNumber(num,del-1)
// }
// let num = +prompt('Enter number');
// let del = num-1;
// console.log(primeNumber(num,del));

// 5. Написать функцию для вывода всех множителей передан-
// ного числа в возрастающем порядке.
// Например: число 18 – множители 2 * 3 * 3.

// function primeNumber(num,del) {
//     if (del===1) return true;
//     if (num % del===0) return false;
//     return primeNumber(num,del-1)
// }
// function multipliers(num) {
//     if (num<=2) return 'This is prime number';
//     if (primeNumber(num,num-1)) return 'This is prime number';
//     let arr = [];
//     for (let i=2; i<=num; ) {
//         if (num % i===0 && primeNumber(i, i-1)) {
//             arr.push(i);
//             num = num/i;
//             i=2;
//         }
//         else i++
//     }
//     let res = arr[0];
//     for(let j = 1; j<arr.length; j++){
//         res += ' * ' + arr[j];
//     }
//     return res;
// }
// let num = +prompt('Enter number');
// console.log(multipliers(num));

// 6. Написать функцию, которая возвращает число Фибоначчи
// по переданному порядковому номеру.
// Числа Фибоначчи: 1, 1, 2, 3, 5, 8, 13… Ряд основывается на
// том, что каждое число равно сумме двух предыдущих чисел.
// Например: порядковый номер 3 – число 2, порядковый
// номер 6 – число 8.

// function fibonacci(n) {
//     if (n<3) return 1;
//     return fibonacci(n-1) + fibonacci(n-2);
// }
// let n = +prompt('Enter row serial number');
// console.log(fibonacci(n));
