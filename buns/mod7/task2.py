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


@validate_args
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(10))
    print(cache)