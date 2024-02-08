import sys
from ft_filter import ft_filter


def ft_punctuation(match: str):

    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for c in match:
        if c in punctuation:
            return 1
    return 0


def check_entry_format(line: str):
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
