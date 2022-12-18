# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

# ===========================================================

# Решение:

num = int(input(
    "Введите число, которое будет максимальным в списке, который вы хотите перетосовать\nЧисло: "))


def СreatingNewList(startNum):

    newList = []
    endNum = startNum + 1

    for i in range(endNum):

        newList.append(i)

    return newList


startNumList = СreatingNewList(num)
print(startNumList)


def ShufflingListItems(startList):

    import random

    newShuffingList = []
    maxIndexList = len(startList) - 1

    for i in range(maxIndexList + 1):

        e = random.randint(0, maxIndexList)
        maxIndexList -= 1
        numEl = startList.pop(e)
        newShuffingList.append(numEl)

    return newShuffingList


shuffingStartNumList = ShufflingListItems(startNumList)
print(shuffingStartNumList)

# ===========================================================
