## Задача 5. Словарь синонимов
### Что нужно сделать
Одна библиотека поручила вам написать программу для оцифровки словарей синонимов.
На вход в программу подаётся N пар слов. Каждое слово является синонимом к своему парному слову.

Реализуйте код, который составляет словарь синонимов (все слова в словаре различны),
затем запрашивает у пользователя слово и выводит на экран его синоним.
Обеспечьте контроль ввода: если такого слова нет, то выведите ошибку и запросите слово ещё раз.
При этом проверка не должна зависеть от регистра символов.

Пример:

```
Введите количество пар слов: 3
Первая пара: Привет — Здравствуйте
Вторая пара: Печально — Грустно
Третья пара: Весело — Радостно

Введите слово: интересно
Такого слова в словаре нет.
Введите слово: здравствуйте
Синоним: Привет
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода.
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
