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
    new_element = 0

    for i in range(count - 1):
        new_element = fibonacci_list[i] + fibonacci_list[i + 1]
        fibonacci_list.append(new_element)

    return fibonacci_list


def negafibonacci(fib_list: list) -> list:
    negafibonacci_list = list(reversed(fib_list))
    length_list_nf = len(negafibonacci_list)

    if length_list_nf % 2 != 0:
        for i in range(0, length_list_nf - 1, 2):
            negafibonacci_list[i] *= (-1)
    else:
        for i in range(1, length_list_nf - 1, 2):
            negafibonacci_list[i] *= (-1)

    for g in range(1, len(fib_list)):
        negafibonacci_list.append(fib_list[g])

    return negafibonacci_list


f_list = fibonacci(num)
negafib_list = negafibonacci(f_list)

print(f_list)
print(negafib_list)


# ============================================================================
