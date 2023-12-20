# TODO здесь писать код


skates = []
counter = 0

amount_skates = int(input("Кол-во коньков: "))

for i in range(amount_skates):
    print(f"Размер {i + 1}-й пары:", end=" ")
    size = int(input())
    skates.append(size)

amount_feet = int(input("\nКол-во человек: "))

for i in range(amount_feet):
    print(f"Размер ноги {i + 1}-го человека:", end=" ")
    foot_size = int(input())
    for i_skates in range(len(skates)):
        if skates[i_skates] == foot_size:
            counter += 1
            skates.remove(foot_size)
            break

print("Наибольшее кол-во людей, которые могут взять ролики:", counter)

# зачтено
