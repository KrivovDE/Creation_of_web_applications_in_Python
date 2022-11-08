'use strict';
// let str1 = "Hello World!";
// let str2 = 'Hello World!';
// let str3 = `Hello World!`;
//
// let name = `Java`, age = 18;
// let str = `Меня зовут ${name}, мне ${age} лет`;
// let strq = "Меня зовут " + name;
// console.log( strq );

//
// •	\n – спецсимвол перевода на новую строку;
// •	\r – возврат каретки (используется в ОС Windows совместно с символом \n);
// •	\t – спецсимвол табуляции;
// •	\uXXXX – символ в кодировке UTF-16;
// •	\" и \' – символы кавычек (внутри строки);
// •	\\ - символ обратного слеша.
//
// let str = 'Hello!\nI\'m Javascript.\nВот мой символ \t табуляции, обратный слеш \\ и символ \u00A9 копирайта';
// //
// console.log( str );


// let str = 'Hello!\nI\'m Javascript.';


// // console.log( str.length );
// let ch1 = str[0];
// let ch2 = str[7];
// console.log(ch1, ch2);
// console.log(typeof ch1);

// let str = 'HelLo!';
// let low = str.toLowerCase();
//
// let hi = "string".toUpperCase();
// console.log(low, hi);

// let str = "   string   "; //убирает пробелы в начале и конце строки
// console.log( str.trim() );

// let str = "-/-";
// console.log( str.repeat(5) ); //для повторения строки n раз:


// Set
// Коллекция Set формируется из уникальных данных (без ключей – только данные).
// Уникальность означает, что одно и то же значение не может быть добавлено дважды – оно просто проигнорируется.
//
// Данный объект имеет следующие методы и свойства:
//
// new Set(iterable) – создаёт Set, если в качестве аргумента был предоставлен итерируемый объект (обычно это массив), то копирует его значения в Set;
// set.add(value) – добавляет значение (если оно уже есть, то ничего не происходит), возвращает тот же объект set;
// set.delete(value) – удаляет значение, возвращает true если value было найдено и удалено, иначе false;
// set.has(value) – возвращает true, если значение присутствует в коллекции, иначе false;
// set.clear() – удаляет все значения из набора;
// set.size – возвращает количество элементов в наборе.

// let guests = new Set();
//
// let alex = { name: "Alexey", old: 25 };
// let oleg = { name: "Oleg", old: 32 };
// var masha = { name: "Masha", old: 18 };
// var masha = { name: "Masha", old: 19 };
//
// guests.add(alex);
// guests.add(oleg);
// guests.add(masha);
// guests.add(alex);
// guests.add(masha);

// // Выведем в консоль получившийся набор:
//
let a = [1,1,2,2,3,3,4,4,5,5,6,6,6,6,6,6,]
let guests = new Set(a);

for (let guest of guests) {
    console.log(guests);
}




















