import time


def validate_args(function):
    def wrapper(*args):
        # ровно один аргумент
        if len(args) < 1:
            raise ValueError("Not enough arguments")
        # целое число
        if type(args[0]) != int:
            raise ValueError("Wrong types")
        # если больше одного
        if len(args) > 1:
            raise ValueError("Too many arguments")
        # не отрицательное
        if args[0] < 0:
            raise ValueError("Negative argument")
        return function(*args)

    return wrapper


cache = {}


def memoize(function):
    def wrapper(*args):
        if not cache.get(args):
          cache[args] = function(*args)
        return cache[args]
    return wrapper


def timer(function):
    def wrapper(*args):
        if not hasattr(wrapper, 'start_time'):
            wrapper.start_time = time.time()
            result = function(*args)
            wrapper.finish_time = time.time()
            print(wrapper.finish_time - wrapper.start_time)
        else:
            return function(*args)
        return result
    return wrapper


@validate_args
@memoize
@timer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(35))

