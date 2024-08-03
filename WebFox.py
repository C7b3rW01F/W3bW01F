#!/usr/bin/env python3

import requests
import subprocess as sp
from colorama import *
import time
import colorama
import re
from bs4 import BeautifulSoup, SoupStrainer
import urllib.parse as urlparse
import os, sys

sp.call("clear", shell=True)

if not os.getuid() == 0:
        sys.exit('This script must be run as root.')

colorama.init(autoreset = True)

sp.call("clear", shell=True)
sp.call("cat asciiart.txt", shell=True)
def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass
try:

    print(Fore.WHITE + Back.RED + Style.NORMAL + "Enter the URL without any HEADERS (www/wap/000 or http:// or https://) \n")
    target_url = input()
    print("\n")
    def webfox():
        def subdomains():
                sp.call("clear", shell=True)
                with open("subdomains.list","r") as wordlist_file:
                    for line in wordlist_file:
                            word = line.strip()
                            test_url = word + "." + target_url
                            response = request(test_url)   	
                            if response:
                                        print(Fore.GREEN + Back.BLACK + "[+] Webfox Discovered this Subdomain --> " + test_url)
                print("\n")
        def directories():
            sp.call("clear", shell=True)
            with open("common.txt","r") as wordlist_file1:
                    for line in wordlist_file1:
                            word1 = line.strip()
                            test_url1 = target_url + "/" + word1
                            response1 = request(test_url1)   	
                            if response1:
                                        print(Fore.GREEN + Back.BLACK + "[+] Webfox Discovered this Path --> " + test_url1)
            print("\n")

        def content():
            response3 = request(target_url)
            print(response3.content)
        
        def links():
            sp.call("clear", shell=True)
            response4 = request(target_url)
            try:                
                test_url9 = "https://" + target_url
                results = []
                
                def fetch_url(url):
                    response4 = requests.get(url)
                    return re.findall('(?:href=")(.*?)"', response4.content.decode(errors="ignore"))

                def extractor(url):
                    href = fetch_url(url)
                    for link in href:
                        link = urlparse.urljoin(url, link)

                        if "#" in link: #If you debug any HTML further you will find the hash symbol is used to load different parts of a page that describes the actual information of thet Tab or that page. 
                            link = link.split("#")[0]

                        if test_url9 in link and link not in results:
                            results.append(link)
                            print(link)
                            extractor(link)

                extractor(test_url9)
            except Exception as e:
                urllists = []
                for urls in BeautifulSoup(response4.content).find_all('a', href=True):
                    urllists.append(urls['href'])

                for urls in urllists:
                    print(urls)
                    

            print("\n")


        def adminpanel():
            sp.call("clear", shell=True)
            with open("admin.txt","r") as wordlist_file6:
                print("Have Patience. \U0001f600 Finding admin panel takes time. ")
                for line in wordlist_file6:
                    word6 = line.strip()
                    test_url6 = target_url + "/" + word6
                    response6 = request(test_url6)   	
                    if response6:                        
                        print(Fore.GREEN + Back.BLACK + "[+] Webfox Discovered the Admin Panel --> " + test_url6)
                        print("\n")

                                        

                            
                    

        print("[1] For Subdomain discovery. \n")
        print("[2] For Directory discovery.\n")
        print("[3] For Admin Panel Finder.\n")
        print("[4] For Analyzing the HTML code of the Target webpage. Please give a proper path.\n")
        print("[5] For Link Extractor.\n")

        user = input("Please select your option?\n")
        if user == '1':
            subdomains()
        elif user == '2':
            directories()
        elif user == '3':
            adminpanel()
        elif user == '4':
            content()
        elif user == '5':
            links()
            print("\n")
        else:
            print("Invalid input: \n")

    webfox()

    while True:
        print("\n")
        run_again = input("Do you want to run the script again? Answer with yes/no. \n")
        if run_again == 'yes' or run_again == 'y':
            sp.call("clear", shell=True)
            question = input("Do you want to test the same url? \n")
            if question == 'yes' or question =='y':
                webfox()
            elif question == 'no' or question =='n':
                new_url = input("please enter a new url. Ex: *google.com*. Don't use any HEADERS (www/wap/000 or http:// or https://)\n")
                target_url = new_url
                webfox()
            else:
                print("invalid input. \n")
                
            
        else:
            sp.call("clear", shell=True)
            sp.call("figlet Thanks for using. Bye", shell=True)
            break
except KeyboardInterrupt:
    print("\n")
    print("Terminated by user.. Quitting. \n")
    time.sleep(1)
    print("Thanks for Using. \U0001f600 \n")
   
