# def is_positive(x):
#     if x >= 0:
#         return True
#     else:
#         return False
# # def is_positive(x):
# #     return x >= 0
#
#
# p = []
# for a in range(-5, 11):
#     if is_positive(a):
#         p.append(a)
#
# print(p)
#
#
# def say_hello(msg, end="!"):
#     print(msg+end)
#
# say_hello("Hello")
# say_hello("Hello", "?")
#
#
# def say_hello(msg, end="!", sep = ": "):
#     print("Message"+sep+msg+end)
#
# say_hello("Hello", sep=" ")
#---------------------------------------------------

def per_and_sq(w, h):
    return 2*(w+h), w*h

res = per_and_sq(2.3, 5)
print(res)

per, sq = per_and_sq(2.3, 5)
print(per, sq)
#---------------------------------------------------

TYPE_FUNC = True

if TYPE_FUNC:
    def say_hello():
        print("hello")
else:
    def say_hello(msg):
        print(msg)

say_hello()
#---------------------------------------------------
def max2(a, b):
    if a > b:
        return a
    return b






















