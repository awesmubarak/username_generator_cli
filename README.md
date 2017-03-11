# random_usernames.py

**A command line application to generate random usernames.**

Each username is an adjective and a noun strung together. There are 142
adjectives and 484 nouns in the wordlists, resulting in 68,728 possible
adjective-noun combinations.

## Usage

Run the script using `python3 random_usernames.py` or `./random_usernames.py`,
followed by any desired command line arguments.

| Command line argument                                         | Description                           |
| ------------------------------------------------------------- | ------------------------------------- |
| `-h`                                                          | Shows a help screen                   |
| `-n <number_of_usernames>` <br> `--number_of_usernames <nou>` | Changes number of usernames generated |
| `-u` <br> `--underscores`                                     | Uses underscores instead of camelCase |
| `--maximum_size <maximum size>`                               | Sets maximum size of usernames        |
| `--minimum_size <minimum size>`                               | Sets minimum size of usernames        |
