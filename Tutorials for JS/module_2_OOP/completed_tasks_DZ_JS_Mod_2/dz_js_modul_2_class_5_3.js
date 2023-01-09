/*Реализовать класс Employee, описывающий работника, и создать массив работников банка.
Реализовать класс EmpTable для генерации html кода таблицы
со списком работников банка.Массив работников необходимо
передавать через конструктор, а получать html код с помощью
метода getHtml().
Создать объект класса EmpTable и вывести на экран результат
работы метода getHtml()*/

class Employee {
    constructor(name, age, salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }
}
class EmpTable {
    constructor(employees) {
        this.employees = employees;
    }
    getHtml() {
        let result = '<table border="1"><tr><th>Name</th><th>Age</th><th>Salary</th></tr>';
        for (let i = 0; i < this.employees.length; i++) {
            result += `<tr><td>${this.employees[i].name}</td><td>${this.employees[i].age}</td><td>${this.employees[i].salary}</td></tr>`;
        }
        result += '</table>';
        return result;
    }
}
function test(){
let employees = [ new Employee('Ivan', 25, 1000), new Employee('Petr', 26, 2000), new Employee('Sidor', 27, 3000) ];
let table = new EmpTable(employees);
console.log(table.getHtml());
let element = document.createElement('div');
element.innerHTML = table.getHtml();
document.body.appendChild(element);
}
test();
