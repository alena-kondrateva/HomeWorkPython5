# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять
# первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint

print('Правила игры:\n'
      'Всего конфет: 2021\n'
      'Первый ход определяется жеребьевкой\n'
      'За один ход можно взять не более 28 конфет\n'
      'Выигрывает тот, кто делает ход последним\n')

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
total_candy = 2021
max_step = 28
flag = False

whose_move = randint(1, 2)    # жеребьевка

if whose_move == 1:
    first, second = player1, player2
    print(f'Первым ходит {player1}')
else:
    first, second = player2, player1
    print(f'Первым ходит {player2}')

while total_candy != 0:
    if flag == False:
        step = int(input(f'Твой ход, {first}: '))
        if step == 0 or step > max_step:
            print('Слишком много, максимум 28 за один ход, попробуй еще раз: ')
        else:
            total_candy -= step
            if step < total_candy and total_candy > 0:
                total_candy -= step
                print(f'Осталось {total_candy} конфет')
                flag = True
            else:
                print('Конфеты кончились!')
                break

    if flag == True:
        step = int(input(f'Твой ход, {second}: '))
        if step == 0 or step > max_step:
            print('Слишком много, максимум 28 за один ход, попробуй еще раз: ')
        else:
            if step < total_candy and total_candy > 0:
                total_candy -= step
                print(f'Осталось {total_candy} конфет')
                flag = False
            else:
                print('Конфеты кончились!')
                break

if flag == True:
    print(f'Победил(-а) {second}!')
else:
    print(f'Победил(-а) {first}!')
