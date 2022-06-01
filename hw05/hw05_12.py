# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield
def odd_nums(right_border):
    for num in range(1, right_border + 1, 2):
        yield num


odd_yield_11 = odd_nums(11)
print(*odd_yield_11)

# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.
odd_no_yield_19 = (num for num in range(1, 19 + 1, 2))
print(*odd_no_yield_19)
