import random


board_list = []


def create_initial_state(user_input):
    global board_list
    board_list = [[(' ' if user_input[3 * i + j] == '_' else user_input[3 * i + j])
                   for j in range(3)] for i in range(3)]


def print_board():
    board = board_list
    print('-' * 9)
    for line in board:
        print(f"| {' '.join(line)} |")
    print('-' * 9)


def x_input():
    while True:
        x_user_input = input('Enter the coordinates: ')
        try:
            x, y = x_user_input.split()
            x = int(x)
            y = int(y)
        except ValueError:
            print('You should enter numbers!')
        else:
            x, y = x_user_input.split()
            x = int(x)
            y = int(y)
            if x > 3 or y > 3:
                print('Coordinates should be from 1 to 3!')
            elif board_list[x - 1][y - 1] != ' ':
                print('This cell is occupied! Choose another one!')
            else:
                board_list[x - 1][y - 1] = 'X'
                break


def o_input():
    while True:
        o_user_input = input('Enter the coordinates: ')
        try:
            x, y = o_user_input.split()
            x = int(x)
            y = int(y)
        except ValueError:
            print('You should enter numbers!')
        else:
            x, y = o_user_input.split()
            x = int(x)
            y = int(y)
            if x > 3 or y > 3:
                print('Coordinates should be from 1 to 3!')
            elif board_list[x - 1][y - 1] != ' ':
                print('This cell is occupied! Choose another one!')
            else:
                board_list[x - 1][y - 1] = 'O'
                break


def check_winner():
    winning_patterns = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for pattern in winning_patterns:
        if all(board_list[row][col] == 'X' for row, col in pattern):
            return 'X'

    for pattern in winning_patterns:
        if all(board_list[row][col] == 'O' for row, col in pattern):
            return 'Y'

    return 'D'


def count_filled_column():
    count_non_space = 0
    for row in board_list:
        for cell in row:
            if cell != ' ':
                count_non_space += 1
    return count_non_space


def print_winner():
    winner = check_winner()
    if winner == 'X':
        return 'X wins'
    elif winner == 'Y':
        return 'O wins'
    elif count_filled_column() == 9 and winner == 'D':
        return 'Draw'
    elif count_filled_column() < 9 and winner == 'D':
        return 'Game not finished'


def easy_ai_play_x():
    available_field = []
    for i, row in enumerate(board_list):
        for j, cell in enumerate(row):
            if cell == ' ':
                available_field.append((i, j))
    random_move = random.choice(available_field)
    x, y = random_move
    board_list[x][y] = 'X'


def easy_ai_play_o():
    available_field = []
    for i, row in enumerate(board_list):
        for j, cell in enumerate(row):
            if cell == ' ':
                available_field.append((i, j))
    random_move = random.choice(available_field)
    x, y = random_move
    board_list[x][y] = 'O'


def medium_ai_play_x():
    winning_patterns = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    def check_pattern(pattern, player):
        return sum(1 for (x, y) in pattern if board_list[x][y] == player)

    for pattern in winning_patterns:
        if check_pattern(pattern, 'X') == 2 and check_pattern(pattern, ' ') == 1:
            for (x, y) in pattern:
                if board_list[x][y] == ' ':
                    board_list[x][y] = 'X'
                    return

    for pattern in winning_patterns:
        if check_pattern(pattern, 'O') == 2 and check_pattern(pattern, ' ') == 1:
            for (x, y) in pattern:
                if board_list[x][y] == ' ':
                    board_list[x][y] = 'X'
                    return

    empty_spots = [(x, y) for x in range(3) for y in range(3) if board_list[x][y] == ' ']
    if empty_spots:
        x, y = random.choice(empty_spots)
        board_list[x][y] = 'X'


def medium_ai_play_o():
    winning_patterns = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    def check_pattern(pattern, player):
        return sum(1 for (x, y) in pattern if board_list[x][y] == player)

    for pattern in winning_patterns:
        if check_pattern(pattern, 'O') == 2 and check_pattern(pattern, ' ') == 1:
            for (x, y) in pattern:
                if board_list[x][y] == ' ':
                    board_list[x][y] = 'O'
                    return

    for pattern in winning_patterns:
        if check_pattern(pattern, 'X') == 2 and check_pattern(pattern, ' ') == 1:
            for (x, y) in pattern:
                if board_list[x][y] == ' ':
                    board_list[x][y] = 'O'
                    return

    empty_spots = [(x, y) for x in range(3) for y in range(3) if board_list[x][y] == ' ']
    if empty_spots:
        x, y = random.choice(empty_spots)
        board_list[x][y] = 'O'


def menu_loop():
    menu_input = str(input('Input command: '))
    if menu_input == 'exit':
        exit()
    else:
        try:
            menu_command, x, o = menu_input.split()
        except ValueError:
            print('Bad parameters!')
            menu_loop()
        else:
            menu_command, x, o = menu_input.split()
            return start_game(x, o)


def start_game(x, o):
    create_initial_state('_________')
    print_board()
    while True:
        if x == 'easy' and o == 'easy':
            easy_ai_play_x()
            print('Making move level "easy"')
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()
            easy_ai_play_o()
            print('Making move level "easy"')
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()

        if x == 'user' and o == 'user':
            x_input()
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()
            o_input()
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()

        if x == 'easy' and o == 'user':
            easy_ai_play_x()
            print('Making move level "easy"')
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()
            o_input()
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()

        if x == 'user' and o == 'easy':
            x_input()
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()
            easy_ai_play_o()
            print('Making move level "easy"')
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()

        if x == 'medium' and o == 'user':
            medium_ai_play_x()
            print('Making move level "medium"')
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()
            o_input()
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()

        if x == 'user' and o == 'medium':
            x_input()
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()
            medium_ai_play_o()
            print('Making move level "medium"')
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()

        if x == 'medium' and o == 'medium':
            medium_ai_play_x()
            print('Making move level "medium"')
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()
            medium_ai_play_o()
            print('Making move level "medium"')
            print_board()
            if print_winner() != 'Game not finished':
                print(print_winner())
                print()
                menu_loop()


menu_loop()