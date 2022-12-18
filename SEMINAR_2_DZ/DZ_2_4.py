# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# ===========================================================

# Решение:

num = int(input("Enter the value of N: "))
num1 = int(input("Position one: "))
num2 = int(input("Position two: "))


def СreatingNewList(startNum):

    newList = []
    endNum = startNum + 1
    startNum *= (-1)

    for i in range(startNum, endNum):

        newList.append(startNum)
        startNum += 1

    return newList


def Element_X_Element(newList, firstEl, secondEl):

    result = 0

    if firstEl > len(newList) or secondEl > len(newList):

        result = "There are no values for these indexes!"

    elif firstEl != 0 and secondEl != 0:

        firstEl -= 1
        secondEl -= 1
        result = newList[firstEl] * newList[secondEl]

    else:

        result = "Incorrect data entered"

    return result


print(СreatingNewList(num))
print(Element_X_Element(СreatingNewList(num), num1, num2))

# ===========================================================
