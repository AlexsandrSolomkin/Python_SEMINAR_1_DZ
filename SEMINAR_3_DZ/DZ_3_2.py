# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

# =====================================================================

# Решение:

num = int(input("Введите количество элементов, \
    которое будет в списке: "))


def get_list_random_elements(length_list: int, min_el: int, \
    max_el: int) -> list:

    if length_list < 0:
        print("Количество элементов списка \
            не может быть меньше нуля!!!")
        return []

    import random
    new_list = []

    for i in range(length_list):
        e = random.randint(min_el, max_el)
        new_list.append(e)

    return new_list

# def multiplying_num_from_list_from_ends(list_elements: list,):


# =====================================================================