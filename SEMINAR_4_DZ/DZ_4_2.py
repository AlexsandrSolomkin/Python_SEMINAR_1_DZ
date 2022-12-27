# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

# =============================================================================

# Решение:

num = int(input("Enter a natural number: "))

def prime_factors(start_num: int) -> list:
    list_p_f = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, \
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result_list = []

    for i in range(len(list_p_f)):

        while start_num % list_p_f[i] == 0:
            if start_num % list_p_f[i] == 0:
                result_list.append(list_p_f[i])
                start_num /= list_p_f[i]
            else:
                continue
        
        if start_num == 1:
            break

    return result_list


new_list = prime_factors(num)

print(new_list)


# =============================================================================
