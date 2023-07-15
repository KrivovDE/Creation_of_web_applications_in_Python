'use strict';
//
// let book = {
//     title: "Три мушкитера",
//     author: "АЛ Дюма",
//     nPages: 0,
//     price: 12
// };
//
// console.log(book)
// //
// console.log(book.title);
// console.log(book.price);
//
// book.isSelled = false;
// //
// delete book.nPages;
// // console.log(book)
// console.log("nPages" in book);
// // if(book.nPages === undefined) console.log("nPages не существует");


// let book = {};
// let book = new Object();
// //
//
// let book = {
//     title: "название",
//     author: "автор",
//     nPages: 0,
//     "size book": {height: 100, width: 20}
// };
//
// book["size book"] = {height: 100, width: 50};
// // console.log(book["size book"]);
//
// // delete book["size book"];
//
// let keyName = "size book";
// console.log(book[keyName]);

// практическое применение

// let keyName = prompt("Что вы хотите узнать о книге?", "title");
// console.log(book[keyName]);


// let newKey = "color";
//
// let car = {
//     model: "toyota",
//     [newKey]: "black",
// };
//
// console.log(car[newKey]);

// // пример создания объекта внутри функции:
// //
// function createCar(model, color) {
//     return {
//        model: model,
//        color: color
//     };
// }
// let car = createCar("toyota", "black");
//
// console.log(car.color);

// // упрощенный синтаксис:
// function createCar(model, color) {
//     return {
//        model, //то же самое, что и model:model
//        color //то же самое, что и color:color
//     };
// }
// console.log(car.color);
// let book = {
//     title: "Муму",
//     author: "Тургенев",
//     price: 100,
//     nPages: 282
// };
// //
// // for(let key in book) {
// //     console.log(key+": "+book[key]);
// // }
//
// let lib = book
