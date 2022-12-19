'use strict';
// let request;
// if(window.XMLHttpRequest){
//  request = new XMLHttpRequest();
// }
// else{
//  request = new ActiveXObject("Microsoft.XMLHTTP");
// }

// ////////////////////////////////////////////////
//
// open(method, URL, [async, user, password])

////////////////////////////////////////////////
// let request;
// if(window.XMLHttpRequest){
//  request = new XMLHttpRequest();
// }
// else{
//  request = new ActiveXObject("Microsoft.XMLHTTP");
// }
// request.open("GET", "text.txt");
//
// request.onreadystatechange = function(){
//     console.log("readyState = " + request.readyState);
//     if(request.readyState === 4){alert(request.response);}
// }
// request.send();
// ////////////////////////////////////////////////
// let request;
// if(window.XMLHttpRequest){
//  request = new XMLHttpRequest();
// }
// else{
//  request = new ActiveXObject("Microsoft.XMLHTTP");
// }
// request.open("GET", "person.txt");
//
// request.responseType = "json";
//
// request.onreadystatechange = function(){
//      if(request.readyState === 4 && request.status === 200){
//          let person = request.response;
//          console.log(person);
//      }
// }
// request.send();
// ////////////////////////////////////////////////
// let request;
// if(window.XMLHttpRequest){
//  request = new XMLHttpRequest();
// }
// else{
//  request = new ActiveXObject("Microsoft.XMLHTTP");
// }
// request.open("GET", "person.txt");
// request.onreadystatechange = function(){
//      if(request.readyState === 4 && request.status === 200){
//      alert(request.responseText);
//      console.log(request.responseText)
//      }
// }
// request.send();
////////////////////////////////////////////////
// let request;
// if(window.XMLHttpRequest)
//     request = new XMLHttpRequest();
// else
//     request = new ActiveXObject("Microsoft.XMLHTTP");
//
// request.open("GET", "person.txt");
// request.onload = function(){
//      if(request.status === 200)
//          alert(request.response)
// }
// request.send();
// ////////////////////////////////////////////////
// let request;
// if(window.XMLHttpRequest)
//     request = new XMLHttpRequest();
// else
//     request = new ActiveXObject("Microsoft.XMLHTTP");
//
// request.open("GET", "text.txt");
//
// request.onloadend = function(event){
//     console.log(`Загружено ${event.loaded}`);
// }
// request.onerror = function(){
//     alert("Ошибка");
// }
// request.onload = function(){
//     if(request.status === 404)
//         alert(request.response);
// }
// request.send();
// ////////////////////////////////////////////////
// let request;
// if(window.XMLHttpRequest)
//     request = new XMLHttpRequest();
// else
//     request = new ActiveXObject("Microsoft.XMLHTTP");
//
// request.open("GET","http://api.openweathermap.org/data/2.5/weather?q=Kiev&units=metric&APPID=b03a2cfad336d11bd9140ffd92074504");
//
// request.onload = function() {
//     if (request.status === 200)
//         let per = request.response;
//         let person2 = JSON.parse(person);
//
//         //     console.log(typeof (person2))
// //     console.log(person2);
// }
// request.send();
//
// // https://openweathermap.org/api
// ////////////////////////////////////////////////
//                             GET /info.html HTTP/1.1              Стартовая строка
//                             Host: mywebsite.ru                   хост, на котором расположен сайт
//                             User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)        информация о клиенте
//                             AppleWebKit/537.36 (KHTML, like Gecko)                       тип ожидаемого ответа от сервера.
//                             Chrome/80.0.3987.122 Safari/537.36
//                             Accept: text/html

// ////////////////////////////////////////////////
// let person = {
//         firstName: "Andrey",
//         lastName: "Ivanov",
//         age: 20
// }
// let request;
// if(window.XMLHttpRequest)
//     request = new XMLHttpRequest();
// else
//     request = new ActiveXObject("Microsoft.XMLHTTP");
//
//
// let jsonPerson = JSON.stringify(person);
// request.open("GET", "text.txt");
//
// request.setRequestHeader('Content-Type', 'application/json');
// request.send(jsonPerson);


// ////////////////////////////////////////////////

// ////////////////////////////////////////////////












































