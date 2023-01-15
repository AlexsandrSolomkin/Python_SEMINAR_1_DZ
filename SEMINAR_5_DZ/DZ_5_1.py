# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

# =============================================================================

# Решение:


num_str = int(input("Number of words: "))
str_el = "абв"


def create_list_str(num_1: int, start_el_str: str) -> list:
    import random

    new_list = []
    start_el_list = list(start_el_str)

    for i in range(num_1):
        random.shuffle(start_el_list)
        new_el_shuffle = ''.join(start_el_list)
        new_list.append(new_el_shuffle)

    return new_list


list_str = create_list_str(num_str, str_el)

print(*list_str)

# =============================================================================
