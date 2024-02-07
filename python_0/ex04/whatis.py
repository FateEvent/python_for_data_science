import sys

if len(sys.argv) == 2:
    if len(sys.argv[1]) > 15:
        sys.exit("AssertionError: too many characters")
    if sys.argv[1][0] == '0' and sys.argv[1][1] != '.':
        sys.exit("AssertionError: unexisting number starting with zero")
    if float(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
else:
    sys.exit("AssertionError: more than one argument is provided")
