# TODO здесь писать код

num_orders = int(input("Введите количество заказов: "))
client_dict = {}

for i_num in range(num_orders):
    print(f"{i_num + 1}-й заказ:", end=" ")
    user_order = input().split(" ")
    if user_order[0] in client_dict:
        if user_order[1] in client_dict[user_order[0]]:
            client_dict[user_order[0]][user_order[1]] += int(user_order[2])
        else:
            client_dict[user_order[0]][user_order[1]] = int(user_order[2])
    else:
        client_dict[user_order[0]] = {user_order[1]: int(user_order[2])}

print()
for client in sorted(client_dict.keys()):
    print(f"{client}:")
    for pizza in sorted(client_dict[client].keys()):
        print(f"    {pizza}: {client_dict[client][pizza]}")

# зачтено
