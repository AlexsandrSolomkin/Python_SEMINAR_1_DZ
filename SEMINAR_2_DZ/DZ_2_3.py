# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

# ===========================================================

# Решение:

num = int(input("Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n\nn: "))

def Formula(startNum, n):
    
    multipliList = []

    for i in range(startNum, n + 1):

        numN = (1 + 1/n) ** n
        multipliList.append(numN)
        
    return multipliList

def SumElementsList(elements):

    result = 0

    for i in range(len(elements)):

        result += elements(i)

    return result




# ===========================================================
