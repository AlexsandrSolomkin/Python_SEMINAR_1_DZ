# ** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

# ============================================================================

# Решение:

num = int(input("Шаги в каждую сторону для Негафибоначчи: "))

def fibonacci(count: int) -> list:
    fibonacci_list = [0, 1]
    # second_index = 1
    new_element = 0

    for i in range(count - 1):
        new_element = fibonacci_list[i] + fibonacci_list[i + 1]
        fibonacci_list.append(new_element)

    return fibonacci_list


# def negafibonacci(fib_list: list) -> list:
#     negafibonacci_list = []

f_list = fibonacci(num)

print(f_list)



# ============================================================================
