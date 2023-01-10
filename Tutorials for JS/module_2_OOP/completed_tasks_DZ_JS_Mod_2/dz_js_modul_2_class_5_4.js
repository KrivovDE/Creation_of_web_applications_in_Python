/*Реализовать класс StyledEmpTable, который наследуется от
класса EmpTable.
Добавить метод getStyles(), который возвращает
строку со стилями для таблицы в тегах style. Переопределить
метод getHtml(), который добавляет стили к тому, что возвращает
метод getHtml() из родительского класса.
Создать объект класса StyledEmpTable и вывести на экран
результат работы метода getHtml(). */

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
            result += `<tr><td>${this.employees[i].name}</td>
                           <td>${this.employees[i].age}</td>
                           <td>${this.employees[i].salary}</td>
                       </tr>`;
        }
        result += '</table>';
        return result;
    }
}
class StyledEmpTable extends EmpTable {
    getStyles() {
        return '<style>table {border-collapse: collapse;color:red;}th, td {border: 1px solid black;}</style>';
    }
    getHtml() {
        return this.getStyles() + super.getHtml();
    }
}
function test(){
    let employees = [ new Employee('Ivan', 25, 1000),
                      new Employee('Petr', 26, 2000),
                      new Employee('Sidor', 27, 3000) ];
    let table = new StyledEmpTable(employees);
    let element = document.createElement('div');
    element.innerHTML = table.getHtml();
    document.body.appendChild(element);
}
test();
