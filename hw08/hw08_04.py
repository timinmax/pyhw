from functools import wraps


def val_checker(check_function):
    def _val_checker(func):
        @wraps(func)
        def f_wrapper(*args):
            if check_function(*args):
                result = func(*args)
            else:
                print(f'{func.__name__} wrong parameter!')
                result = None
            return result

        return f_wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


@val_checker(lambda x, y: y != 0)
def calc_div(x, y):
    return x / y


print(calc_cube(4))
print(calc_cube(-2))
print(calc_div(10, 5))
print(calc_div(0, 10))
print(calc_div(10, 0))
