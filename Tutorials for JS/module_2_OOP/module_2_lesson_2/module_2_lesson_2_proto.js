"use strict";

// let geom = {
//     name: "фигура",
//     sp: {x: 0, y: 0},
//     ep: {x: 100, y: 20}
// };
//
// // for(let key in geom) {
// //          console.log(key+": "+geom[key]);
// // }
// //
// let rect = {
//          draw() {
//                    console.log("Рисование прямоугольника: " +
//                             this.sp.x+","+this.sp.y+","+this.ep.x+","+this.ep.y);
//          }
// };
//
// rect.__proto__ = geom;
// //
// // for(let key in rect) {
// //          console.log(key+": "+rect[key]);
// // }
// // rect.draw()
//
// let info = {
//
//          getInfo() {
//                    console.log(this.name);
//          },
//          __proto__: rect
// }
//
// info.getInfo()

//////////////////////////////////////////////////////////////////////
// •	set <имя метода>([параметры]) {…} – свойство для записи значений в объект;
// •	get <имя метода>([параметры]) {…} – свойство для чтения значений из объекта.

//
let geom = {
         name: "фигура",
         sp: {x: 0, y: 0},
         ep: {x: 100, y: 20},
         get nameGeom() {return this.name; },
         set nameGeom(name) {this.name = name;},
};
let rect = {
         // name: "Прямоугольник",
         draw() {
                   console.log("Рисование прямоугольника: " +
                            this.sp.x+","+this.sp.y+","+this.ep.x+","+this.ep.y);
         },
         __proto__: geom

};

// //
// //
// console.log(rect.nameGeom);      // чтение свойства
// rect.nameGeom = "Прямоугольник"; // запись свойства
// console.log(rect.nameGeom);
// console.log(geom.nameGeom);
//////////////////////////////////////////////////////////////////////
// let prop = {
//          sp: {x: 0, y: 0},
//          ep: {x: 100, y: 20},
//          get coords() {
//                    return [this.sp.x, this.sp.y, this.ep.x, this.ep.y];
//          },
//          set coords(coords) {
//                    this.sp.x = coords[0]; this.sp.y = coords[1];
//                    this.ep.x = coords[2]; this.ep.y = coords[3];
//          }
// };
//
//
// function Rect() {
//          this.name = "прямоугольник";
//
//          this.draw = function() {
//                    console.log("Рисование фигуры: "+this.name);
//          }
//          // this.__proto__ = prop;
// }
// Rect.prototype = prop;
//
// let r = new Rect();
// // r.draw();
// for(let p in r)
//          console.log(p+': '+r[p]);

// //////////////////////////////////////////////////////////////////////
// let prop = {
//          sp: {x: 0, y: 0},
//          ep: {x: 100, y: 20},
//          get coords() {
//                    return [this.sp.x, this.sp.y, this.ep.x, this.ep.y];
//          },
//          set coords(coords) {
//                    this.sp.x = coords[0]; this.sp.y = coords[1];
//                    this.ep.x = coords[2]; this.ep.y = coords[3];
//          }
// };
// function Rect() {
//          this.name = "прямоугольник";
//
//          this.draw = function() {
//                    console.log("Рисование фигуры: "+this.name);
//          }
//          // this.__proto__ = prop; ---- вместо этой  строчки
// }
//
// // Rect.prototype = prop // вот эта строчка
// //
// // let r = new Rect();
// //
// // for(let p in r)
// //          console.log(p+': '+r[p]);
// //////////////////////////////////////////////////////////////////////
// //
// // Создать себя как обект с двумя свойствами имя и фамилия,
// // а так же геттерами и сеттерами, для их изменения, вывести в консоль свои данные,
// //     поменять их на данные соседа и вывести в консоль
// let studentTop = {
//          name: "Dmitrii",
//          surname: "Krivov",
//
//          get nameTop() {return this.name; },
//          get surnameTop() {return this.surname; },
//          set nameTop(name) {this.name = name; },
//          set surnameTop(surname) {this.surname = surname; },
// };
// console.log(studentTop.nameTop)
// console.log(studentTop.surnameTop)
//
// studentTop.nameTop = 'Alex'
// studentTop.surnameTop = 'Meshcheryakov'
//
// console.log(studentTop.nameTop)
// console.log(studentTop.surnameTop)







