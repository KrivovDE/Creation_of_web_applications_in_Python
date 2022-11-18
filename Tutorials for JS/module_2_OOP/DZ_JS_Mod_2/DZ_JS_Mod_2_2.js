'use strict';

// Задание 1
// Создать массив «Список покупок». Каждый элемент массива
// является объектом, который содержит название продукта, необ-
// ходимое количество и куплен или нет. Написать несколько функ-
// ций для работы с таким массивом.
// 1. Вывод всего списка на экран таким образом, чтобы сначала
// шли некупленные продукты, а потом – купленные.
// 2. Добавление покупки в список. Учтите, что при добавлении
// покупки с уже существующим в списке продуктом, необ-
// ходимо увеличивать количество в существующей покупке,
// а не добавлять новую.
// 3. Покупка продукта. Функция принимает название продукта
// и отмечает его как купленный.

// let shoppingList = [                                     //создаем массив "список покупок"
//     {product: 'bread', quantity: 1, buy: 'yes'},          //yes и no вместо true и false только для наглядности
//     {product: 'milk', quantity: 2, buy: 'no'},            //хотя я уже знаю способ их красиво преобразовать, но
//     {product: 'eggs', quantity: 10, buy: 'no'},           //исправлять не стал. В другой раз сделаю лучше.
//     {product: 'beer', quantity: 3, buy: 'yes'},
//     {product: 'mushrooms', quantity: 5, buy: 'no'}
// ];
// function sortShoppingList() {                              //сортируем по принципу куплен или нет
//     for (let i=0; i<shoppingList.length; i++) {
//         if (shoppingList[i].buy === 'no') {
//             shoppingList.unshift(shoppingList[i]);
//             shoppingList.splice(i+1,1);
//         }
//     }
// }
// sortShoppingList();                                        //выводим список на экран
// function listLog() {
//     for (let i=0; i<shoppingList.length; i++) {
//         console.log(shoppingList[i].product + ' ' + shoppingList[i].quantity + 'pcs, bought: ' + shoppingList[i].buy);
//     }
// }
// listLog();
// function addProduct() {                                     //добавляем продукт
//     let newProd = {};
//     newProd.product = prompt('Enter what else do you want to buy?', 'meet');
//     newProd.quantity = +prompt('Enter how much of this product do you need?');
//     for (let i=0; i<shoppingList.length; i++) {                   //проверяем на наличие продукта в списке
//         if (newProd.product === shoppingList[i].product) {
//             shoppingList[i].quantity += newProd.quantity;
//             return;
//         }
//     }
//     newProd.buy = 'no';
//     shoppingList.unshift(newProd);
// }
// addProduct();
// console.log('List after adding product:');
// listLog();
// function buyProduct() {                                      //отмечаем купленный продукт
//     let buyProd = prompt('Enter purchased product');
//     for (let i=0; i<shoppingList.length; i++) {
//         if (buyProd === shoppingList[i].product) {
//             shoppingList[i].buy = 'yes';
//             break;
//         }
//     }
// }
// buyProduct();
// sortShoppingList();
// console.log('List after purchasing product:');
// listLog();

// Задание 2
// Создать массив, описывающий чек в магазине. Каждый эле-
// мент массива состоит из названия товара, количества и цены за
// единицу товара. Написать следующие функции.
// 1. Распечатка чека на экран.
// 2. Подсчет общей суммы покупки.
// 3. Получение самой дорогой покупки в чеке.
// 4. Подсчет средней стоимости одного товара в чеке.

// let check = [                                           //создаем массив
//     {product: 'T-shirt', quantity: 3, price: 990},
//     {product: 'Sneakers', quantity: 1, price: 3490},
//     {product: 'Ball', quantity: 2, price: 2500},
//     {product: 'Socks', quantity: 8, price: 250},
//     {product: 'Cap', quantity: 1, price: 1590}
// ];
// function logCheck() {                                     //выводим на экран чек
//     for (let i=0; i<check.length; i++) { //используем метод ≠, чтобы добавить точки и выровнять значения в консоли
//         console.log(check[i].product.padEnd(20, '.') + ' : ' + check[i].quantity + ' pcs *' + ' '
//             +  check[i].price + ' rub');
//     }
// }
// function sumCheck() {                   //выводим на экран сумму чека
//     let sum = 0;
//     for (let i=0; i<check.length; i++) {
//         sum +=check[i].price * check[i].quantity;
//     }
//     console.log('Total :'.padEnd(31, '.') + sum + ' rub');
//     return sum;
// }
// function mostExpensiveCheck() {           //выводим самый дорогой товар
//     let maxIndex = 0;
//     for (let i=1; i<check.length; i++) {
//         if (check[i].price > check[maxIndex].price) maxIndex = i;
//     }                                    //самый дорогой товар за ... рублей
//     console.log('Most expensive is ' + check[maxIndex].product + ' for ' + check[maxIndex].price + ' rub');
// }
// function averageCostCheck() {   //средняя стоимость в чеке в зависимости от общего количества проданных товаров
//     let quan = 0;
//     for (let i=0; i<check.length; i++) quan += check[i].quantity;               //округляем до копеек
//     console.log('Average cost in check :'.padEnd(31, '.') + (sumCheck()/quan).toFixed(2) + ' rub');
// }
// logCheck();
// console.log(''.padStart(40, '_'));
// sumCheck();
// mostExpensiveCheck();
// averageCostCheck();

// Задание 3
// Создать массив css-стилей (цвет, размер шрифта, выравнива-
// ние, подчеркивание и т. д.). Каждый элемент массива – это объ-
// ект, состоящий из двух свойств: название стиля и значение стиля.
// Написать функцию, которая принимает массив стилей и
// текст, и выводит этот текст с помощью document.write() в тегах
// <p></p>, добавив в открывающий тег атрибут style со всеми сти-
// лями, перечисленными в массиве.

// let styleSheet = [                           //создаем массив из объектов
//     {name: 'color', value: 'red'},
//     {name: 'font-size', value: '20px'},
//     {name: 'align', value: 'center'},
//     {name: 'text-decoration', value: 'underline'},
//     {name: 'text-transform', value: 'capitalize'}
// ];
// function logText() {                                 //функция запрашивающая текст и создающая строку для тега style
//     let text = prompt('Enter text', 'For example just this');
//     let arrStyle =[];                             //создаем пустой массив
//     for (let i=0; i<styleSheet.length; i++) {
//         arrStyle.push(styleSheet[i].name + ': ' + styleSheet[i].value);  //записываем в него значения полей из объектов
//     }
//     console.log('style = ' + arrStyle.join('; '));          //объединяем массив в одну строку с помощью метода join
//     document.write('<p style="' + arrStyle.join('; ') + '">' + text + '</p>'); //выводим текст на экран
// }
// logText();

// Задание 4
// Создать массив аудиторий академии. Объект-аудитория со-
// стоит из названия, количества посадочных мест (от 10 до 20) и
// названия факультета, для которого она предназначена.
// Написать несколько функций для работы с ним.
// 1. Вывод на экран всех аудиторий.
// 2. Вывод на экран аудиторий для указанного факультета.
// 3. Вывод на экран только тех аудиторий, которые подходят для
// переданной группы. Объект-группа состоит из названия,
// количества студентов и названия факультета.
// 4. Функция сортировки аудиторий по количеству мест.
// 5. Функция сортировки аудиторий по названию (по алфа-
// виту).
//
// let arrAcademy = [                                     //создаем массив
//     {name: 'aud C', seats: 20, faculty: 'Fiz'},        //имя, количество мест, факультет
//     {name: 'aud E', seats: 18, faculty: 'Mat'},
//     {name: 'aud A', seats: 10, faculty: 'Him'},
//     {name: 'aud D', seats: 15, faculty: 'Mat'},
//     {name: 'aud F', seats: 13, faculty: 'Fiz'},
//     {name: 'aud B', seats: 17, faculty: 'Him'}
// ];
// function logAud() {                                    //функция для вывода аудиторий
//     for (let i=0; i<arrAcademy.length; i++) {
//         console.log('class: '+arrAcademy[i].name+' have '+arrAcademy[i].seats+' seats, faculty is '
//             +arrAcademy[i].faculty);
//     }
// }
// function logFacAud() {                                     //функция для вывода аудиторий по конкретному факультету
//     let fac = prompt('Choose faculty: Fiz/Mat/Him', 'Mat');
//     for (let i=0; i<arrAcademy.length; i++) {
//         if (fac===arrAcademy[i].faculty) console.log('class: ' + arrAcademy[i].name + ' belongs to the faculty ' + fac);
//     }
// }
// function chooseAudForGroup() {                          //функция подбирающая подходящую аудиторию для группы
//     let studGroup = {};                                      //создаем объект группы
//     studGroup.name = prompt('Enter name of group', 'First course');
//     studGroup.quan = +prompt('Enter quantity of group', '14');
//     studGroup.fac = prompt('Enter faculty of group','Fiz');
//     let ch=false;
//     for (let i=0; i<arrAcademy.length; i++) {
//         if (arrAcademy[i].seats>=studGroup.quan && arrAcademy[i].faculty===studGroup.fac) {
//             console.log('class: '+ arrAcademy[i].name +' is suitable for '+ studGroup.name); //эти аудитории подходят
//             ch=true;                                //проверяем были ли вообще подходящие аудитории
//         }
//     }
//     if (!ch) console.log('No class for your group!'); //нет таких
// }
// function sortAudSeats() {                    //функция для сортировки аудиторий согласно посадочных мест
//     let tempObj={};
//     let ch=false;
//     for (let i=0; i<arrAcademy.length-1; i++) {
//         if (arrAcademy[i+1].seats < arrAcademy[i].seats) {
//             tempObj=arrAcademy[i+1];
//             arrAcademy[i+1]=arrAcademy[i];
//             arrAcademy[i]=tempObj;
//             ch=true;
//         }
//     }
//     if (ch) sortAudSeats();    //Если перестановки чисел были, то функция действует с начала
// }
// function sortAudName() {                      //функция для сортировки имен аудиторий по алфавиту
//     let tempObj={};
//     for (let i=0; i<arrAcademy.length; i++) {        //другой способ сортировки с помощью вложенного цикла
//         for (let j=i+1; j<arrAcademy.length; j++) {
//             if (arrAcademy[j].name < arrAcademy[i].name) {
//                 tempObj=arrAcademy[j];
//                 arrAcademy[j]=arrAcademy[i];
//                 arrAcademy[i]=tempObj;
//             }
//         }
//     }
// }
// logAud();
// console.log(''.padStart(30, '_'));
// logFacAud();
// console.log(''.padStart(30, '_'));
// chooseAudForGroup();
// console.log(''.padStart(30, '_'));
// sortAudSeats();
// logAud();
// console.log(''.padStart(30, '_'));
// sortAudName();
// logAud();