# Username generator

**A command line application to generate random usernames.**

Each username is an adjective and a noun strung together. There are 142
adjectives and 484 nouns in the wordlists, resulting in 68,728 possible
adjective-noun combinations.

The adjective list was taken from [talkenglish][adjective list source]. The
noun list was also taken from [talkenglish][noun list source]. Word that fit
into more than one category were excluded (e.g. file is a noun and a verb).

## Usage

Run the script using `python3 username_generator.py` or `./username_generator.py`,
followed by any desired command line arguments.

| Command line argument            | Description                                |
| -------------------------------- | ------------------------------------------ |
| `-h`                             | Shows a help screen                        |
| `--number_of_usernames <number>` | Changes number of usernames generated      |
| `--underscores`                  | Uses underscores instead of camelCase      |
| `--file_name <file name>`        | Allows saving and specifies save location. |
| `--maximum_size <maximum size>`  | Sets maximum size of usernames             |
| `--minimum_size <minimum size>`  | Sets minimum size of usernames             |

<!-- Links: -->

[adjective list source]: http://www.talkenglish.com/vocabulary/top-500-adjectives.aspx

[noun list source]: http://www.talkenglish.com/vocabulary/top-1500-nouns.aspx
