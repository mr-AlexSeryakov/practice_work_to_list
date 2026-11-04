# description
# sorting
# Дан список из N чисел.
# task
# Напишите программу, которая сортирует элементы списка по
# возрастанию и выводит их на экран. Дополнительный список использовать нельзя.
# Также нельзя использовать готовые функции sorted/min/max и метод sort
# Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.

# Пример:
# Изначальный список: [1, 4, –3, 0, 10] 
# Отсортированный список: [–3, 0, 1, 4, 10]

number_list = [1, 4, -3, 0, 10]

print(f'Изначальный список: {number_list}')

for i_step in range(len(number_list) - 1):
    for i in range(len(number_list) - 1 - i_step):
        if number_list[i] > number_list[i + 1]:
            number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]

print(f'Отсортированный список: {number_list}')