goods = {
    "Лампа": "12345",
    "Стол": "23456",
    "Диван": "34567",
    "Стул": "45678",
}

store = {
    "12345": [
        {"quantity": 27, "price": 42},
    ],
    "23456": [
        {"quantity": 22, "price": 510},
        {"quantity": 32, "price": 520},
    ],
    "34567": [
        {"quantity": 2, "price": 1200},
        {"quantity": 1, "price": 1150},
    ],
    "45678": [
        {"quantity": 50, "price": 100},
        {"quantity": 12, "price": 95},
        {"quantity": 43, "price": 97},
    ],
}

# TODO здесь писать код

for key, value in goods.items():
    total_cost = 0
    total_count = 0
    for thing in store[value]:
        total_count += thing["quantity"]
        total_cost += thing["quantity"] * thing["price"]
    print(f"{key} — {total_count} штук, стоимость {total_cost:,d} рубля")

# зачтено
