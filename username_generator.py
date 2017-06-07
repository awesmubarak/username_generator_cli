#!/usr/bin/env python3

import sys
import getopt
from random import randint


def find_word(filename):
    """Return a chosen word from a file containing a word per line."""
    with open(filename, "r") as file:
        list_of_words = file.readlines()
    return(list_of_words[randint(0, len(list_of_words) - 1)].rstrip())


def main(args):
    """Main program."""
    # define variables
    USAGE_INSTRUCTIONS = ("\nrandom_usernames.py"
                          " -u "
                          "[-n <number of usernames>]"
                          "[--file_name <file name>]"
                          "[--minimum_size <minimum size>]"
                          "[--maximum_size <maximum size>]"
                          "\n")
    ERROR_MESSAGE = "\033[1m" + "\nERROR: "
    file_name = ""
    underscores = False
    indentation_level = 4
    maximum_size = 255
    minimum_size = 0
    number_of_usernames = 6
    usernames = []

    # parse command line arguments
    try:
        opts, args = getopt.getopt(
            args, "h", ["help", "underscores", "number_of_usernames=",
                        "file_name=", "maximum_size=", "minimum_size="])
    except getopt.GetoptError:
        print(ERROR_MESSAGE + "Invalid commandline arguments")
        print(USAGE_INSTRUCTIONS)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "help"):
            # help instructins
            print(USAGE_INSTRUCTIONS)
            sys.exit(0)
        elif opt == "--number_of_usernames":
            # number of usernames
            try:
                # check if positive
                if int(arg) >= 1:
                    number_of_usernames = int(arg)
                else:
                    print(ERROR_MESSAGE + "Number of usernames must be positive\n")
                    sys.exit(2)
            except ValueError:
                print(ERROR_MESSAGE + "Number of usernames must be a number\n")
                sys.exit(2)
        elif opt == "--underscores":
            # underscores
            underscores = True
        elif opt == "--maximum_size":
            # maximum size
            try:
                maximum_size = int(arg)
            except ValueError:
                print(ERROR_MESSAGE + "Maximum size must be a number\n")
                sys.exit(2)
        elif opt == "--minimum_size":
            # minimum size
            try:
                minimum_size = int(arg)
            except ValueError:
                print(ERROR_MESSAGE + "Minimum size must be a number\n")
                sys.exit(2)
        elif opt == "--file_name":
            # file name
            file_name = arg

    # get usernames
    for count in range(number_of_usernames):
        # load words from files
        adjective = (find_word("./wordlists/adjectives.txt"))
        noun = (find_word("./wordlists/nouns.txt"))
        # make sure the word size is appropriate
        word_size = len(adjective + noun)
        if maximum_size > word_size and word_size > minimum_size:
            # print in the correct format
            if underscores:
                chosen_username = adjective + "_" + noun
            else:
                camel_case_adjective = adjective[0].upper() + adjective[1:]
                camel_case_noun = noun[0].upper() + noun[1:]
                chosen_username = (camel_case_adjective + camel_case_noun)
            # indent and append username
            usernames.append(((indentation_level + 1) * " ") + chosen_username)

    # join and format usernames
    output_text = "\n Your usernames:\n" + ("\n").join(usernames) + "\n"

    # print or save usernames
    if file_name == "":
        print(output_text)
    else:
        with open(file_name, 'w') as file:
            file.write(output_text)


if __name__ == "__main__":
    main(sys.argv[1:])
