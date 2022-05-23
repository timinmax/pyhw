def check_int(item_to_check):
    try:
        int(item_to_check)
        return True
    except ValueError:
        return False


def format_int(item_2_format):
    # Эта функция под вопросом. Альтернативный вариант - приведение к int вставить внутрь функции replace
    # И вместо вызова функции format_int вставить эту "формулу"
    # КАК ЛУЧШЕ С Т.ЗРЕНИЯ BEST PRACTICE?
    int_value = int(item_2_format)
    return item_2_format.replace(f"{int_value}", f"{int_value:02d}")


init_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
digit_pos_list = [i for i, list_item in enumerate(init_list) if check_int(list_item)]

digit_pos_list.reverse()

for digit_pos in digit_pos_list:
    init_list[digit_pos] = format_int(init_list[digit_pos])
    init_list.insert(digit_pos + 1, '"')
    init_list.insert(digit_pos, '"')
# ВАРИАНТ 1
print(" ".join(init_list))

# ВАРИАНТ 2 - УБРАТЬ ЛИШНИЕ ПРОБЕЛЫ У КАВЫЧЕК
print(init_list)
init_list = [f"{list_item}" if list_item == '"' or check_int(list_item) else f" {list_item} " for list_item in init_list]
print(init_list)
print("".join(init_list).replace("  ", " ").strip())
