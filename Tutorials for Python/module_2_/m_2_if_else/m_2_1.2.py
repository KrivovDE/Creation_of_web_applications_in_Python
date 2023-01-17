x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
grade = int(input('Введите вашу отметку по 100-балльной системе: '))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70:
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
grade = int(input('Введите вашу отметку: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||

x, y = 25, 50
big = x if x < y else y

num1 = 5
num2 = 10

print("num1 больше, чем num2" if num1 > num2 else "num1 меньше, чем num2" if num1 == num2 else "Оба числа не равны")
