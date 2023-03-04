<div align="center">

# ANNOUNCEMENT: I have barely tested this bot, so if you find any bugs, please open up an issue. I will try to fix it as soon as possible.

# ![Plate Checker Logo](https://github.com/bestadamdagoat/flVanityPlateChecker/blob/main/platechecker.png?raw=true)

## A bot that will check if Florida vanity plates are available or taken, poorly coded in Python.
#### If this bot surprisingly worked for you, it would be cool if you donated to me. It would convince me to code better and actually be more commited to these projects. Check the sidebar for ways to donate to me.
<img alt="GitHub" src="https://img.shields.io/github/license/bestadamdagoat/flVanityPlateChecker"> ![Website](https://img.shields.io/website?label=FLHSMV%20Tool&url=https%3A%2F%2Fservices.flhsmv.gov%2Fmvcheckpersonalplate%2F) ![Liberapay receiving](https://img.shields.io/liberapay/receives/bestadam?label=receiving%20on%20liberapay) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/colorama) ![GitHub issues](https://img.shields.io/github/issues/bestadamdagoat/flVanityPlateChecker) ![GitHub repo size](https://img.shields.io/github/repo-size/bestadamdagoat/flVanityPlateChecker) ![GitHub repo file count](https://img.shields.io/github/directory-file-count/bestadamdagoat/flVanityPlateChecker) ![Lines of code](https://img.shields.io/tokei/lines/github/bestadamdagoat/flVanityPlateChecker)
</div>

Basically what this bot does is:
- Reads your query.txt file.
- Grabs the useless request headers from the FLHSMV website.
- Appends the next two lines to a request to the [FLHSMV Personalized Plate Tool](https://services.flhsmv.gov/mvcheckpersonalplate/).
- Opens the link and reads the page.
- Checks if the plate is taken or available.
- Exports all the available plates to a txt.
- And does a lot more in the background.

## NOTES: 
- The default `query.txt` file will contain random plates that are available and not available. If every plate is coming up as either available/not-available, go into the main.py and set debug mode to true to get a further insight into what the bot is seeing and open up an issue with a log from the console.

- You can theoretically check 5 plates at a time, but anything above 2 plates at a time throws an error. I will try to fix this in the future.

- EXE releases will always be based off of the main branch.

- Developer/Maintainer Notes:
     - Main Branch requires a PR and will only be updated after a few commits to dev. All important issues with main/important updates must require a PR. 
     - Dev Branch gets updated frequently. All updates/mini issue fixes must be pushed to dev first. 

## CONFIG.INI
- NOTE: Leaving any of these unset/incorrectly set will set the variables to their defaults.
1. `debug`
    - Can be set to either `true` or `false`. Enables/disables debug mode, which outputs the checklink with the query, the page, and the query. The default setting for this is `false`.
2. `sleeptime`
    - Can be set to any time in seconds (ex. `3`, `7`, `1`). The default setting for this is `3`.
3. `minimode`
    - Can be set to either `true` or `false`. Enables/disables mini mode, which disables output of not-available plates. The default setting for this is `false`.

## HOW TO USE THE BOT:
NOTE: Make sure you are using Python 3.
1. Clone the repository
     - Or download the zip using [this link](https://github.com/bestadamdagoat/flVanityPlateChecker/archive/refs/heads/main.zip).
2. Open up the folder in your favorite IDE (like PyCharm or VScode)
     - If you can open up this file in CMD/Terminal, you do not need an explanation on how to get this thing fully setup.
3. Go into the terminal and type `pip install -r requirements.txt`
4. Edit the `query.txt` file to your liking
     - Make sure to separate all the plates by new lines. Also make sure all the queries fit the plate requirements.
5. Edit the `config.ini` file to your liking
6. You are now ready to run the bot! Make sure to run `main.py`. 

## COMMON ISSUES + FIXES:
NOTE: This will not always be up-to-date, and I will not add uncommon issues to this list. If you want an up-to-date list of fixes, click [here](https://github.com/bestadamdagoat/flVanityPlateBot/issues?q=is%3Aissue+is%3Aclosed).

- `warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "`
     - Run `pip install --upgrade requests` in the terminal.
