/*Реализовать класс, описывающий простой маркер. В классе
должны быть следующие компоненты:
■ поле, которое хранит цвет маркера;
■ поле, которое хранит количество чернил в маркере (в процентах);
■ метод для печати (метод принимает строку и выводит
текст соответствующим цветом; текст выводится до тех
пор, пока в маркере есть чернила; один не пробельный
символ – это 0,5% чернил в маркере).
Реализовать класс, описывающий заправляющийся маркер,
унаследовав его от простого маркера и добавив метод для заправки
маркера.
Продемонстрировать работу написанных методов. */

class Marker {
    constructor(color, ink) {
        this.color = color;
        this.ink = ink;
    }
    print(text) {
        let textArr = text.split('');
        let result = '';
        for (let i = 0; i < textArr.length; i++) {
            if (textArr[i] == ' ') {
                result += textArr[i];
                continue;
            }
            if (this.ink > 0) {
                result += textArr[i];
                this.ink -= 0.5;
            }
        }
        console.log('%c' + result, 'color: ' + this.color);
    }
}
class RefillableMarker extends Marker {
    refill(ink) {
        this.ink += ink;
    }
}
function test_basic_marker()
{
    let marker = new Marker('red', 100);
    marker.print('Hello World');
    if (marker.ink != 95) {
        throw new Error('Test failed');
    }
}
function test_refillable_marker()
{
    let marker = new RefillableMarker('green', 100);
    marker.print('Hello World');
    marker.refill(10);
    if (marker.ink != 105) {
        throw new Error('Test failed');
    }
}
test_basic_marker();
test_refillable_marker();
