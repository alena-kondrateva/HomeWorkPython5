board = list(range(1, 10))
wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
              (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|',
              board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-'*13)


def user_input(playar_token):
    while True:
        value = input('Куда поставить ' + playar_token + ': ')
        if not (value in '123456789'):
            print('Неправильно введенное значение.\n'
                  'Введите значение от 1 до 9: ')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Эта клетка занята. Выбери другую.')
            continue
        board[value - 1] = playar_token
        break


def chek_win():
    for each in wins_coord:
        if board[each[0] - 1] == board[each[1] - 1] == board[each[2] - 1]:
            return board[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            user_input('X')
        else:
            user_input('O')
        if counter > 3:
            win = chek_win()
            if win:
                draw_board()
                print(f'Победитель - {win}')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Победителя нет')
            break


main()
