import sys


def analyze_entry(line: str):
    if len(line):
        if not line.isascii():
            sys.exit("AssertionError: non ASCII characters in the string")

        print(line)
    return 0


def prompt_a_prompt():

    buffer = list()
    ret = ''
    for line in sys.stdin:
        buffer.append(line)

    return ret.join(buffer)


def main():

    if len(sys.argv) > 2:
        sys.exit("AssertionError: more than one argument is provided")
    if len(sys.argv) == 1:
        text = prompt_a_prompt()
    else:
        text = sys.argv[1]
    analyze_entry(text)

    return 0


if __name__ == "__main__":
    main()
