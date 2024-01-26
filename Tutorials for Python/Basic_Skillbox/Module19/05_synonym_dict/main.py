# TODO здесь писать код


def value_search(word, input_dict):
    for key, value in input_dict.items():
        if value == word:
            return key
    else:
        return False


num_pair = int(input("Введите количество пар слов: "))
syn_dict = {}

for i_num in range(num_pair):
    print(f"{i_num + 1}-я пара:", end=" ")
    new_word = input().split(" — ")
    syn_dict[new_word[0].capitalize()] = new_word[1].capitalize()

while True:
    searched_wd = input("Введите слово: ").capitalize()
    if searched_wd in syn_dict:
        print("Синоним:", syn_dict[searched_wd])
        break
    elif value_search(searched_wd, syn_dict):
        print("Синоним:", value_search(searched_wd, syn_dict))
        break
    else:
        print("Такого слова в словаре нет.")

# зачтено
