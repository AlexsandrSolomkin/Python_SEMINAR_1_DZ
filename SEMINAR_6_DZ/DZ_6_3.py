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


def thesaurus(list_el: list) -> dict:
    names_dict = {}

    for i in sorted(list_el):
        # new_el_dict = {}
        key = i[0]
        # item = i

        if key not in names_dict:
            names_dict[key] = [i]
            # .update({key: i})
            # new_el_dict.update({key: i})
            # names_dict = dict(names_dict.items() + new_el_dict.items())
        else:
            names_dict[key] += [i]

    # for i in sorted(args):
    #     letter = i[0]
    #     if letter not in names_dict:
    #         names_dict[letter] = [i]
    #     else:
    #         names_dict[letter] += [i]

    return names_dict


new_list = input_str_in_list("exit")
new_args = thesaurus(new_list)

# print(new_list)
print(new_args)
# print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))

# =============================================================================
