# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

#===================================================================================

#Решение:

quarter = int(input("Для какой четверти плоскости вам нужно узнать диапазон координат точек: "))

answer = "нет такой четверти"

if quarter == 1:
    answer = "x > 0, y > 0" 
elif quarter == 2:
    answer = "x < 0, y > 0"
elif quarter == 3:
    answer = "x < 0, y < 0"
elif quarter == 4:
    answer = "x > 0, y < 0"

print(quarter, "->", answer)

#===================================================================================
