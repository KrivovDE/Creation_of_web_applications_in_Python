# TODO здесь писать код

import re

text = ["9999999999", "999999-999", "99999x9999"]

for i_text in text:
    if re.fullmatch(r"[89]\d{9}", i_text) is None:
        print(i_text, "- не подходит")
    else:
        print(i_text, "- всё в порядке")
