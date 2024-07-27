from colorama import *
import subprocess as sp
print("""


░█████╗░███████╗██████╗░██████╗░██████╗░░██╗░░░░░░░██╗░█████╗░░░███╗░░███████╗
██╔══██╗╚════██║██╔══██╗╚════██╗██╔══██╗░██║░░██╗░░██║██╔══██╗░████║░░██╔════╝
██║░░╚═╝░░░░██╔╝██████╦╝░█████╔╝██████╔╝░╚██╗████╗██╔╝██║░░██║██╔██║░░█████╗░░
██║░░██╗░░░██╔╝░██╔══██╗░╚═══██╗██╔══██╗░░████╔═████║░██║░░██║╚═╝██║░░██╔══╝░░
╚█████╔╝░░██╔╝░░██████╦╝██████╔╝██║░░██║░░╚██╔╝░╚██╔╝░╚█████╔╝███████╗██║░░░░░
░╚════╝░░░╚═╝░░░╚═════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚════╝░╚══════╝╚═╝░░░░░
	

             Disclaimer:An automated payload generator script dedicated
			for Metasploit Enthusiastics. This tool is for educational
			Purposes only. I will not be responsible for any illegal
			activity done by you. You'll solely be responsible for
			any misuse of this script.\n""")
print("Do you agree with the terms and conditions? \n")
user = input()
if (user == 'yes') or (user == 'y') or (user == 'Yes') or (user == 'Y'):
    sp.call("python3 Mal_gen.py", shell=True)
else:
    print("\n")
    print("Seems you don't agree. Thanks for using. \n")