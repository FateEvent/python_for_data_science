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


def create_dictionary(dictionary: dict):
    """
    create_dictionary(dictionary: dict) --> dict

    The function returns a dictionary made up of latin alphanumeric characters
    as entries and the corresponding morse code values as values.
    """

    latin_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                   "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                   "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6",
                   "7", "8", "9", " "]
    morse_line = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                  "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                  "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                  "-.--", "--..", "-----", ".----", "..---", "...--", "....-",
                  ".....", "-....", "--...", "---..", "----.", "/"]

    i = 0
    while i < len(latin_chars):

        dictionary[latin_chars[i]] = morse_line[i]
        i += 1

    return dictionary


def main():
    """
    The program takes a string as an argument and encodes it into Morse Code.
    """

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        check_entry_format(sys.argv[1])

        NESTED_MORSE = dict()
        create_dictionary(NESTED_MORSE)

        text = sys.argv[1]
        print(text)

        i = 0
        for character in text:

            print(NESTED_MORSE[character.capitalize()], end='')
            if (i < len(text) - 1):
                print(end=' ')
            else:
                print()
            i += 1

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        exit()

    print(main.__doc__)
    return 0


if __name__ == "__main__":
    main()
