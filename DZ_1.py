# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

#===================================================================================

#Решение:

dayWeek = int(input("Какой день недели от 1 до 7 сейчас, для проверки выходного: "))

if 1 <= dayWeek <= 7:
    if dayWeek >= 6:
        print(dayWeek, "да", sep=" -> ")
    else:
        print(dayWeek, "нет", sep=" -> ")
else:
    print("такого дня недели нет")

#===================================================================================