# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

# ===========================================================

# Решение:

num = float(input("Сумма всех цифр какого числа вам нужна?\nЧисло: "))


def SumNumFloat(numFloat):

    sumResult = 0

    if numFloat < 0:
        numFloat *= -1

    if numFloat % 1 != 0:

        while numFloat % 1 != 0:
            numFloat *= 10

    while numFloat != 0:

        number = numFloat % 10
        sumResult += number
        numFloat //= 10

    return sumResult


if num % 1 != 0:
    int(num)

print("{} -> {}".format(num, int(SumNumFloat(num))))

# ===========================================================
