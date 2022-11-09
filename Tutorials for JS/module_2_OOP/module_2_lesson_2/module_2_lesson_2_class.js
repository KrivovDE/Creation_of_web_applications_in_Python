"use strict";

// class Book {
//          constructor() {
//                    console.log("создание объекта book");
//          }
// }
//
// let book1 = new Book();
//////////////////////////////////////////////////////////
// class Book {
//          constructor(title, author, price) {
//                    this.title = title;
//                    this.author = author;
//                    this.price = price;
//          }
//          // getTitle() { return this.title; }
//          // setPrice(pr) { this.price = pr; }
// }
//
// let book1 = new Book("Муму", "Тургенев", 112);
// console.log(book1);
// // console.log(book1.getTitle());
//////////////////////////////////////////////////////////
//
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
//////////////////////////////////////////////////////////
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
// class Book {
//          pages = 123;
//
//          constructor(title, author, price) {
//                    this.title = title;
//                    this.author = author;
//                    this.price = price;
//          };
// }
//
// let book1 = new Book("Муму", "Тургенев", 112);
// console.log(book1);












