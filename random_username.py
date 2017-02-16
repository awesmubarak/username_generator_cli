#!/usr/bin/python3

import sys, getopt
from random import randint

def find_word(filename):
    file = open(filename,"r")
    list_of_words = file.readlines()
    return(list_of_words[randint(0, len(list_of_words) - 1)].rstrip())
    file.close()

def main(args):

    USAGE_INSTRUCTIONS = "\n random_username.py -u -n <number_of_usernames> \n"
    number_of_usernames = 6
    includes_underscores = False

    try:
        opts, args = getopt.getopt(args,"hun:",["help","underscores=","number_of_usernames=",])
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

    print("\n Your usernames:")
    for word_number in range(number_of_usernames):
        adjective = (find_word("./wordlists/adjectives.txt"))
        noun = (find_word("./wordlists/nouns.txt"))
        if includes_underscores:
            print("    ", (adjective + "_" + noun))
        else:
            print("    ", (adjective[0].upper() + adjective[1:] +
                           noun[0].upper() + noun[1:]))
    print("")


if __name__ == "__main__":
    main(sys.argv[1:])
