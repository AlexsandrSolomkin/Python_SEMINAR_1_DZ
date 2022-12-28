# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

# =============================================================================

# Решение:

num = int(input("Enter a natural number: "))


def get_list_random_elements(length_list: int, min_el: int,
                             max_el: int) -> list:

    if length_list < 0:
        print("Negative value of the number of numbers!")
        return []

    import random
    new_list = []

    for i in range(length_list):
        e = random.randint(min_el, max_el)
        new_list.append(e)

    return new_list


def unique_elements_list(start_list: list) -> list:
    un_el_list = []
    count = 0

    for i in range(len(start_list)):
        un_el_list.append(start_list[i])

        for g in range(len(start_list)):

            if un_el_list[-1] == start_list[g]:
                count += 1
            
            if count == 2:
                del un_el_list[-1]
                break

        count = 0

    return un_el_list





start_list = get_list_random_elements(num, 1, num)
new_l = unique_elements_list(start_list)

print(start_list)
print(new_l)

# =============================================================================
