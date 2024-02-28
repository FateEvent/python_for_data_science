import sys


def is_integer(n) -> bool:
    """is_integer(n) --> bool

The function returns True if the number passed as parameter is an integer;
False otherwise."""

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
        if not is_integer(sys.argv[1]):
            raise AssertionError("argument is not an integer")
        if float(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        raise AssertionError("more than one argument is provided")
except Exception as error:
    print(f'{type(error).__name__}: {error}')
    exit()
