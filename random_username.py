#!/usr/bin/python3

from random import randint

def find_word(filename):
    file = open(filename,"r")
    list_of_words = file.readlines()
    return(list_of_words[randint(0, len(list_of_words) - 1)].rstrip())
    file.close()

for word in range(6):
    adjective = (find_word("./wordlists/adjectives.txt"))
    noun = (find_word("./wordlists/nouns.txt"))
    print((adjective[0].upper() + adjective[1:] + noun[0].upper() + noun[1:]))
