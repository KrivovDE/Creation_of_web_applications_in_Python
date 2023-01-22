x = input("x: ")
y = input("y: ")

x = int(x)
y = int(y)

res = x / y
print(res)

try:
    x = int(x)
    y = int(y)

    res = x / y
except ZeroDivisionError:
    res = "деление на ноль"
print(res)
# # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||


# except (ZeroDivisionError, ValueError):
#     res = "деление на ноль или нечисловое значение"
#
# except ZeroDivisionError:
#     res = "деление на ноль"
# except ValueError:
#     res = "одно из введенных значений не число"
# # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def getValues():
#     x = input("x: ")
#     y = input("y: ")
#     try:
#         x = int(x)
#         y = int(y)
#         return x, y
#     except ValueError as v:
#         print(v)
#         return 0, 0
#     finally:
#         print("finally выполняется до return")
#
#
# x, y = getValues()
# print(x, y)
# # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||

x = input("x: ")
y = input("y: ")
try:
    x = int(x)
    y = int(y)

    res = x / y
except:
    print("Произошло исключение")
else:
    print("Исключений не произошло")
finally:
    print("Блок finally выполняется всегда")

print(res)
# # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
print("Куда ты скачешь, гордый конь,")
print("И где опустишь ты копыта?")
print("О мощный властелин судьбы!")
1/0
print("Не так ли ты над самой бездной")
print("На высоте, уздой железной")
print("Россию поднял на дыбы?")

