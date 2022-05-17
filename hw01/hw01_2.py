def get_digit_sum(number):
    digits_sum = 0
    while number // 10 > 0:
        digits_sum += number % 10
        number = number // 10
    digits_sum += number
    return digits_sum


def get_sum_by_condition(numbers_list):
    sum_2_return = sum(num for num in numbers_list if get_digit_sum(num) % 7 == 0)
    return sum_2_return

# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень
# числа X):


init_list = [num ** 3 for num in range(1, 1000) if num % 2 != 0]
print(init_list)


# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!


sum_num = get_sum_by_condition(init_list)
print(f"Сумма чисел списка, сумма цифр которых делится нацело на 7 = {sum_num}")


# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.


init_list = [num + 17 for num in init_list]
print(init_list)
sum_num = get_sum_by_condition(init_list)
print(f"Сумма чисел списка, сумма цифр которых делится нацело на 7 = {sum_num}")

# c. * Решить задачу под пунктом b, не создавая новый список.
