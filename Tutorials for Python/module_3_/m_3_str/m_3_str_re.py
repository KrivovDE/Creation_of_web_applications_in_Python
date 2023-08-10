import re

#
# text = "(Eда), беду, победа"


# match = re.findall(r"\(Eда\)", text)
# print(match)
# # /////////////////////////////////
# match = re.findall(r"[еЕ]д[ау]", text)
# print(match)
# /////////////////////////////////

text = "Google, Gooogle, Goooooogle"
# match = re.findall(r"o{2,5}", text)
# print(match)
#
# match = re.findall(r"o{2,5}?", text)
# print(match)
#
phone = "81234567890"
match = re.findall(r"8\d{10}", phone)
print(type(match))
# /////////////////////////////////
