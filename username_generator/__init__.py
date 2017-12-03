#!/usr/bin/env python3

"""Username generator.

A command line application to generate random usernames.

"""

from argparse import ArgumentParser
from random import choice as randchoice
from os import path
from .wordlists import ADJECTIVES, NOUNS


def check_arguments(args: dict):
    """Verify arguments.

    Args:
        Dict: Arguments.

    Raises:
        ValueError for all errors.

    """
    if args["min_size"] >= args["max_size"]:
        raise ValueError("Max size must be greater than min size")
    if args["min_size"] > 14 or args["max_size"] < 8:
        raise ValueError("Word range must be between 3 and 14")
    if args["num"] > 10000:
        raise ValueError("Can't generate more than 10000 usernames")


def get_uname(min_size: int, max_size: int, underscores: bool):
    """Chooses username.

    Args:
        Min_size (int): Minimum size.
        Max_size (int): Maximum size.
        Underscores (bool): If true the sections of the username will be
            seperated using underscores. If false they will be joined in camel
            case (LikeThis).

    Returns:
        Str: Username.

    """
    # choose base words and strip
    adjective = randchoice(ADJECTIVES)
    noun = randchoice(NOUNS)
    # join words as requested
    if underscores:
        uname = adjective + "_" + noun
    else:
        camel_case_adjective = adjective[0].upper() + adjective[1:]
        camel_case_noun = noun[0].upper() + noun[1:]
        uname = (camel_case_adjective + camel_case_noun)
    if not (min_size <= len(uname) and len(uname) <= max_size):
        uname = get_uname(min_size, max_size, underscores)
    return uname


def main(**kwargs):
    """Main."""

    # parse command line arguments
    parser = ArgumentParser(description="Generate random usernames.")
    parser.add_argument("--num", metavar="NUMBER", type=int,
                        default=6, help="change number of usernames generated")
    parser.add_argument("--underscores", default=False, action="store_true",
                        help="use underscores instead of camelCase")
    parser.add_argument("--max_size", metavar="NUMBER", type=int,
                        default=255, help="set maximum size of usernames")
    parser.add_argument("--min_size", metavar="NUMBER", type=int,
                        default=0, help="set minimum size of usernames")
    parser.add_argument("--no_print", default=False, action="store_true",
                        help="prevent printing usernames to terminal")
    parser.add_argument("--fname", metavar="FILE NAME", default="",
                        help="save output in a text file")
    parser.add_argument("--indentation", metavar="LEVEL", type=int,
                        default=4, help="number of spaces to indent usernames")
    parser.add_argument("--no_intro", default=False, action="store_true",
                        help="hide short introductory notes")
    parser.add_argument("--return_val", default=False, action="store_true",
                        help="returns username list")

    # get args
    if "args" in kwargs:
        args = kwargs["args"]
    else:
        args = vars(parser.parse_args())
    try:
        check_arguments(args)
    except ValueError as error:
        print("Error: " + str(error))
        exit(1)

    # get usernames
    min_s, max_s, u = args["min_size"], args["max_size"], args["underscores"]
    raw_unames = [get_uname(min_s, max_s, u) for i in range(args["num"])]
    unames = [(" " * (args["indentation"])) + uname for uname in raw_unames]

    # format and display usernames
    header = ("Your usernames:\n" * (not args["no_intro"]))
    output_text = header + ("\n").join(unames)
    if not args["no_print"]:
        print(output_text)
    if args["fname"] != "":
        with open(path.expanduser(args["fname"]), "w") as file:
            file.write(output_text + "\n")

    if args["return_val"]:
        return unames


if __name__ == "__main__":
    main()
