# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

# =============================================================================

# Решение:

num = int(input("Введите сколько сгенерировать элементов в списке: "))
min_n = 1
max_n = 100


def get_random_el(start_data: int, min_el: int, max_el: int) -> int:
    el = 0

    if start_data < 0:
        return el

    import random

    el = random.randint(min_el, max_el)
    return el


list_n = [get_random_el(num, min_n, max_n) for i in range(num)]
list_new = [list_n[j] for j in range(1, len(list_n)) if list_n[j - 1] < list_n[j]]

print(list_n)
print(list_new)

# =============================================================================
