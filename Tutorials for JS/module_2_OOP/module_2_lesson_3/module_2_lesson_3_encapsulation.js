"use strict";
// class Users {
//          constructor(name, old) {
//                    this._name = name;
//                    this._old = old;
//          }
//
//          _getName() { return this._name; }
// }
// let u1 = new Users('Роман', 30)
// console.log( u1._name );
///////////////////////////////////////////////////////

// class Users {
//          #name;
//          #old;
//          constructor(name, old) {
//                    this.#name = name;
//                    this.#old = old;
//          }
//          _getName() { return this.#name; }
// }
//
// class Admin extends Users {
//          constructor(name, old, login, psw) {
//                    super(name, old);
//                    this.login = login;
//                    this.psw = psw;
//          }
// }
//
// let u1 = new Users("Анатолий", 38);
// let u2 = new Admin("Евгений", 38, "admin", "1111");
//
// console.log( u1._getName() );
// console.log( u2._getName() );

// console.log( u1.#name );
///////////////////////////////////////////////////////

// console.log( u1 instanceof Admin);   // false
// console.log( u2 instanceof Admin );   // true
//
// // А, вот если вместо Admin написать Users:

// console.log( u1 instanceof Users);
// console.log( u2 instanceof Users);

// console.log( u1.constructor == Users);
// console.log( u2.constructor == Users);

///////////////////////////////////////////////////////

///////////////////////////////////////////////////////
