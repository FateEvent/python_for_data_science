from ft_package import ft_punctuation


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
