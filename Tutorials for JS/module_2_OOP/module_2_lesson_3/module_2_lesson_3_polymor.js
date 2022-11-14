// "use strict";
// //
// // class User {
// //   constructor(email, password) {
// //     this.email = email;
// //     this.password = password;
// //   }
// //
// //   login(email, password) {
// //     if (email === this.email && password === this.password) {
// //       console.log('Login Successfully');
// //     }
// //     else {
// //       console.log('Authentication Failed!!');
// //     }
// //   }
// // }
// //
// // class Author extends User {
// //   #numOfPost;
// //   constructor(email, password) {
// //     super(email, password);
// //     this.#numOfPost = 0;
// //   }
// //
// //   createPost(content) {
// //     this.#numOfPost++;
// //   }
// //
// //   getNumOfPost() {
// //     return this.#numOfPost;
// //   }
// // }
// //
// // class Admin extends User {
// //   constructor(email, password) {
// //     super(email, password);
// //   }
// //
// //   login(email, password) {
// // 		const isAdminValid = true;
// // 		// делаем проверку на валидность администратора
// // 		// например 2-ух факторная идентификация
// //     if (email === this.email && password === this.password && isAdminValid === true) {
// //       console.log('Admin Login Successfully');
// //     }
// //     else {
// //       console.log('Authentication Failed!!');
// //     }
// //   }
// //
// //   removeUser(userId) {
// //     console.log('User Removed successfully.');
// //   }
// // }
// //
// // const author= new Author('author@gmail.com', 'password:)');
// // author.login('author@gmail.com', 'password:)'); // Login Successfully
// //
// // const admin= new Admin('admin@gmail.com', 'password');
// // admin.login('admin@gmail.com', 'password'); // Admin Logi
// //////////////////////////////////////////////////////////////////////////
//
// class Human {
//   constructor(name) {
//     this.name = name;
//   }
//
//   say() {
//     return `Хороший человек по имени ${this.name}`;
//   }
// }
//
// class Men extends Human {
//   constructor(name) {
//     super(name)
//   }
//   // Берем метод say у родителя.
// }
//
// class Coder extends Human {
//   constructor(name) {
//     super(name)
//   }
//
//   say() {
//     // Переопределяем метод родителя say для отображения нового значения.
//     return `Привет! Я ${this.name}, Я люблю яблоки!`;
//   }
// }
//
// let nata = new Men('Наташа');
// let toha = new Coder('Антон');
//
// console.log(nata.say())
//
// console.log(toha.say())
