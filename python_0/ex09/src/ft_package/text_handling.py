import sys


def ft_punctuation(match: str) -> int:
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


def is_integer(n) -> bool:
    """
    is_integer(n) --> bool

    The function returns True if the number passed as parameter is an integer;
    False otherwise.
    """

    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def prompt_a_prompt() -> str:
    """
    prompt_a_prompt() --> str

    A prompt is offered to the user and their input is appended
    to a buffer which is returned.
    """

    buffer = list()
    ret = ''
    for line in sys.stdin:
        buffer.append(line)

    return ret.join(buffer)
