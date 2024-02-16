import sys


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
