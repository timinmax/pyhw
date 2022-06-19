import inspect
from functools import wraps


def type_logger(func):
    @wraps(func)
    def f_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_name = list(zip(inspect.getfullargspec(func)[0], args))

        str_to_log = f'{func.__name__}('
        for arg in args_name:
            str_to_log += f'{arg[0]} = {arg[1]}: {type(arg[1])}  '
        str_to_log = str_to_log.strip()
        str_to_log += f') = {result}\n'

        with open('arg_log.txt', 'a') as log_file:
            log_file.write(str_to_log)
        return result

    return f_wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(3), calc_cube(5))
