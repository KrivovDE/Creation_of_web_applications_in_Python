# -----------------------------------TASK 1-----------------------------------
a, b, c = map(int, input().split())
if c > a < b:
    print(a)
elif c > b < a:
    print(b)
else:
    print(c)



# -----------------------------------TASK 2-----------------------------------
a = float(input())
if a <= 60:
    print(1)
elif 60 <= a <= 64:
    print(2)
elif 64 <= a <= 69:
    print(3)
else:
    print(4)


# -----------------------------------TASK 3-----------------------------------
a, b = float(input()), float(input())
d = a if a > b else b
print(d)

a = int(input())
msg = 'кратно 3' if a % 3 == 0 else 'не кратно 3'
print(msg)

a = int(input())
st = 'False' if a == 0 else 'True'
print(st)

# -----------------------------------TASK 4-----------------------------------
a = int(input())
c = 0 if a == 59 else a + 1
print(c)

# С использованием арифметических операторов:
print((a+1) % 60)


# -----------------------------------TASK 5-----------------------------------

# -----------------------------------TASK 6-----------------------------------
a,b,c,d = map(int, input().split())

if c+2 <= a and d+2 <= b or c+2 <= b and d+2 <= a:
    print('ДА')
else:
    print('НЕТ')


