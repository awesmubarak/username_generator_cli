#!/usr/bin/env python3

import sys
import getopt
from random import randint


def find_word(filename):
    file = open(filename, "r")
    list_of_words = file.readlines()
    return(list_of_words[randint(0, len(list_of_words) - 1)].rstrip())
    file.close()


def main(args):

    USAGE_INSTRUCTIONS = ("\n random_usernames.py"
                          " -u "
                          "[-n <number of usernames>]"
                          "[--minimum_size <minimum size>]"
                          "[--maximum_size <maximum size>]"
                          "\n")
    number_of_usernames = 6
    includes_underscores = False
    minimum_size = 0
    maximum_size = 255
    indentation_level = 4

    try:
        opts, args = getopt.getopt(
            args, "hun:", ["help", "underscores", "number_of_usernames=",
                           "maximum_size=", "minimum_size="])
    except getopt.GetoptError:
        print(USAGE_INSTRUCTIONS)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "help"):
            print(USAGE_INSTRUCTIONS)
            sys.exit()
        elif opt in ("-n", "--number_of_usernames"):
            try:
                if int(arg) > 0:
                    number_of_usernames = int(arg)
                else:
                    print(USAGE_INSTRUCTIONS)
                    sys.exit()
            except:
                print(USAGE_INSTRUCTIONS)
                sys.exit()
        elif opt in ("-u", "--underscores="):
            includes_underscores = True
        elif opt == "--maximum_size":
            try:
                maximum_size = int(arg)
            except ValueError:
                print("\n Maximum size must be a number\n")
                sys.exit(2)
        elif opt == "--minimum_size":
            try:
                minimum_size = int(arg)
            except ValueError:
                print("\n Minimum size must be a number\n")
                sys.exit(2)

    print("\n Your usernames:")
    for count in range(number_of_usernames):
        adjective = (find_word("./wordlists/adjectives.txt"))
        noun = (find_word("./wordlists/nouns.txt"))
        word_size = len(adjective + noun)
        if maximum_size > word_size and word_size > minimum_size:
            if includes_underscores:
                chosen_username = adjective + "_" + noun
                print(" " * (indentation_level + 1), chosen_username)
            else:
                camel_case_adjective = adjective[0].upper() + adjective[1:]
                camel_case_noun = noun[0].upper() + noun[1:]
                chosen_username = (camel_case_adjective + camel_case_noun)
                print(" " * (indentation_level + 1), chosen_username)
    print("")


if __name__ == "__main__":
    main(sys.argv[1:])
