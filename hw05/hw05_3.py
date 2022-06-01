# Есть два списка
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В'
     # , '8Б', '10А', '10Б', '9А'
]

# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None)
zipped_gen = ((tutor, klasses[tutors.index(tutor)] if tutors.index(tutor) < len(klasses) else None) for tutor in tutors)

# Доказать, что вы создали именно генератор.
print(zipped_gen)
# <generator object <genexpr> at 0x00000183E3036570>

# Проверить его работу вплоть до истощения
print(*zipped_gen)
# ('Иван', '9А') ('Анастасия', '7В') ('Петр', '9Б') ('Сергей', '9В') ('Дмитрий', None) ('Борис', None) ('Елена', None)
