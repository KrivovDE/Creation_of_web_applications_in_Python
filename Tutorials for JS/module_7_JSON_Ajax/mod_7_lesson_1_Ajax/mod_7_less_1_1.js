// let person = {
//  firstName: "Andrey",
//  lastName: "Ivanov",
//  birthDate : "05.05.2000"
// }

//        "{
//          "firstName" : "Andrey",
//          "lastName" : "Ivanov",
//          "birthDate" : "04.05.2000"
//         }"
// ////////////////////////////////////////////////
// {
//  "firstName" : "Andrey",
//  "lastName" : "Ivanov",
//  "age" : 20,
//  "isStudent" : true
// }
// ////////////////////////////////////////////////
// {
//  "firstName" : "Andrey",
//  "lastName" : "Ivanov",
//  "age" : 20,
//  "isStudent" : true,
//  "сontactInfo" : {
//  "phone" : "098-556-33-41",
//  "email" : "AndreyIvanov@gmail.com"
//  },
//  "disciplines" : ["Programming", "Machine engineering", "English"]
// }
// ////////////////////////////////////////////////

// let person = {
//                firstName: "Andrey",
//                lastName: "Ivanov",
//                age: 20,
//                isStudent: true,
//                contactInfo: {
//                              "phone": "098-556-33-41",
//                              "email": "AndreyIvanov@gmail.com"
//                              },
//                disciplines: ["Programming", "Machine engineering", "English"]
//               }
//
// let jsonPerson = JSON.stringify(person);
// document.write(`<h1 style="color: blue">` + jsonPerson + `</h1>`)
//

////////////////////////////////////////////////
// Циклическая ссылка
// let Kate = {
//  name : "Kate"
// }
// let Dev = {
//  name: "Dev"
// }
// Kate.parent = Dev;
// Dev.child = Kate;
// let family = JSON.stringify(Dev);
// console.log(family);

////////////////////////////////////////////////
// let person = {
//                firstName: "Andrey",
//                lastName: "Ivanov",
//                age: 19,
//                isStudent: true,
//                contactInfo: {
//                              "phone": "098-556-33-41",
//                              "email": "AndreyIvanov@gmail.com"
//                              },
//                disciplines: ["Programming", "Machine engineering", "English"]
//               }
//
// function checkAge(key, value) {
//     if (key === "age" && value >= 18) {
//         return undefined;
//     }
//     return value;
// }

// let jsonPerson2 = JSON.stringify(person, checkAge);
// document.write(`<h1 style="color: red">` + jsonPerson2 + `</h1>`)

// let jsonPerson3 = JSON.stringify(person, ["firstName", "lastName"]);
// document.write(`<h1 style="color: mediumspringgreen">` + jsonPerson3 + `</h1>`)

// let jsonPerson3 = JSON.stringify(person, ["firstName", "lastName"]);
// document.write(`<h1 style="color: mediumspringgreen">` + jsonPerson3 + `</h1>`)
// console.log(jsonPerson3)

// let jsonPerson4 = JSON.stringify(person, null, 2);
// document.write(`<h1 style="color: blueviolet">` + jsonPerson4 + `</h1>`)
// console.log(jsonPerson4)
////////////////////////////////////////////////
// let personStr = '{' +
//                 '"firstName": "Andrey", ' +
//                 '"lastName": "Ivanov",' +
//                 '"age": 20, ' +
//                 '"isStudent": true, ' +
//                 '"contactInfo": { ' +
//                                     '"phone": "098-556-33-41", ' +
//                                     '"email": "AndreyIvanov@gmail.com" }, ' +
//                 '"disciplines": [ "Programming", "Machine engineering", "English" ]' +
//                 '}'
//
// let person = JSON.parse(personStr);
// console.log(typeof(person))
// console.log(person)
//
// alert(person.firstName)
// alert(person.contactInfo.phone);
////////////////////////////////////////////////
let personStr = '{' +
                '"firstName": "Andrey", ' +
                '"lastName": "Ivanov",' +
                '"age": 20, ' +
                '"isStudent": true, ' +
                '"contactInfo": { ' +
                                    '"phone": "098-556-33-41", ' +
                                    '"email": "AndreyIvanov@gmail.com" }, ' +
                '"disciplines": [ "Programming", "Machine engineering", "English" ]' +
                '}'

function CheckIsStudent(key, value) {
    if (key === "isStudent" && value === true) {
        return undefined;
    }
return value;
}

let person2 = JSON.parse(personStr, CheckIsStudent);
alert(person2.isStudent);
////////////////////////////////////////////////

// let model = {
//             name: "BMW",
//             autopilot : undefined,
//             toJSON(){
//                     let jsonStr = `{"name": "${this.name}", "autopilot": `;
//                     if(this.autopilot === undefined){
//                         jsonStr += `"Not"}`
//                     }
//                     else{
//                         jsonStr += `"${this.autopilot}"`
//                     }
//             return jsonStr;
//             }
//
// }
// let car = {
//             color: "Black",
//             date : new Date(2022, 2, 24),
//             model
// }
//
// let carJSON = JSON.stringify(car)
// alert(carJSON)
// document.write(`<h1 style="color: darkorange">` + carJSON + `</h1>`)




























