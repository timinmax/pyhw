def num_translate(en_num):
    # Написать функцию num_translate(), переводящую числительные от
    # 0 до 10 c английского на русский язык
    num_voc = {"ONE": "один",
               "TWO": "два",
               "THREE": "три",
               "FOUR": "четыре",
               "FIVE": "пять",
               "SIX": "шесть",
               "SEVEN": "семь",
               "EIGHT": "восемь",
               "NINE": "девять",
               "ZERO": "ноль"
               }
    ru_num = num_voc.get(en_num.upper())
    if not (ru_num is None) and en_num[0].isupper():
        # Доработать предыдущую функцию в num_translate_adv(): реализовать корректную
        # работу с числительными, начинающимися с заглавной буквы — результат тоже
        # должен быть с заглавной.
        return ru_num.capitalize()
    return ru_num


print(num_translate("ONeew"))
print(num_translate("ONe"))
print(num_translate("oNE"))