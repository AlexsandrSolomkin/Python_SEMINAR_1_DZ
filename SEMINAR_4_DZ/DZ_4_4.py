# * 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

# =============================================================================

# Решение:


def get_list_random_elements(length_list: int, min_el: int,
                             max_el: int) -> list:

    if length_list < 0:
        # print("Negative value of the number of numbers!")
        return []

    import random
    new_list = []

    for i in range(length_list):
        e = random.randint(min_el, max_el)
        new_list.append(e)

    return new_list


def add_data(num: int, list_n: list, name_file: str) -> str:
    import random

    with open(name_file, "a", encoding="utf-8") as my_f:

        for i in range(-num, 0):

            plus_minus = random.randint(0, 1)

            if list_n[i] > 0:
                my_f.write(F"{list_n[i]}*x^{num}")

                if plus_minus != 0:
                    my_f.write(f" + ")
                else:
                    my_f.write(f" - ")

            num -= 1

        last_el = random.randint(1, 10)
        my_f.write(f"{last_el} = 0\n")


num_k = int(input("k: "))

list_k = get_list_random_elements(num_k, 0, 10)
add_new_data = add_data(num_k, list_k, "poly.txt")

print(list_k)

# =============================================================================
