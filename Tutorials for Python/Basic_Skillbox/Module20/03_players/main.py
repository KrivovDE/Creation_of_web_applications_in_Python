players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2),
}

# TODO здесь писать код

print(
    [
        (name[0], name[1], score[0], score[1], score[2])
        for name, score in players.items()
    ]
)

# зачтено
