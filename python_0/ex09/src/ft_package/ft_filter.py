from collections.abc import Iterable, Callable
from typing import TypeVar


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
