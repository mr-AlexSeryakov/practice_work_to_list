# description
# song
# Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти песен
# группы Depeche Mode. В информацию о каждом треке входит название и продолжительность с
# точностью до долей минут:
# violator_songs = [
# ['World in My Eyes', 4.86],
# ['Sweetest Perfection', 4.43],
# ['Personal Jesus', 4.56],
# ['Halo', 4.9],
# ['Waiting for the Night', 6.07],
# ['Enjoy the Silence', 4.20],
# ['Policy of Truth', 4.76],
# ['Blue Dress', 4.29],
# ['Clean', 5.83]
# ]
# Из этого списка Ваня хочет выбрать N песен и добавить их в особый плейлист с другими треками.
# При этом ему важно, сколько времени в сумме эти N песен будут звучать.
# task
# Напишите программу, которая запрашивает у пользователя количество песен из списка и их
# названия, а на экран выводит общее время их звучания.
# Пример
# Сколько песен выбрать? 3
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean
# Общее время звучания песен — 14,93 минуты

violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]
]

try:
    quantity_songs = int(input('Сколько песен выбрать? '))
except ValueError:
    print('Ввод должен быть числовым')
else:
    total_minutes_songs = 0

    for number in range(quantity_songs):
        name_song = input(f'Название {number + 1}-й песни: ')
        for i_name in violator_songs:
            if name_song == i_name[0]:
                total_minutes_songs += i_name[1]
                break
        else:
            print('Песня не найдена!')

    if total_minutes_songs > 0:
        print(f'Общее время звучания песен — {round(total_minutes_songs, 2)} минуты')
    else:
        print('Нет добавленных песен')