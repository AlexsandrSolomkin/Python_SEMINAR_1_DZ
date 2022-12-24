# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

# ===========================================================

# Решение:

num = int(input("Введите количество элементов, которое будет в списке: "))


def GetListRandomElements(lengthList, minEl, maxEL):
    import random
    newList = []

    for i in range(lengthList):
        e = random.randint(minEl, maxEL)
        newList.append(e)

    return newList


def SumElementsListWithStep(listElements, start, step):
    sumEl = 0

    for i in range(start, len(listElements), step):
        sumEl += listElements[i]

    return sumEl


listNum = GetListRandomElements(num, 1, 10)
sumElementsNum = SumElementsListWithStep(listNum, 0, 2)

print(listNum, "\n", sumElementsNum)

# ===========================================================
