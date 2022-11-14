// "use strict";
// // class Users {
// //          constructor(name, old) {
// //                    this._name = name;
// //                    this._old = old;
// //          }
// //
// //          _getName() { return this._name; }
// // }
// // let u1 = new Users('Роман', 30)
// // console.log( u1._name );
// ///////////////////////////////////////////////////////
//
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
// //
// // console.log( u1._getName() );
// // console.log( u2._getName() );
// //
// // console.log( u1.#name );
// ///////////////////////////////////////////////////////
//
// // console.log( u1 instanceof Admin);   // false
// // console.log( u2 instanceof Admin );   // true
//
// // // А, вот если вместо Admin написать Users:
//
// // console.log( u1 instanceof Users);
// // console.log( u2 instanceof Users);
// //
// // console.log( u1.constructor == Users);
// // console.log( u2.constructor == Users);
//
// ///////////////////////////////////////////////////////
// // Создать класс User с полями имя и #пароль
// // метод логин принимающий эти данные и прорверяющий их
// // на соответствие с переданными данными при инициализации объекта
// // выводит в консоль Вход выполнен если ОК, а если не ОК то сорян
// // и приватные метод измененя пароля
// // И продемонстрировать работоспособность))
//
// class User {
// 	#password;
// 	constructor(name, password) {
// 		this.name = name;
// 		this.#password = password;
// 	}
// 	login(name, password) {
// 		if (name === this.name && password === this.#password) {
// 			console.log('Вход выполнен');
// 		} else {
// 			console.log('Сорян!!');
// 		}
// 	}
//
// 	setPassword(newPassword) {
// 		this.#password = newPassword;
// 	}
// }
//
// // let user = new User('Test testov','password:)');
// // user.login('Test testov', 'password:)');
//
// // console.log(user.name);
// // console.log(user.password);
// // console.log(user.#password);
// //
// user.setPassword('new_password:)');
//
// user.login('Test testov', 'new_password:)');
//
// ///////////////////////////////////////////////////////
