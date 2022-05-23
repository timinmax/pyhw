init_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Вариант со списком
names_list = [str(mixed_string).split(" ")[-1].capitalize() for mixed_string in init_list]
for name in names_list:
    print(f"Привет, {name}!")
# Вариант "сразу" 
for mixed_string in init_list:
    name = str(mixed_string).split(" ")[-1].capitalize()
    print(f"Привет, {name}!")