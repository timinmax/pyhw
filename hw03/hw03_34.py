# * (вместо задачи 3) Написать функцию thesaurus_adv(),
#     принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
#     в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
#     предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.

def thesaurus_adv(*name_surname_pairs):
    thesaurus = {}
    for name_surname in name_surname_pairs:
        name_surname_list = name_surname.split()
        name_key = name_surname_list[0][0].upper()
        surname_key = name_surname_list[1][0].upper()
        thesaurus.setdefault(surname_key, {})
        thesaurus[surname_key].setdefault(name_key, [])
        thesaurus[surname_key][name_key].append(name_surname.title())

    sorted_thesaurus = {key: thesaurus[key] for key in sorted(thesaurus)}

    return sorted_thesaurus


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
