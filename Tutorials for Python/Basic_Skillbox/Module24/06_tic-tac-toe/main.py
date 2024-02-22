# TODO здесь писать код

from random import randint


class Cell:
    def __init__(self, x: int, y: int, index: int, busy: str = "_"):
        self.index = x
        self.ordinate = y
        self.index = index
        self.busy = busy


class Board:
    def __init__(self, x_size: int = 3, y_size: int = 3):
        self.board_list = [
            [Cell(column, row, column + row * x_size) for column in range(x_size)]
            for row in range(y_size)
        ]

    def show(self):
        for y_index, i_line in enumerate(self.board_list):
            for x_index, i_column in enumerate(i_line):
                if i_column.busy == "_":
                    print(i_column.index + 1, end="\t")
                else:
                    print(i_column.busy, end="\t")
            print()
        print()

    def clear(self):
        for i_line in self.board_list:
            for i_column in i_line:
                i_column.busy = "_"


class Player:
    win_counter = 0

    def __init__(self, name: str, board: Board, sign: str = None):
        self.name = name
        self.board = board.board_list
        self.sign = sign

    def move_check(self, index: int):
        try:
            index = int(index) - 1

            if isinstance(index, int) and index < (
                len(self.board[0]) * len(self.board)
            ):
                x = index % len(self.board[0])
                y = int(index // len(self.board))
                return False if self.board[y][x].busy == "_" else True
            else:
                return True
        except ValueError:
            return True

    def move(self, index: int):
        index = int(index) - 1
        x = index % len(self.board[0])
        y = int(index // len(self.board))
        self.board[y][x].busy = self.sign


class Game:

    move_counter = 0

    def __init__(self, pl_1: Player, pl_2: Player, board: Board, status: str = "new"):
        self.player_1 = pl_1
        self.player_2 = pl_2
        self.board_list = board.board_list
        self.board = board
        self.status = status

    def make_move(self, player):
        self.board.show()
        move = input("Выберете ячейку: ")

        while player.move_check(move):
            move = input("Введены некорректные данные, повторите ввод: ")
        else:
            self.move_counter += 1
            player.move(move)

    def win_check(self, player):

        if self.move_counter < 5:
            return False
        else:
            combination = [
                "".join(
                    [
                        self.board_list[y][x].busy
                        for x in range(
                            len(self.board_list[y]),
                        )
                    ]
                )
                for y in range(len(self.board_list))
            ]
            combination.extend(
                [
                    "".join(
                        [
                            self.board_list[x][y].busy
                            for x in range(len(self.board_list[y]))
                        ]
                    )
                    for y in range(len(self.board_list))
                ]
            )
            combination.extend(
                [
                    "".join(
                        [
                            self.board_list[0][0].busy,
                            self.board_list[1][1].busy,
                            self.board_list[2][2].busy,
                        ]
                    ),
                    "".join(
                        [
                            self.board_list[2][0].busy,
                            self.board_list[1][1].busy,
                            self.board_list[0][2].busy,
                        ]
                    ),
                ]
            )

            for i_comb in combination:
                if i_comb == 3 * player.sign:
                    return True
            else:
                return False

    def lets_play(self, active_player):

        for _ in range(9):
            print(
                "Ходит -",
                active_player.name,
                "ставит -",
                active_player.sign,
            )
            self.make_move(active_player)
            if self.win_check(active_player):
                print(f"Игрок {active_player.name} победил")
                active_player.win_counter += 1
                print(
                    "Счёт - {} : {}\n".format(
                        self.player_1.win_counter,
                        self.player_2.win_counter,
                    ),
                )
                break
            else:
                active_player = (
                    self.player_2 if active_player == self.player_1 else self.player_1
                )
        else:
            print("Ничья")
            # print('Счёт - ', self.player_1.win_counter, ':',
            #       self.player_2.win_counter, '\n')
            print(
                "Счёт - {} : {}\n".format(
                    self.player_1.win_counter,
                    self.player_2.win_counter,
                ),
            )


again = True

board_1 = Board()
man_1 = Player(input("Введите имя первого Игрока: "), board_1, "x")
man_2 = Player(input("Введите имя второго Игрока: "), board_1, "o")

game_1 = Game(man_1, man_2, board_1)
active_player = man_1 if randint(0, 1) == 0 else man_2
while again:
    game_1.lets_play(active_player)
    game_1.board.clear()
    active_player = man_2 if active_player == man_1 else man_1
    again = (
        True
        if input("Для продолжения нажмите - 1, другая клавиша - Выход: ") == "1"
        else False
    )
else:
    print("End Game")
