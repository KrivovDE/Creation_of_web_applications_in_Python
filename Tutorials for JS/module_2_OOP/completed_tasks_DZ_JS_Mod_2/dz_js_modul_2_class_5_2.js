/*Реализуйте класс ExtendedDate, унаследовав его от стандартного класса Date и добавив следующие возможности:
■ метод для вывода даты (числа и месяца) текстом;
■ метод для проверки – это прошедшая дата или будущая
(если прошедшая, то метод возвращает false; если будущая или текущая, то true);
■ метод для проверки – високосный год или нет;
■ метод, возвращающий следующую дату.
Создайте объект класса ExtendedDate и выведите на экран
результаты работы новых методов.
 */

class ExtendedDate extends Date {
    constructor(year, month, day) {
        super(year, month, day);
    }
    printDate() {
        let months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'];
        return `${this.getDate()} ${months[this.getMonth()]}`;
    }
    isFuture() {
        let now = new Date();
        return this.getTime() >= now.getTime();
    }
    isLeapYear() {
        let year = this.getFullYear();
        return year % 4 === 0 && year % 100 !== 0 || year % 400 === 0;
    }
    nextDate() {
        let nextDay = new Date(this.getFullYear(), this.getMonth(), this.getDate() + 1);
        return nextDay;
    }
}
function test_1() {
    let date = new ExtendedDate(2020, 0, 30);
    console.log(date.printDate());
    console.log(date.isFuture());
    console.log(date.isLeapYear());
    console.log(date.nextDate());
}
test_1();
