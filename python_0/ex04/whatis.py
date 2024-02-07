import sys


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


try:
    if len(sys.argv) == 2:
        if len(sys.argv[1]) > 15:
            raise AssertionError("too many characters")
        if sys.argv[1][0] == '0' and sys.argv[1][1] != '.':
            raise AssertionError("unexisting number starting with zero")
        if not is_integer(sys.argv[1]):
            raise AssertionError("argument is not an integer")
        num = float(sys.argv[1]).is_integer()
        if num % 2 == 0:
            print("{num} I'm Even.")
        else:
            print("I'm Odd.")
    else:
        raise AssertionError("more than one argument is provided")
except Exception as error:
    print(f'{type(error).__name__}: {error}')
    exit()
