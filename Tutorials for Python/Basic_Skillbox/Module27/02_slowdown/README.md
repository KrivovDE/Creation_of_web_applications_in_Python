## Задача 2. Замедление кода
### Что нужно сделать
В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.

Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.
### Что оценивается
- Результат вычислений корректен.
- Сообщения о процессе получения результата осмыслены и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.
- Во всех декораторах используется `functools.wraps`.
