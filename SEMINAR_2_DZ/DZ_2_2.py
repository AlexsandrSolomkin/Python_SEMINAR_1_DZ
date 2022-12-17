# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

# ===========================================================

# Решение:

num = int(input("Введите число N для составления списка состоящего из элементов от 1 до N\nЧисло: "))


def СreatingMultiplicationList(startNum, number):

    multipliList = []

    for i in range(startNum, number + 1):
        startNum *= i
        multipliList.append(startNum)
        

    return multipliList


print("{} -> {}".format(num, СreatingMultiplicationList(1, num)))

# ===========================================================
