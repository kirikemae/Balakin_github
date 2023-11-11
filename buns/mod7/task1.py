def validate_args(function):
    def wrapper(*args):
        print(f"{args=}")
        # ровно один аргумент
        if len(args) < 1:
            return "Not enough arguments"
        # целое число
        if type(args[0]) != int:
            return "Wrong types"
        # если больше одного
        if len(args) > 1:
            return "Too many arguments"
        # не отрицательное
        if args[0] < 0:
            return "Negative argument"
        return function(*args)

    return wrapper


@validate_args
def testing(variable):
    return variable


if __name__ == '__main__':
    print(testing(2), '\n')
    print(testing(), '\n')
    print(testing(-10), '\n')
    print(testing(2.1), '\n')
    print(testing(0), '\n')
    print(testing('1'), '\n')
