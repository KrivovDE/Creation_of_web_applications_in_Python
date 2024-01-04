shop = [
    ["каретка", 1200],
    ["шатун", 1000],
    ["седло", 300],
    ["педаль", 100],
    ["седло", 1500],
    ["рама", 12000],
    ["обод", 2000],
    ["шатун", 200],
    ["седло", 2700],
]

# TODO здесь писать код


detail = input("Название детали: ")
amount = 0
common_cost = 0

for goods in shop:
    if goods[0] == detail:
        amount += 1
        common_cost += goods[1]
if amount != 0:
    print("Кол-во деталей —", amount)
    print("Общая стоимость —", common_cost)
else:
    print("Такого товара нет в списке :(")

# зачтено
