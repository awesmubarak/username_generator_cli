Username generator
==================

**A command line application to generate random usernames.**

Each username is an adjective and a noun strung together. There are 142
adjectives and 484 nouns in the wordlists, resulting in 68,728 possible
adjective-noun combinations.

Wordlist sources:

- http://www.talkenglish.com/vocabulary/top-500-adjectives.aspx
- http://www.talkenglish.com/vocabulary/top-1500-nouns.aspx

Installation
------------

Using pip:

``pip3 install username_generator``

Manual:

``git clone https://github.com/abactel/username_generator_cli``

``cd username_generator_cli``

``setup.py install``

Usage
-----

Open a terminal and run ``usernames``. The following options are available:

+---------------------------+------------------------------------------+
| Command line argument     | Description                              |
+===========================+==========================================+
| ``-h``, ``--help``        | Show this help message and exit          |
+---------------------------+------------------------------------------+
| ``--num NUMBER``          | Change number of usernames generated     |
+---------------------------+------------------------------------------+
| ``--underscores``         | Use underscores instead of camelCase     |
+---------------------------+------------------------------------------+
| ``--max_size NUMBER``     | Set maximum size of usernames            |
+---------------------------+------------------------------------------+
| ``--min_size NUMBER``     | Set minimum size of usernames            |
+---------------------------+------------------------------------------+
| ``--no_print``            | Prevent printing usernames to terminal   |
+---------------------------+------------------------------------------+
| ``--fname FILE NAME``     | Save output in a text file               |
+---------------------------+------------------------------------------+
| ``--indentation LEVEL``   | Number of spaces to indent usernames     |
+---------------------------+------------------------------------------+
| ``--no_intro``            | Hide short introductory notes            |
+---------------------------+------------------------------------------+
