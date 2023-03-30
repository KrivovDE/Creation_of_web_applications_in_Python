

# def fuu(msg, _end='!', _sep=':'):
#     print(_sep+_end+msg)
#
# fuu('Hello')
# fuu('Hello', '?', '&&&')
# fuu('Какой то текст в msg', _sep='*****', _end='')

# #
# def get_sqr(w, h, fg=0):
#     return 2 * (w+h) + fg
#
# p = get_sqr(10, 20, 100)
# print(p)

# def is_positive(x):
#     if x >= 0:
#         return True
#     else:
#         return False
#
# def is_positive(x):
#     return x >= 0
#
# p = []
#
# for a in range(-588, 11):
#     if is_positive(a):
#         p.append(a)
#
# print(p)

# #
# def say_hello(msg, end="!"):
#     print(msg+end)
#
#
# say_hello("Hello", )
# say_hello("Hello", "?")


# def say_hello(msg, end="!", sep=": "):
#     print("Message"+sep+msg+end)
#
# say_hello("Hello", sep=" ")
# #---------------------------------------------------
#
def per_and_sq(w, h):
    return 2*(w+h), w*h


# res = per_and_sq(2.3, 5)
# print(res[0], res[1])

# per, sq = per_and_sq(2.3, 5)
# print(per, sq)
# #---------------------------------------------------


# TYPE_FUNC = True
#
# if TYPE_FUNC:
#     def say_hello(z):
#         print("hello")
# else:
#     def say_hello(msg):
#         print(msg)
#
# say_hello(False)
# #---------------------------------------------------
# #
def max2(a, b):
    if a > b:
        return a
    return b

# print(max2(2, -3))
#
#
# def max3(a, b, c):
#     return max2(a, max2(b, c))
# #
# print(max3(2, -3, 5))

 #---------------------------------------------------
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
# print(is_triangle(1,2,3))
# print(is_triangle(12,2,14))
# print(is_triangle(8,8,8))
# #---------------------------------------------------
# # Подвиг 4.
#5
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



# a = 'dmitrii'
# print(a)
# print(a.capitalize())
# print(a.isupper())









