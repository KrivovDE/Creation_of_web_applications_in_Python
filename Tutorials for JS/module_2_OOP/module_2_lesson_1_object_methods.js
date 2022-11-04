'use strict';

//
// let car = {
//     model: "toyota",
//     color: "black",
//     go: function() {
//           console.log("машина едет");
//     }
// };
// car.go();
//
// car.stop = function () {
//     console.log("машина остановлена");
// }
// car.stop()

// let car = {
//     model: "toyota",
//     color: "black",
//     go: function (driverName) {
//           console.log("Водитель " + driverName + ": машина едет");
//     },
//     stop: function () {
//           console.log("машина остановлена");
//     }
// };
// car.go("Глеб");

// //ES6
// let car = {
//     model: "toyota",
//     color: "black",
//     go(driverName) {
//         console.log("Водитель " + driverName + ": машина едет");
//     },
//     stop() {
//         console.log("машина остановлена");
//     },
//     getModel() {
//          return this.model;
//     }
//
// };
// console.log(car.getModel())
//
// function getModel() {
//     return this.model;
// }
//
// let car1 = {model: "toyota"};
// let car2 = {model: "opel"};
//
// car1.getModel = getModel;
// car2.getModel = getModel;
//
// console.log( car1.getModel() );
// console.log( car2.getModel() );
//
//
// let car = {
//     model: "toyota",
//     getModel() {
//         return this.model;
//     }
// };
//
// let get = car.getModel();
//
// console.log( car.getModel() );
// console.log( get() );





