# s = 0
# i = 1
#
# while i <= 1000:
#     s += 1/i
#     i += 1
# print(s)


z = 0
v = 10

while v < 100:
    if v == 0:
        break
    z += 1/v
    v = v + 1
else:
    print("Сумма вычислена корретно")
print(z)

