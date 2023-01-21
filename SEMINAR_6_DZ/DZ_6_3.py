# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

# =============================================================================

# Решение:

def input_str_in_list(stop: str) -> list:
    list_data = []
    el = ""

    while True:
        el = input(
            "Enter the data for the list, to exit, enter '{}': ".format(stop))
        if el == stop:
            return list_data
        else:
            list_data.append(el)


# def thesaurus(*args):
#     names_dict = {}
#     for i in sorted(args):
#         letter = i[0]
#         if letter not in names_dict:
#             names_dict[letter] = [i]
#         else:
#             names_dict[letter] += [i]

#     return names_dict


new_list = input_str_in_list("exit")

print(new_list)
# print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))

# =============================================================================
