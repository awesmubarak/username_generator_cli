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

| Command line argument         | Description                          |
| ----------------------------- | ------------------------------------ |
| `-h`, `--help`                | Display usage instructions           |
| `--num <number of usernames>` | Change number of usernames generated |
| `--underscores`               | Use underscores instead of camelCase |
| `--fname <file name>`         | Save output in a text file           |
| `--max_size <maximum size>`   | Set maximum size of usernames        |
| `--min_size <minimum size>`   | Set minimum size of usernames        |

<!-- Links: -->

[adjective list source]: http://www.talkenglish.com/vocabulary/top-500-adjectives.aspx

[noun list source]: http://www.talkenglish.com/vocabulary/top-1500-nouns.aspx
