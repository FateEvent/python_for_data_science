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
