# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

# ============================================================================

# Решение:

num1 = int(input("Какое целое преобразовать из десятичного числа в двоичное: "))


def number_conversion(start_num: int) -> int:
    result = 1
    num_list = []

    if start_num == 0:
        result = 0
    elif start_num == 1:
        return result
    else:
        while start_num > 0:
            if start_num % 2 == 0:
                start_num /= 2
                num_list.append(0)
            else:
                num_list.append(int(start_num % 2))
                start_num = int(start_num / 2)

        start_index_rigth = -2

        for i in range(len(num_list) - 1):
            if num_list[start_index_rigth] == 1:
                result = result * 10 + 1
                start_index_rigth -= 1
            else:
                result = result * 10
                start_index_rigth -= 1

    return result


print(number_conversion(num1))


# ============================================================================
