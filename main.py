import requests
from colorama import Fore, init
import os.path
import time
import logging
from configparser import ConfigParser

def writeconfig(variable, setting):
    config_object.set("CONFIG", variable, setting)
    with open('config.ini', 'w') as configfile:
        config_object.write(configfile)

def errorprocess(errormsg):
    print(Fore.RED + errormsg)
    time.sleep(2)
    print(f"{Fore.RED}Quitting, restart the script.")
    quit(time.sleep(2))

def debugprint(printmsg):
    if debug == "true":
        print(printmsg)

def platequery():
    global endofquery
    query = queryfile.readline()
    if not query:
        endofquery = True
    query = query.replace('\n', '')
    return(query)

def logavailability(checkquery, query):
    if 'NOT' in checkquery:
        if minimode == "false":
            print(Fore.RED + query + " is not available")
    else:
        if minimode == "false":
            print(Fore.GREEN + query + " is available")
        else:
            print(query)
        logger.info(query)
            
if os.path.isfile("available-plates.txt"):
    print("You have an available-plates log already in this directory. Continuing will erase that file.")
    print("Are you sure you want to continue? (Y/N)")
    while True:
        continuewithprogram = input()
        if continuewithprogram.lower() not in ('y', 'n'):
            continue
        if continuewithprogram.lower() == "y":
            break
        else:
            quit()

logging.basicConfig(filename="available-plates.txt", format='%(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

init(autoreset=True)

config_object = ConfigParser()
config_object.read("config.ini")
try:
    config = config_object["CONFIG"]
except KeyError:
    writeconfig = open("config.ini", "w")
    writeconfig.write("[CONFIG]\ndebug = false\nsleeptime = 3\nminimode = false")
    errorprocess("Config file missing. Don't worry though, I made one for you with the default options.")

debug = config["debug"]
minimode = config["minimode"]
try:
    sleeptime = float(config["sleeptime"])
except ValueError:
    print(
        f"{Fore.RED}Please specify sleeptime in seconds (ex. 3) next time. Defaulting to 3."
    )
    writeconfig("sleeptime", "3")
    sleeptime = float(config["sleeptime"])
    time.sleep(3)
if debug.lower() not in ("false", "true"):
    print(
        f"{Fore.RED}Please specify if debug is true or false next time. Defaulting to false."
    )
    writeconfig("debug", "false")
    debug = config["debug"]
    time.sleep(3)
if minimode.lower() not in ("false", "true"):
    print(
        f"{Fore.RED}Please specify if minimode is true or false next time. Defaulting to false."
    )
    writeconfig("minimode", "false")
    minimode = config["minimode"]
    time.sleep(3)

try:
    queryfile = open('query.txt')
except FileNotFoundError:
    errorprocess("No query specified. Make sure you created a query.txt file.")

endofquery = False

logging.getLogger("urllib3").setLevel(logging.WARNING)

payloadsetup = requests.get("https://services.flhsmv.gov/mvcheckpersonalplate/")
viewstate = payloadsetup.text.split('id="__VIEWSTATE" value="')[1].split('"')[0]
eventvalidation = payloadsetup.text.split('id="__EVENTVALIDATION" value="')[1].split('"')[0]
viewstategenerator = payloadsetup.text.split('id="__VIEWSTATEGENERATOR" value="')[1].split('"')[0]

if minimode == "true":
    print("Started")
while True:
    payload = {'__VIEWSTATE': viewstate, '__VIEWSTATEGENERATOR': viewstategenerator, '__EVENTVALIDATION': eventvalidation, 'ctl00$MainContent$txtInputRowOne': platequery(), 'ctl00$MainContent$txtInputRowTwo': platequery(), 'ctl00$MainContent$txtInputRowThree': '', 'ctl00$MainContent$txtInputRowFour': '', 'ctl00$MainContent$txtInputRowFive': '', 'ctl00$MainContent$btnSubmit': 'Submit'}
    debugprint(payload)
    checkrequest = requests.post("https://services.flhsmv.gov/mvcheckpersonalplate/", data=payload)
    cr2 = checkrequest
    debugprint(checkrequest.text)
    try:
        r1availability = checkrequest.text.split('id="MainContent_lblOutPutRowOne" class="outputText" style="color: #0000a0; font-weight: bold">')[1].split('<')[0]
        r2availability = checkrequest.text.split('id="MainContent_lblOutPutRowTwo" class="outputText" style="color: #0000a0; font-weight: bold">')[1].split('<')[0]
        r1query = checkrequest.text.split('name="ctl00$MainContent$txtInputRowOne" type="text" value="')[1].split('"')[0]
        r2query = checkrequest.text.split('name="ctl00$MainContent$txtInputRowTwo" type="text" value="')[1].split('"')[0]
    except IndexError:
        if endofquery:
            quit(print("End of query file reached. Quitting."))
        else:
            errorprocess("Something went wrong. Please try again.")
    debugprint(r1query)
    debugprint(r1availability)
    debugprint(r2query)
    debugprint(r2availability)
    logavailability(r1availability, r1query)
    logavailability(r2availability, r2query)
    time.sleep(sleeptime)