# Реализовать  вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
sec_in_min = 60
sec_in_hour = sec_in_min * 60
sec_in_day = sec_in_hour * 24

sec_count_input = input("Введите количество секунд: ")
# a. до минуты: <s> сек;
print(f"a. Введено: {sec_count_input} секунд")
# b. до часа: <m> мин <s> сек;
sec_count = int(sec_count_input)
min_count = sec_count // sec_in_min
sec_count = sec_count - min_count * sec_in_min
print(f"b. Введено: {min_count} мин и {sec_count} секунд")
# c. до суток: <h> час <m> мин <s> сек;
sec_count = int(sec_count_input)
hour_count = sec_count // sec_in_hour
sec_count = sec_count - hour_count * sec_in_hour
min_count = sec_count // sec_in_min
sec_count = sec_count - min_count * sec_in_min
print(f"c. Введено: {hour_count} ч {min_count} мин и {sec_count} секунд")

# d. * в остальных случаях:  <d> дн <h> час <m> мин <s> сек
sec_count = int(sec_count_input)
day_count = sec_count // sec_in_day
sec_count = sec_count - day_count * sec_in_day
hour_count = sec_count // sec_in_hour
sec_count = sec_count - hour_count * sec_in_hour
min_count = sec_count // sec_in_min
sec_count = sec_count - min_count * sec_in_min
print(f"d. Введено: {day_count} дн {hour_count} ч {min_count} мин и {sec_count} секунд")
