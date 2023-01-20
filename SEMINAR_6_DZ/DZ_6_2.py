# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

# in
# 424

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]

# =============================================================================

# Решение:

num_1, num_2 = 20, 21
min_n = 20
max_n = int(input("Введите диапозон от {} до N, \
    чтобы найти числа, кратные {} или {}".format(min_n, num_1, num_2)))


# def get_random_el(start_data: int, min_el: int, max_el: int) -> int:
#     el = 0

#     if start_data < 0:
#         return el

#     import random

#     el = random.randint(min_el, max_el)
#     return el


# list_n = [get_random_el(num, min_n, max_n) for i in range(num)]
# list_new = [list_n[j] for j in range(1, len(list_n)) if list_n[j - 1] < list_n[j]]

# print(list_n)
# print(list_new)

# =============================================================================
