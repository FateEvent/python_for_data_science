import sys
from ft_filter import ft_filter


def ft_punctuation(match: str):
    """
    ft_punctuation(match: str) --> int

    The function checks each character of the string passed as a parameter
    for a punctuation mark and returns 1 if it finds it and 0 otherwise.
    """

    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for c in match:
        if c in punctuation:
            return 1
    return 0


def check_entry_format(line: str):
    """
    check_entry_format(line: str)

    The function parses the string passed as a parameter and raises exceptions
    if non-ascii characters, punctuation marks or non-printable characters are
    present.
    """

    if len(line):
        if not line.isascii():
            raise AssertionError("non ASCII characters present in the string")
        if ft_punctuation(line):
            raise AssertionError("punctuation present in the string")
        if not line.isprintable():
            raise AssertionError("invisible characters present in the string")
    else:
        raise AssertionError("the string is empty")


def main():

    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        try:
            num = float(sys.argv[2])
        except Exception:
            raise AssertionError("error in converting the argument to float")

        args = ft_filter(lambda w: len(w) > num,
                         sys.argv[1].split())
        print(args)

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        exit()

    return 0


if __name__ == "__main__":
    main()
