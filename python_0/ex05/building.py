import sys


def ft_punctuation(match: str):
    """
    ft_punctuation(match: str) --> int

    The function checks each character of the string passed as a parameter
    for a punctuation mark and returns 1 if it finds it and 0 otherwise.
    """

    punctuation = "!\"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~"
    for c in match:
        if c in punctuation:
            return 1
    return 0


def analyze_entry(line: str):
    """
    analyze_entry(line: str)

    The function parses the string passed as a parameter and prints on the
    standard output the number of total characters present in the string as
    well as the count of uppercase and lowercase letters, punctuation marks,
    spaces and digits.
    """

    if len(line):

        if not line.isascii():
            raise AssertionError("non ASCII characters present in the string")

        uppers = 0
        lowers = 0
        spaces = 0
        punct_marks = 0
        digits = 0
        for c in line:
            if c.isupper():
                uppers += 1
            elif c.islower():
                lowers += 1
            elif c.isspace():
                spaces += 1
            elif ft_punctuation(c):
                punct_marks += 1
            elif c.isdigit():
                digits += 1

        print(f'The text contains {len(line)} characters:')
        print(f'{uppers} uppercase letters')
        print(f'{lowers} lowercase letters')
        print(f'{punct_marks} punctuation marks')
        print(f'{spaces} spaces')
        print(f'{digits} digits')


def prompt_a_prompt():
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


def building():
    """
    The goal of this program is parsing the text given as an argument
    or prompted by the user and displays the count of its upper-case
    and lower-case characters, punctuation marks, digits and spaces.
    """

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 1:
            try:
                text = prompt_a_prompt()
            except Exception as error:
                print(f'{type(error).__name__}: {error}')
                exit()
        else:
            try:
                text = sys.argv[1]
            except Exception as error:
                print(f'{type(error).__name__}: {error}')
                exit()
        try:
            analyze_entry(text)
        except Exception as error:
            print(f'{type(error).__name__}: {error}')
            exit()
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        exit()


def main():

    building()
    return 0


if __name__ == "__main__":
    main()
