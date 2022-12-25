# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

# ============================================================================

# Решение:

num = int(input("Сколько произвольных вещественных чисел сгенерировать: "))


def get_list_random_elements(length_list: int, min_el: float, max_el: float) -> list:
    import random
    new_list = []

    for i in range(length_list):
        e = random.uniform(min_el, max_el)
        e = round(e, 2)
        new_list.append(e)

    return new_list


def list_fractional_part(list_elements: list) -> list:
    new_list_elements = []
    new_element = float(0)

    for g in range(len(list_elements)):
        new_element = list_elements[g] % 1
        new_element = round(new_element, 2)
        new_list_elements.append(new_element)

    return new_list_elements

list_random_elements_float = get_list_random_elements(num, 0.00, 10.00)
list_float_elements = list_fractional_part(list_random_elements_float)

print(list_random_elements_float, "\n", list_float_elements, sep="")


# ============================================================================
