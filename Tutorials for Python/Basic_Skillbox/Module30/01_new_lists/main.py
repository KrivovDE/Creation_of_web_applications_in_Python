# TODO здесь писать код


from functools import reduce

floats: list[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: list[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: list[int] = [22, 33, 10, 6894, 11, 2, 1]

cubes_floats = list(map(lambda x: round(x**3, 3), floats))
longest_names = list(filter(lambda x: len(x) >= 5, names))
multiplex = reduce(lambda x, y: x * y, numbers)

print(cubes_floats, longest_names, multiplex, sep="\n")

# зачтено
