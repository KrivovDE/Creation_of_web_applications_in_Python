## Цели практической работы
- Отработать навык использования рекурсивного метода для решения задач, поработать со стеком вызовов.
- Научиться находить и исправлять возможные проблемы, которые могут возникнуть при передаче изменяемых типов данных в качестве параметров функции.
- Научиться отличать именованные аргументы и значения по умолчанию, уметь использовать их при написании функций, чтобы избежать повторов и писать более гибкий код.
- Отработать применение аргументов `*args` и `**kwargs` для решения задач.
## Что входит в работу
- Задача 1. Challenge 2.
- Задача 2. Поиск элемента 2.
- Задача 3. Глубокое копирование.
- Задача 4. Продвинутая функция sum.
- Задача 5. Список списков 2.
- Задача 6. Быстрая сортировка.
## Задача 1. Challenge 2
### Что нужно сделать
Вдохновившись мотивацией Антона, ваш друг тоже решил поставить перед собой задачу, но не сильно связанную с математикой, а именно: написать функцию, которая выводит все числа от 1 до num без использования циклов. Помогите другу реализовать такую функцию.

Пример работы программы:

```
Введите num: 10
1
2
3
4
5
6
7
8
9
10
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- input содержит корректные приглашения для ввода. 
- Основной функционал описан в отдельной функции(-ях).
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

## Задача 2. Поиск элемента 2
### Что нужно сделать
Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную глубину — уровень, до которого будет просматриваться структура. 

Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран. По умолчанию уровень не задан. В качестве примера можно использовать такой словарь:

```python
site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}
```
Пример 1:
```
Введите искомый ключ: head
Хотите ввести максимальную глубину? Y/N: n
Значение ключа: {'title': 'Мой сайт'}
```

Пример 2:
```
Введите искомый ключ: head
Хотите ввести максимальную глубину? Y/N: y
Введите максимальную глубину: 1
Значение ключа: None
```

### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- input содержит корректные приглашения для ввода. 
- Основной функционал описан в отдельной функции(-ях).
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

## Задача 3. Глубокое копирование
### Что нужно сделать
Вы сделали для заказчика структуру сайта по продаже телефонов:
```python
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам телефон недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': 'Продать'
		}
	}
}
```

Заказчик рассказал своим коллегам на рынке, и они тоже захотели такой сайт, только для своих товаров. Вы посчитали, что это лёгкая задача, и быстро принялись за работу. 

Напишите программу, которая запрашивает у клиента, сколько будет сайтов, а затем запрашивает название продукта и после каждого запроса выводит на экран активные сайты. 

Условия: структуру сайта нужно описать один раз, копипасту никто не любит.

Подсказка: используйте рекурсию.

Пример:
```
Сколько сайтов: 2
Введите название продукта для нового сайта: iPhone
Сайт для iPhone: 
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам iPhone недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': ‘Продать'
		}
	}
}

Введите название продукта для нового сайта: Samsung
Сайт для iPhone: 
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам iPhone недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': ‘Продать'
		}
	}
}

Сайт для Samsung: 
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам Samsung недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на Samsung',
			'div': 'Купить',
			'p': ‘Продать'
		}
	}
}
```

### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- input содержит корректные приглашения для ввода. 
- Основной функционал описан в отдельной функции(-ях).
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

## Задача 4. Продвинутая функция sum 
### Что нужно сделать
Как вы знаете, в Python есть полезная функция sum, которая умеет находить сумму элементов списков. Но иногда базовых возможностей функций не хватает для работы и приходится их усовершенствовать.

Напишите свою функцию sum, которая должна быть более гибкой, чем стандартная функция sum. Она должна уметь:

- складывать числа из списка списков;
- складывать числа из набора параметров.

Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

Примеры вызовов функции:
```
sum([[1, 2, [3]], [1], 3])
Ответ в консоли: 10

sum(1, 2, 3, 4, 5)
Ответ в консоли: 15
```

### Что оценивается
- Результат вычислений корректен.
- Весь функционал описан в отдельной функции.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

## Задача 5. Список списков 2
### Что нужно сделать
Вы уже работали с многомерными списками и решали задачи, где с помощью list comprehensions «выпрямляли» многомерные списки в один. Однако такой фокус не пройдёт, если у элементов разные уровни вложенности и этих списков неограниченное количество.

Дан такой список:

```python
nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
```

Напишите рекурсивную функцию, которая раскрывает все вложенные списки, то есть оставляет только внешний список. 

```
Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
```

Подсказка: можно возвращать списки и срезы списков.

### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельной функции(-ях).
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

## Задача 6. Быстрая сортировка
### Что нужно сделать
Реализуйте алгоритм быстрой сортировки (её называют сортировкой Хоара). 
За один шаг алгоритма выполните следующие действия:
1) Выберите один элемент списка (его иногда называют опорным элементом). Сделать это можно разными способами, но важно придерживаться 
одного принципа. В нашем случае опорным элементом всегда будет крайний правый (например, в списке [1, 2, 3] это 3).
2) Разбейте текущий список на три части: элементы меньше опорного, равные опорному и больше опорного. 
В списке [5, 8, 9, 4, 2, 9, 1, 8] опорным элементом будет число 8 (крайнее правое), а получить надо три списка:
- [5, 4, 2, 1];
- [8, 8];
- [9, 9].
3) Для списка с элементами меньше опорного ([5, 4, 2, 1]) и списка с элементами больше опорного ([9, 9]) выполните те же шаги заново — 
  запустите рекурсию.
- результат_1 = рекурсия([5, 4, 2, 1]).
- результат_2 = [8, 8].
- результат_3 = рекурсия([9, 9]).
4) Сложите результаты вызова рекурсий и получите отсортированный список:
отсортированный_список = результат_1 + результат_2 + результат_3.

#### Пример с разбором алгоритма выше (как сработала рекурсия)
С [9, 9] всё просто. Элементов меньше или больше опорного нет, поэтому рекурсия не пойдёт глубже, а вызов рекурсии по списку [9, 9] быстро завершится и вернёт этот же список (его и не нужно было сортировать).

С [5, 4, 2, 1] рекурсия пойдёт вглубь: 
- Первый шаг — [5, 4, 2, 1]:
  - опорным элементом выбирается число 1;
  - меньше 1 элементов нет (значит, рекурсия по ним продолжаться не будет);
  - помимо опорного элемента, других равных нет, получаем список [1];
  - больше 1 все остальные элементы [5, 4, 2] — с этим списком будет вызвана рекурсия.
- Второй шаг — [5, 4, 2]:
  - опорный элемент — 2;
  - меньше опорного — [];
  - равные опорному — [2];
  - больше опорного — [5, 4].
- Третий шаг — [5, 4]:
  - опорный элемент — 4;
  - меньше — [];
  - равны — [4];
  - больше — [5]. 
- Четвёртый шаг — [5]:
  - меньше — [];
  - равны — [5];
  - больше — [].

Тут вызовы завершаются, мы соединяем списки и возвращаем список [5] на уровень выше (в вызов с числами [5, 4]).

Там мы соединяем списки [] + [4] + [5] и получаем [4, 5]. Этот список возвращаем ещё на уровень выше (в вызов с числами [5, 4, 2]).


````
Опять складываем списки:
    [ ] + [2] + [4, 5] = [2, 4, 5].	

Этот список возвращаем в вызов на уровень выше (тот, который был запущен с [5, 4, 2, 1]).

Складываем списки:
    [ ] + [1] + [2, 4, 5] = [1, 2, 4, 5].

Возвращаем [1, 2, 4, 5] в самый первый вызов, где мы выполняли следующие вызовы:
результат_1 = рекурсия([5, 4, 2, 1]).
результат_2 = [8, 8].
результат_3 = рекурсия([9, 9]).

В итоге после выполнения всех рекурсий получаем:
результат_1 = [1, 2, 4, 5].
результат_2 = [8, 8].
результат_3 = [9, 9].

Складываем все списки: 
[1, 2, 4, 5] + [8, 8] + [9, 9] = [1, 2, 4, 5, 8, 8, 9, 9].

Этот полный список возвращается наружу — туда, где функция была вызвана изначально.
````

Напишите функцию, которая реализует этот алгоритм. Для удобства добавьте вспомогательную функцию, пусть она принимает на вход список, а возвращает три списка (с элементами меньше, равными и больше опорного).

Пример работы такой функции:

числа = [4, 9, 2, 7, 5]

вспомогательная_функция(числа) → [4, 2], [5], [9, 7]


Эту функцию можно будет использовать в основной-рекурсивной, чтобы код основной функции стал проще и понятнее.

### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельной функции(-ях).
- Переменные и функции имеют значащие имена, не только a, b, c, d.

## Что оценивается в практической работе
- Практическая работа сдана через GitLab.
- Структура папок и файлов репозитория соответствует репозиторию python_basic.
- Все задачи выполнены в соответствующих папках и файлах `main.py`.
- Описания коммитов осмысленны и понятны: `111`, `done`, `«я сделалъ»` — неверно; `added m15 homework`, `14.3 fix: variables naming` — верно.
- Использованы именованные индексы, не просто `i` (подробнее в видео 7.2).
- Использованы правильные числа, без дополнительных действий со стороны пользователя, без `+1` (подробнее об этом в видео 7.4).
- Правильно оформлен `input`, без пустого приветствия для ввода (подробнее об этом в видео 2.3).
- Переменные и функции имеют значащие имена, не только `a`, `b`, `c`, `d` (подробнее об этом в видео 2.3).
- Есть пробелы после запятых и при бинарных операциях.
- Нет пробелов после имён функций и перед скобками: `print ()`, `input ()` — неверно; `print()` — верно.
- Правильно оформлены блоки `if-elif-else`, циклы и функции; отступы одинаковы во всех блоках одного уровня.
- Все входные и выходные файлы называются так, как указано в заданиях.
- Основной функционал описывается в отдельной функции(-ях).
## Рекомендации
- Арифметические операции [PEP8](https://docs.python.org/3.7/reference/expressions.html#operator-precedence) остаются в приоритете. Необходимо вводить and, or.
- Руководство по стилю Python [PEP8 на английском языке](https://www.python.org/dev/peps/pep-0008/).
- Руководство по стилю Python [PEP8 на русском языке](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html).
- [Список встроенных функций](https://docs.python.org/3.7/library/functions.html).
## Как отправить работу на проверку
Чтобы выполнить практическую работу, обновите репозиторий python_basic на своём компьютере при помощи IDE PyCharm. Задачи находятся в папке Module21.

Сдайте практическую работу этого модуля через систему контроля версий Git сервиса Skillbox GitLab. В нижнем поле практической работы напишите «Сделано» и прикрепите ссылку на репозиторий. Ссылки на реплит оставлять не нужно.
