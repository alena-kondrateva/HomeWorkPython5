from random import randint

candies_total = 201
max_take = 28
player_1 = input('Введи свое имя: ')
player_2 = 'Бот'
players = [player_1, player_2]

lucky = randint(-1, 0)

print(f'Первым ходит: {players[lucky+1]}')

while candies_total > 0:
    lucky += 1

    if players[lucky % 2] == 'Бот':
        print(
            f'\nХодит {players[lucky%2]} \nОсталось {candies_total} конфет: ')

        if candies_total < 29:
            step = candies_total
        else:
            step = candies_total - ((candies_total//28)+1)

        while step > 28 or step < 1:
            step = randint(1, 28)

        print(step)
    else:
        step = int(
            input(f'Твой ход, {players[lucky%2]} \nОсталось {candies_total} конфет:  '))

        while step > max_take or step > candies_total:
            step = int(
                input(f'За один ход можно взять {max_take} конфет, попробуй еще раз: '))

    candies_total = candies_total - step

print(f'Победил(-а) {players[lucky%2]}')
