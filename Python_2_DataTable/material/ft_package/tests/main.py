import sys
from ft_package import check_entry_format
from ft_package import ft_filter


def main():

    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        try:
            num = int(sys.argv[2])
        except Exception:
            raise AssertionError("error in converting the argument to int")
        check_entry_format(sys.argv[1])
        args = ft_filter(lambda w: len(w) > num,
                         sys.argv[1].split())

        print(args)

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        exit()

    return 0


if __name__ == "__main__":
    main()
