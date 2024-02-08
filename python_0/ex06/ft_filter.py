from collections.abc import Iterable
from typing import TypeVar, Callable


_T = TypeVar("_T")


def ft_filter(__function: Callable[[_T], bool] | None,
              __iterable: Iterable[_T | None]):
    """
    ft_filter(function or None, iterable) --> list

    Returns a list yielding those items of iterable for which
    function(item) is true. If function is None, return the items that are
    true.
    """

    if __function:
        return [el for el in __iterable if __function(el)]
    else:
        return [el for el in __iterable if el]


def main():

    try:
        args = ft_filter(None, [0, 56, 76, 43, 89, 97])
        print(args)
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        exit()

    try:
        args = ft_filter(None, ["0", "", "la mamma", "va lontano", "a fare",
                                "le compere", ""])
        print(args)
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        exit()

    try:
        args = ft_filter(lambda w: len(w) > 5, ["0", "", "la mamma",
                                                "va lontano", "a fare",
                                                "le compere", ""])
        print(args)
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        exit()

    print(ft_filter.__doc__)
    return 0


if __name__ == "__main__":
    main()
