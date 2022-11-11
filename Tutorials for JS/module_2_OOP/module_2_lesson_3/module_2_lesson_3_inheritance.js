"use strict";
// class Prop {
//          constructor(width, color) {
//                    this.width = width;
//                    this.color = color;
//          }
// }
//
// class Line {
//          constructor(sp, ep, width, color) {
//                    this.sp = sp;
//                    this.ep = ep;
//                    this.width = width;
//                    this.color = color;
//          }
//
//          draw() {
//                    console.log("Линия: "+this.sp.x+", "+this.sp.y+
//                                      ", "+this.ep.x+", "+this.ep.y);
//          }
// }
/////////////////////////////////////////////////////////////////////////////
// class Prop {
//          constructor(width, color) {
//                    this.width = width;
//                    this.color = color;
//          }
// }
//
// class Line extends Prop{
//          constructor(sp, ep, width, color) {
//                    super (width, color)
//                    this.sp = sp;
//                    this.ep = ep;
//                    // this.width = width;
//                    // this.color = color;
//          }
//
//          draw() {
//                    console.log("Линия: "+this.sp.x+", "+this.sp.y+
//                                      ", "+this.ep.x+", "+this.ep.y);
//          }
// }
// let l1 = new Line({x: 0, y: 0}, {x: 10, y: 20}, 1, 'red');
// console.log(l1)
/////////////////////////////////////////////////////////////////////////////
// class Prop {
//          constructor(width, color) {
//                    this.width = width;
//                    this.color = color;
//          }
//          getColor() {
//                    return this.color;
//          }
//
// }
//
// class Line extends Prop{
//          constructor(sp, ep, width, color) {
//                    super (width, color)
//                    this.sp = sp;
//                    this.ep = ep;
//                    // this.width = width;
//                    // this.color = color;
//          }
//          // getColor() {
//          //           return '[]'+this.color+'[]';
//          // }
//
//          // getColor() {
//          //     let color = super.getColor();
//          //     return '[|]'+color+'[|]';
//          // }
//
//          draw() {
//                    console.log("Линия: "+this.sp.x+", "+this.sp.y+
//                                      ", "+this.ep.x+", "+this.ep.y);
//          }
// }
// let l1 = new Line({x: 0, y: 0}, {x: 10, y: 20}, 1, 'red')
// console.log(l1.getColor());

/////////////////////////////////////////////////////////////////////////////
// class Prop {
//          constructor(width, color) {
//                    this.width = width;
//                    this.color = color;
//          }
//          getColor() { return this.color; }
// }

// class Prop {
//          getColor() { return this.color; }
// }
//
// class Line extends Prop {
//          draw() {
//                    console.log("Линия: "+this.sp.x+", "+this.sp.y+
//                                      ", "+this.ep.x+", "+this.ep.y);
//          }
// }
//
// let l1 = new Line({x: 0, y: 0}, {x: 10, y: 20}, 1, 'red');
// console.log( l1 );
//
// // constructor(...args) {
// //     super(...args);
// // }

/////////////////////////////////////////////////////////////////////////////
// class Prop {
//          constructor(width, color) {
//                    this.width = width;
//                    this.color = color;
//          }
//          getColor() { return this.color; }
// }

// function getExtends(type) {
//          return class {
//                    constructor(width, color) {
//                             this.type = type;
//                             this.width = width;
//                             this.color = color;
//                    }
//          };
// }
//
// class Line extends getExtends('2D') {
//     draw() {
//         console.log("Линия: " + this.sp.x + ", " + this.sp.y +
//             ", " + this.ep.x + ", " + this.ep.y);
//     }
// }
// let l1 = new Line({x: 0, y: 0}, {x: 10, y: 20}, 1, 'red');
// console.log( l1 );
/////////////////////////////////////////////////////////////////////////////
// создать класс "животное" /поля - скорость и имя/методы (с alert)
// 1 - имя бежит сос коростью --- такой то
// 2 - стоит на месте
//
// сщздать своего питомца у которого есть свой уникальный метод и вывести
// по отдельности результат работы ваших методов после создания питомца

// class Animal {
//         constructor(name) {
//                 this.speed = 0;
//                 this.name = name;
//                 }
//         run(speed) {
//                 this.speed = speed;
//                 alert(`${this.name} бежит со скоростью ${this.speed}.`);
//         }
//         stop() {
//                 this.speed = 0;
//                 alert(`${this.name} стоит неподвижно.`);
//         }
// }
// class Rabbit extends Animal {
//        hide() {
//                 alert(`${this.name} прячется!`);
//        }
// }
//
// let rabbit = new Rabbit("Белый кролик");
//
// rabbit.run(5); // Белый кролик бежит со скоростью 5.
// rabbit.stop()
// rabbit.hide(); // Белый кролик прячется!