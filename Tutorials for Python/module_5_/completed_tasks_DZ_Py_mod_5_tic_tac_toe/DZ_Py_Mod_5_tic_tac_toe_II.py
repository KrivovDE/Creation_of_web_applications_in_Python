# Что такое крестики-нолики?
# Крестики-нолики на Python – одна из игр, в которые играют два игрока на квадратной сетке 3 x 3.
# Каждый игрок заселяет клетку в свои ходы, стараясь поставить три одинаковых метки по вертикали, горизонтали
# или диагонали. Первый игрок использует Крестик (X), а другой использует Ноль (O).
# Дизайн крестиков-ноликов
# Мы будем использовать командную строку, чтобы играть в крестики-нолики.
# Задача: если игроку нужно отметить определенный блок, он должен ввести соответствующую цифру, отображаемую в сетке.
# Например, мы хотели занять верхний правый блок, а затем нам нужно ввести цифру 3 в терминал.
# Хранение данных
# Принцип любой игры основан на механике игры. Поскольку мы создаем относительно простую и легкую игру,
# включенная в нее механика также проста.
# В любой момент времени требуются две важные части информации:
# Состояние сетки:
# мы должны создать структуру данных, которая будет содержать состояние каждой ячейки. Состояние может быть как занятым,
# так и вакантным.
# Ходы каждого игрока:
# каким-то образом требуется знание прошлых и настоящих ходов каждого игрока, то есть позиций, занятых ‘X’ и ‘O’.
# Проверка победы или ничьей
# После каждого хода нам нужно проверять, выиграл ли какой-либо игрок матч или матч был ничейным.

start_cells = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
results = [0, 0]


def print_rules():
    print('Правила: \n'
          '1.Первый игрок всегда играет за Х\n'
          '2.Второй за ○\n'
          '3.После окончания раунда игроки меняются автоматически\n')


def reg_player():
    p1 = input('Enter name of player 1: ')
    p2 = input('Enter name of player 2: ')
    return p1, p2


def print_field(cells):
    print('-' * 13, '\n',
          '| ', cells[0], ' | ', cells[1], ' | ', cells[2], ' |', '\n',
          '-' * 13, '\n',
          '| ', cells[3], ' | ', cells[4], ' | ', cells[5], ' |', '\n',
          '-' * 13, '\n',
          '| ', cells[6], ' | ', cells[7], ' | ', cells[8], ' |', '\n',
          '-' * 13, '\n', sep='')


def check_parity(num):
    return True if num % 2 == 0 else False


def check_current_player(step_even, pl1, pl2, r_num):
    if r_num % 2 != 0:
        return pl1 if step_even else pl2
    else:
        return pl2 if step_even else pl1


def input_step(step_even, player_name):
    if step_even:
        pos = input(f'{player_name}, enter field for X: ')
        sym_let = 'X'
    else:
        pos = input(f'{player_name}, enter field for ○: ')
        sym_let = '○'
    return pos, sym_let


def check_step(cells, elem):
    return True if elem in cells and elem != 'X' and elem != '○' else False


def change_field(cells, cell_num, symbol):
    ind_step = cells.index(cell_num)
    cells.remove(cell_num)
    cells.insert(ind_step, symbol)
    return cells


def check_victory(cells, counter):
    if counter < 4:
        return False
    vic_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for comb in vic_comb:
        if cells[comb[0]] + cells[comb[1]] + cells[comb[2]] == 'XXX':
            return True
        elif cells[comb[0]] + cells[comb[1]] + cells[comb[2]] == '○○○':
            return True
        elif counter == 8:
            return 'Draw'
    return False


def count_result(symbol, round_num):
    if round_num % 2 != 0:
        if symbol == 'X':
            results[0] += 1
        else:
            results[1] += 1
    else:
        if symbol == '○':
            results[0] += 1
        else:
            results[1] += 1


def print_result(pl1, pl2, res_arr):
    print(f'Current match score:\n'
          f'{pl1}: {res_arr[0]}  '
          f'{pl2}: {res_arr[1]}')


def func_game(field):
    print_rules()
    player1, player2 = reg_player()
    round_number = 1
    cont = 'Y'

    while cont == 'Y':
        cur_field = field.copy()
        print_field(cur_field)
        i = 0

        while i != 9:
            step_parity = check_parity(i)
            current_player = check_current_player(step_parity, player1, player2, round_number)
            step_pos, step_sym = input_step(step_parity, current_player)

            if check_step(cur_field, step_pos):
                cur_field = change_field(cur_field, step_pos, step_sym)
            else:
                print('Choose empty field, please!')
                continue

            print_field(cur_field)
            res = check_victory(cur_field, i)

            if res and step_sym == 'X':
                print(f'{current_player} win!!!')
                count_result(step_sym, round_number)
                break
            elif res and step_sym == '○':
                print(f'{current_player} win!!!')
                count_result(step_sym, round_number)
                break
            elif res == 'Draw':
                print('Draw!!!')
                break
            elif not res:
                i += 1

        print_result(player1, player2, results)
        round_number += 1
        cont = input('If You want to continue, press Y or any key for stop: ')

    print('Thank you for game!')


func_game(start_cells)

