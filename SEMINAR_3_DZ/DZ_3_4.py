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


def GetListRandomElements(lengthList: int, minEl: float, maxEL: float) -> list:
    import random
    newList = []

    for i in range(lengthList):
        e = random.uniform(minEl, maxEL)
        e = round(e, 2)
        newList.append(e)

    return newList


list_random_elements_float = GetListRandomElements(num, 0.00, 10.00)

print(list_random_elements_float)

# ============================================================================
