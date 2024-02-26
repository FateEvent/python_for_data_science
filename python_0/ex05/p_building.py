# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    building.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/02/08 08:20:39 by pwolff            #+#    #+#             #
#    Updated: 2024/02/09 17:34:30 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

"""
    Chemin pour flack8 :
    export PATH=$PATH:/home/pwolff/.local/bin

    lire la doc :
    python3
    import building
    help(building)

    Expected outputs: (the carriage return counts as a space, if you don’t
    want to return one use ctrl + D)
https://stackoverflow.com/questions/15666923/sys-stdin-does-not-close-on-ctrl-d

"""

import sys
# import string


def treatement(sentence):

    """
    This time you have to make a real autonomous program, with a main,
    which takes a single string argument and displays the sums of its
    upper-case characters, lower-case characters, punctuation characters,
    digits and spaces.
    """

    strPunctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    nbUpperCase = sum(1 for value in sentence if value.isupper())
    nbLowerCase = sum(1 for value in sentence if value.islower())
    nbPunctuation = sum(1 for value in sentence if value in strPunctuation)
    nbDigits = sum(1 for value in sentence if value.isdigit())
    nbSpaces = sum(1 for value in sentence if value.isspace() or value == '\n')

    # strPunctuation = string.punctuation
    # for value in tab[1]:
    #     if value.isupper():
    #         nbUpperCase += 1
    #     elif value.islower():
    #         nbLowerCase += 1
    #     elif value in strPunctuation:
    #         nbPunctuation += 1
    #     elif value.isdigit():
    #         nbDigits += 1
    #     elif value == " " or value =="\n":
    #         nbSpaces += 1

    print(f"The text contains {len(sentence)} characters:")
    print(f"{nbUpperCase} upper letters")
    print(f"{nbLowerCase} lower letters")
    print(f"{nbPunctuation} punctuation marks")
    print(f"{nbSpaces} spaces")
    print(f"{nbDigits} digits")


def main():

    """
        • If None or nothing is provided, the user is prompted to provide
        a string.
        • If more than one argument is provided to the program,
        print an AssertionError.
    """

    tab = sys.argv
    sentence = ""
    try:
        if len(tab) > 2:
            raise AssertionError("Error too many arguments !!!")
        elif len(tab) == 2:
            sentence = tab[1]
        else:
            print("What is the text to count?")
            while True:
                line = sys.stdin.readline()
                if line == "":
                    break
                sentence += line

    except AssertionError as error:
        print(AssertionError.__name__+": ", error)
        sys.exit()

    treatement(sentence)


if __name__ == "__main__":
    main()
