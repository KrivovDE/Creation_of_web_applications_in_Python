// 'use strict';
//
// // Задание 1
// // Реализовать класс, описывающий простой маркер. В классе
// // должны быть следующие компоненты:
// // ■■ поле, которое хранит цвет маркера;
// // ■■ поле, которое хранит количество чернил в маркере (в про-
// // центах);
// // ■■ метод для печати (метод принимает строку и выводит
// // текст соответствующим цветом; текст выводится до тех
// // пор, пока в маркере есть чернила; один не пробельный
// // символ – это 0,5% чернил в маркере).
// // Реализовать класс, описывающий заправляющийся маркер,
// // унаследовав его от простого маркера и добавив метод для заправки
// // маркера.
// // Продемонстрировать работу написанных методов.
//
// // class Marker {
// //     constructor(color, inkLevel) {
// //         this.color = color;
// //         this.inkLevel = inkLevel;
// //     }
// //     print() {
// //
// //         let i=0;
// //         let newStr ='';
// //         while (this.inkLevel>=0.5 && str[i]!==undefined) {
// //             newStr +=str[i];
// //             if (str[i] !== ' ') this.inkLevel -= 0.5;
// //             i++;
// //         }
// //         document.write(`<p style="color:` + this.color + `">` + newStr + `</p>`); //выводим печать на экран
// //         console.log('Ink left after printing: ' + this.inkLevel);  //выводим остаток чернил в консоль
// //         return(this.inkLevel);  //возвращаем остаток чернил
// //     }
// // }
// //
// // class AddInkMarker extends Marker {
// //     constructor(color,inkLevel,addInk) {
// //         super(color,inkLevel);
// //         this.addInk = addInk;
// //     }
// //     fillUp () {
// //         this.inkLevel += this.addInk;  //добавляем к уровню чернил в родительском классе новые чернила
// //         console.log('Now Ink level is ' + this.inkLevel);  //выводим остаток чернил в консоль
// //     }
// // }
// // let col;
// // let pr = new Marker(col = prompt('Enter color of Ink','red'),+prompt('Enter level of Ink','100'));
// // let str = prompt('Enter your text','Интернет является основой сети (the Web),  технической ' +
// //             'инфраструктурой, благодаря которой и существует Всемирная Паутина. По своей сути, интернет - очень ' +
// //             'большая сеть  компьютеров, которые могут взаимодействовать друг с другом.');
// // let rem = pr.print(str);
// // let refill = new AddInkMarker(col,rem,+prompt('Enter level of Ink for refilling','10'));
// // refill.fillUp();
// // refill.print();
//
// // Задание 2
// // Реализуйте класс ExtendedDate, унаследовав его от стандарт-
// // ного класса Date и добавив следующие возможности:
// // ■■ метод для вывода даты (числа и месяца) текстом;
// // ■■ метод для проверки – это прошедшая дата или будущая
// // (если прошедшая, то метод возвращает false; если буду-
// // щая или текущая, то true);
// // ■■ метод для проверки – високосный год или нет;
// // ■■ метод, возвращающий следующую дату.
// // Создайте объект класса ExtendedDate и выведите на экран
// // результаты работы новых методов.
//
// // class ExtendedDate extends Date {
// //     dateLog(userdata) {
// //         let arrMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
// //         console.log(userdata.getDate() + ' ' + arrMonth[userdata.getMonth()]);
// //     }
// //     pastOrFuture(userdata) {
// //         let res;
// //         res = userdata.getDate() >= this.getDate();
// //         res = userdata.getMonth() >= this.getMonth();
// //         res = userdata.getFullYear() >= this.getFullYear();
// //         return res;
// //     }
// //     abnormalYear(userdata) {
// //         let y = userdata.getFullYear();
// //         if (y % 400 === 0) return true;
// //         return (y % 4 === 0 && y % 100 !== 0);
// //     }
// //     nextDate(userdata) {
// //         userdata.setDate(userdata.getDate()+1);
// //         return userdata;
// //     }
// // }
// // let eD = new ExtendedDate();
// // let anyDay = new Date(prompt('Enter your date in year-month-day format', '2022-11-15'));
// // eD.dateLog(anyDay);
// // console.log('It is a future Date: ' + eD.pastOrFuture(anyDay));
// // console.log('It is a Date of abnormal year: ' + eD.abnormalYear(anyDay));
// // console.log('Next date is ' + eD.nextDate(anyDay));
//
// // Задание 3
// // Реализовать класс Employee, описывающий работника, и со-
// // здать массив работников банка.
// // Реализовать класс EmpTable для генерации html кода таблицы
// // со списком работников банка. Массив работников необходимо
// // передавать через конструктор, а получать html код с помощью
// // метода getHtml().
// // Создать объект класса EmpTable и вывести на экран результат
// // работы метода getHtml().
//
// class Employee {
//     constructor(surname, name, age, experience, jobTitle) {
//         this.surname = surname;
//         this.name = name;
//         this.age = age;
//         this.experience = experience;
//         this.jobTitle = jobTitle;
//     }
// }
// class EmpTable {
//     constructor(employees) {            //передаем массив работников
//         this.employees = employees;
//     }
//     getHtml() {
//         document.write('<table>');
//         document.write('<tr>');
//         for (let keys in this.employees[0]) {    //печатаем заголовок таблицы через перебор циклом for in названий
//             document.write('<th>' + keys +'</th>');                            //свойств первого объекта в массиве
//         }
//         document.write('</tr>');                        //печатаем ячейки таблицы тем же способом
//         for (let i=0; i < employees.length; i++) {      //цикл, перебирающий объекты в массиве
//             document.write('<tr>');
//             for (let key in this.employees[i]) {        //цикл for in, перебирающий значения свойств объектов массива
//                 document.write('<td>' + this.employees[i][key] + '</td>');
//             }
//             document.write('</tr>');
//         }
//         document.write('</table>');
//     }
// }
// const employees = [new Employee('Ivanov', 'Ivan', 25, 5, 'Director'),
//                    new Employee('Petrov', 'Petr', 30, 10, 'Manager'),
//                    new Employee('Sidorov', 'Sidor', 22, 2, 'Trainee'),
//                    new Employee('Tikhonov', 'Tikhon', 45, 25,'Booker'),
//                    new Employee('Novikova', 'Marina', 39, 19, 'Vice-President')];
//
// const empTable = new EmpTable(employees);
// // empTable.getHtml();         //!!!нужно разкомментировать, чтобы посмотреть решение первой задачи!!!
// //----------------------------------------------------------------------------------------------------------------------
// // Задание 4
// // Реализовать класс StyledEmpTable, который наследуется от
// // класса EmpTable. Добавить метод getStyles(), который возвращает
// // строку со стилями для таблицы в тегах style. Переопределить
// // метод getHtml(), который добавляет стили к тому, что возвращает
// // метод getHtml() из родительского класса.
// // Создать объект класса StyledEmpTable и вывести на экран
// // результат работы метода getHtml().
//
// class StyledEmpTable extends EmpTable {
//     getStyles() {                                                  //добавляем свойства CSS для таблицы
//         let head = document.querySelector('head');         //находим тег head
//         let newItem = document.createElement('style');     //создаем тег style
//         newItem.innerHTML = '        table {\n' +                  //вводим содержание в тег style (свойства CSS)
//             '            border-collapse: collapse;\n' +
//             '        }\n' +
//             '        th, td {\n' +
//             '            width: 100px;\n' +
//             '            height: 30px;\n' +
//             '            border: 1px solid black;\n' +
//             '        }\n' +
//             '        th {\n' +
//             '            background: slategrey;\n' +
//             '        }';
//         head.appendChild(newItem);                                 //добавляем в head новый элемент
//     }
//     getHtml() {
//         super.getHtml();                                           //выполняем метод getHtml родительского класса
//         this.getStyles();                                          //добавляем к методу функционал
//     }
// }
// let styledEmpTable = new StyledEmpTable(employees);
// styledEmpTable.getHtml();
