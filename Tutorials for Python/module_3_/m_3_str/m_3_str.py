# str1 = 'Hello '
# str2 = "world!"
# msg = str1+str2
# print(msg)
# # /////////////////////////////////
# one = 'ай'
# msg = one*20
# # print(msg)
# #
# N = len(msg)
# print(msg, N)
# /////////////////////////////////
# s = "abcdefg0123"
# print("abc" in s)
# print('0' in s)
# print('13' in s)

# /////////////////////////////////
# msg = "Hello World!"
# print(msg[6:11])
# print(msg[:5])
# print(msg[6:])
# print(msg[:])
#
# print(msg[::2])
# print(msg[:5:2])
# print(msg[6::2])
# print(msg[1:6:2])
# print(msg[::-1])
# /////////////////////////////////
# ПРАКТИКА
# a = input()
# b = input()
# c = (a + ' ') * 2
# d = (b + ' ') * 3
# print(c, d, sep='')
# ----------------------------
# st = input()
# print(st[0], st[-1], sep='')
# ----------------------------
# print(input()[1::2])
# ----------------------------
# a = input()
# b = input()
# print(b[:len(a):])
# /////////////////////////////////
# digs = "1, 2,3, 4,5,6"
#
# print(digs.replace(" ", "").split(","))

# fio = "Иванов     Иван Иванович"
# fio2 = ",".join(fio.split())
#
# print(fio2)
# /////////////////////////////////
# normalText = '''Python Arithmetic Operators:\n
#  Arithmetic operators are used to perform
#  mathematical operations like addition,
#  subtraction, multiplication and division.\n
#  \tThere are 7 arithmetic operators in Python:
#  \t\tAddition +\n
#  \t\tSubtraction -\n
#  \t\tDivision /\n
#  \t\tModulus %\n
#  \t\tExponentiation **\n
#  \t\tFloor division //\n'''
# #
# rawText = r'''Python Arithmetic Operators:\n
#  Arithmetic operators are used to perform
#  mathematical operations like addition,
#  subtraction, multiplication and division.\n
#  \tThere are 7 arithmetic operators in Python:
#  \t\tAddition +\n
#  \t\tSubtraction -\n
#  \t\tDivision /\n
#  \t\tModulus %\n
#  \t\tExponentiation **\n
#  \t\tFloor division //\n
# #  '''
# print(normalText)
# print(100*'-')
# print(rawText)
# /////////////////////////////////
# age = 33
# name = "Dmitrii"
# print("Меня зовут "+name+", мне "+str(age)+" и я люблю язык Python.")
# print(100*'-')
#
# msg = "Меня зовут {0}, мне {1} и я люблю язык Python.".format(name, age)
# print(msg)
# print(100*'-')
#
# msg_2 = "Меня зовут {fio}, мне {old} и я люблю язык Python.".format(fio=name, old=age)
# print(msg_2)
# # /////////////////////////////////
# age = 33
# name = "Dmitrii"
# msg = f"Меня зовут {name}, мне {age} и я люблю язык Python."
# print(msg)
# print(100*'-')
#
# print(f"Меня зовут {name.upper()}, мне {age-15} и я люблю язык Python.")
# /////////////////////////////////

# userLogin = "".join(random.sample(string.ascii_lowercase, 6))
# userPass = "".join(random.sample(string.ascii_letters + string.digits, 8))

# userLogin = random.sample(string.ascii_lowercase, 6)
# userPass = random.sample(string.ascii_letters + string.digits, 8)
#
# userLogin = ''.join(userLogin)
# userPass = ''.join(userPass)
#
# print("login:", userLogin)
# print("password:", userPass)
# /////////////////////////////////


# /////////////////////////////////

# a = 'abrakadabra'
#
# print(a.count(''))
