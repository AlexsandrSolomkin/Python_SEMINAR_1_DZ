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

# ===========================================================
