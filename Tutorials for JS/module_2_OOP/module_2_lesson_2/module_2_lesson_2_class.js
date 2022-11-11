"use strict";
//
// class Book {
//          constructor() {
//                    console.log("создание объекта book");
//          }
// }
//
// let book1 = new Book();
// console.log(typeof book1)
// //////////////////////////////////////////////////////////
// class Book {
//          constructor(title, author, price) {
//                    this.title = title;
//                    this.author = author;
//                    this.price = price;
//          }
//          getTitle() { return this.title; }
//          setPrice(pr) { this.price = pr; }
// }
// //
// let book1 = new Book("Муму", "Тургенев", 112);
// let book2 = new Book("Отцы", "Глеб", 3);
// console.log(book1);
// console.log(book2);

// console.log(book1.getTitle());
//////////////////////////////////////////////////////////
// //
// function Book(title, author, price) {
//          this.title = title;
//          this.author = author;
//          this.price = price;
// }
//
// Book.prototype.getTitle = function() { return this.title; }
// Book.prototype.setPrice = function(pr) { this.price = pr; }

//////////////////////////////////////////////////////////
// // Class Expression
// let Book = class {
//          constructor(title, author, price) {
//                    this.title = title;
//                    this.author = author;
//                    this.price = price;
//          };
// }
//
// let Book = class BookClass {
//          constructor(title, author, price) {
//                    this.title = title;
//                    this.author = author;
//                    this.price = price;
//          };
// }
// //////////////////////////////////////////////////////////
// let Book = class {
//          constructor(title, author, price) {
//                    this.title = title;
//                    this.author = author;
//                    this.price = price;
//          };
//          get titleBook() {return this.title; }
//          set titleBook(value) { this.title = value; }
// }
// let book1 = new Book("Муму", "Тургенев", 112);
//
// console.log(book1.titleBook) //расширить геттеры на все поля
//////////////////////////////////////////////////////////
class Book {
         pages = 123;

         constructor(title, author, price) {
                   this.title = title;
                   this.author = author;
                   this.price = price;
         };


}

let book1 = new Book("Муму", "Тургенев", 112);
console.log(book1.mhghjg);
console.log(book1.S);
//////////////////////////////////////////////////////////

// Давайте рассмотрим еще один пример создания
// класса Rectangle, который будет находить площади и периметр
// прямоугольника, для которого известны его ширина и высота.
//
// Создадим два экземпляра класса Rectangle и выведем
// в консоль данные, возвращаемые методами
// square() и perimeter().

// class Rectangle {
//                 constructor(width, height){
//                     this.width = width;
//                     this.height = height;
//                 }
//                 square() {
//                     return this.width * this.height;
//                 }
//                 perimeter(){
//                     return 2 * (this.width + this.height);
//                 }
// }
//
// let rect1 = new Rectangle(20, 30);
// console.log(rect1.square(), rect1.perimeter());
//
//
// let rect2 = new Rectangle(78, 92);
// console.log(rect2.square(), rect2.perimeter());








