# TODO здесь писать код
import os


def str_counter_gen():
    for i_file in os.listdir():
        if ".py" in i_file:
            counter = 0
            with open(i_file, encoding="utf-8") as file:
                for i_str in file:
                    if not (len(i_str) < 2 or '"""' in i_str or "#" in i_str):
                        counter += 1
                else:
                    yield counter


for i_sum in str_counter_gen():
    print(i_sum)

# зачтено
