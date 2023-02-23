# iter_1 = (x**2 for x in range(10))
# for i in iter_1:
#    print(i, end=" ")

# print(list(range(1000000000)))

# lst = (x for x in range(1000000000))
#
# for i in lst:
#     print(i, end="-")
#     if i > 1000000000:
#         break
#---------------------------------------------------

# def get_all_average(n):
#     avs = []
#     count = 0
#     res = 0
#     for i in range(1, n + 1):
#         count += 1
#         res += i
#         avs.append(res / count)
#
#     return avs
#
# print(get_all_average(100))
# print(get_all_average(100).__sizeof__())
#---------------------------------------------------


def f():
    return list(range(10))
print( f() )

def f():
    for x in range(10):
        yield x













