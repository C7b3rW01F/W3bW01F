import subprocess as sp
import os, sys
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
from colorama import *

if not os.getuid() == 0:
        sys.exit('This script must be run as root.')

def intro():
    sp.call("clear", shell=True)
    sp.call("figlet SQLi vuln scanner", shell=True)
    time.sleep(1)
    sp.call("clear", shell=True)
    sp.call("figlet Coded By", shell=True)
    sp.call("figlet DarknetWolf", shell=True)
    time.sleep(1)
    sp.call("clear", shell=True)
    print(" \n")

intro()

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url", help='url', required=True)
parser.add_argument("-p","--payloads", help="payloads list", required=True)
args = parser.parse_args()

def fuzz(url, payloads):
    for payload in open(payloads, "r").readlines(): #open function used to open a file and return a corresponding file object. It takes two arguments: the file path and the mode in which the file should be opened (e.g., 'r' for reading, 'w' for writing).
        new_url = url.replace('{fuzz}',payload)
        request = requests.get(new_url)
        if request.elapsed.total_seconds() > 7:
            print(Style.BRIGHT + Fore.RED + "Timeout Detected with", new_url)
        else:
            print(Style.BRIGHT + Fore.CYAN + "Not working with this following payload:", payload)

def verify(url):
    url_test = url.replace("{fuzz}", "")
    req = requests.get(url_test)
    if req.elapsed.total_seconds() > 6:
        sys.exit("Please make sure you have a good internet connection:")
    else:
        fuzz(args.url, args.payloads)
if not '{fuzz}' in args.url:
    sys.exit("The {fuzz} parameter is not found:")
else: 
    verify(args.url)
