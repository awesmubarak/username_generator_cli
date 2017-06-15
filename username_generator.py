#!/usr/bin/env python3

import argparse
import sys
import os
from random import randint


def find_word(filename):
    """Return a chosen word from a file containing a word per line."""
    with open(filename, "r") as file:
        list_of_words = file.readlines()
    return(list_of_words[randint(0, len(list_of_words) - 1)].rstrip())


def main(args):
    """Main program."""
    # define variables
    indentation_level = 4
    usernames = []

    # parse command line arguments
    parser = argparse.ArgumentParser(description="Generate random usernames.")
    parser.add_argument("--num", metavar="NUMBER", type=int,
                        default=6, help="Change number of usernames generated")
    parser.add_argument("--underscores", default=False, action="store_true",
                        help="Use underscores instead of camelCase")
    parser.add_argument("--fname", metavar="FILE NAME", default="",
                        help="Save output in a text file")
    parser.add_argument("--max_size", metavar="NUMBER", type=int,
                        default=255, help="Set maximum size of usernames")
    parser.add_argument("--min_size", metavar="NUMBER", type=int,
                        default=0, help="Set minimum size of usernames")
    args = parser.parse_args()

    # get usernames
    for count in range(args.num):
        # load words from files
        adjective = (find_word("./wordlists/adjectives.txt"))
        noun = (find_word("./wordlists/nouns.txt"))
        # make sure the word size is appropriate
        word_size = len(adjective + noun)
        if args.max_size > word_size and word_size > args.min_size:
            # print in the correct format
            if args.underscores:
                chosen_username = adjective + "_" + noun
            else:
                camel_case_adjective = adjective[0].upper() + adjective[1:]
                camel_case_noun = noun[0].upper() + noun[1:]
                chosen_username = (camel_case_adjective + camel_case_noun)
            # indent and append username
            usernames.append(((indentation_level + 1) * " ") + chosen_username)

    # format and return usernames to user
    output_text = "\n Your usernames:\n" + ("\n").join(usernames) + "\n"
    if args.fname == "":
        print(output_text)
    else:
        with open(os.path.expanduser(args.fname), "w") as file:
            file.write(output_text + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
