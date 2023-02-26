# # def is_positive(x):
# #     if x >= 0:
# #         return True
# #     else:
# #         return False
# def is_positive(x):
#     return x >= 0
#
# p = []
#
# for a in range(-5, 11):
#     if is_positive(a):
#         p.append(a)
#
# print(p)
#
# #
# def say_hello(msg, end="!"):
#     print(msg+end)
#
#
# say_hello("Hello")
# say_hello("Hello", "?")
#


# def say_hello(msg, end="!", sep=": "):
#     print("Message"+sep+msg+end)
#
# say_hello("Hello", sep=" ")
# #---------------------------------------------------
#
# def per_and_sq(w, h):
#     return 2*(w+h), w*h
#
# res = per_and_sq(2.3, 5)
# print(res)
# #
# per, sq = per_and_sq(2.3, 5)
# print(per, sq)
# #---------------------------------------------------
# #
# TYPE_FUNC = False
#
# if TYPE_FUNC:
#     def say_hello():
#         print("hello")
# else:
#     def say_hello(msg):
#         print(msg)
#
# say_hello('xcvbnm,')
# #---------------------------------------------------


# def max2(a, b):
#     if a > b:
#         return a
#     return b
#
#
# print(max2(2, -3))
#
#
# def max3(a, b, c):
#     return max2(a, max2(b, c))
#
#
# print(max3(2, -3, 5))
# #---------------------------------------------------
# Подвиг 1.

#
# def min_max_sum():
#     n = [int(x) for x in input().split()]
#     print(f'Min = {min(n)}, max = {max(n)}, sum = {sum(n)}')
#
# min_max_sum()

#---------------------------------------------------
# Подвиг 2.

# def perimetr(width, height):
#     p = (width + height) * 2
#     print(f"Периметр прямоугольника, равен {p}")
#
#
# width, height = map(int, input().split())
# perimetr(width, height)
# #---------------------------------------------------
# # Подвиг 3.
# def is_triangle(a, b, c):
#     return a < b + c and b < a + c and c < a + b
#
# #---------------------------------------------------
# # Подвиг 4.
#
#
# def is_odd(n):
#     return len(n) >= 6
#
#
# lst = [i for i in input().split() if is_odd(i)]
#
# print(*lst)

#---------------------------------------------------
# Подвиг 5.



a = 'dmitrii'
print(a)
print(a.capitalize())
print(a.isupper())









