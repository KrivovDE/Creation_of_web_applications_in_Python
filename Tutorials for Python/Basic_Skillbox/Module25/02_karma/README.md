## Задача 02. Карма
### Что нужно сделать
Один буддист-программист решил создать свой симулятор жизни, 
в котором нужно набрать 500 очков кармы (это константа), чтобы достичь просветления. 

Каждый день вызывается специальная функция `one_day()`, 
которая возвращает количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:

- `KillError`;
- `DrunkError`;
- `CarCrashError`;
- `GluttonyError`;
- `DepressionError`.

Напишите такую программу. 
Функцию оберните в бесконечный цикл, 
выход из которого возможен только при накоплении кармы до уровня константы. 
Исключения обработайте и запишите в отдельный лог `karma.log`.
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
  - Для создания нового класса на основе уже существующего используется наследование.
- Сообщения о процессе получения результата осмыслены и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена, а не `a`, `b`, `c`, `d`.
- Классы и методы/функции имеют прописанную документацию.
- Названия используемых файлов соответствуют тем, которые написаны в задаче.
