import locale
import os
import time
import webbrowser
import colorama
from colorama import *
import sys
import random

"""
# ERRORS CLASS
This Class contains all the G/BS's of Death
"""
def error(code, reason, message):
    reason = str(reason)
    """
    This is the actual stuff

    The system will call this function in this class to raise the actual error

    ARGUMENT CODE will determine what screen to show, ARGUMENT REASON will determine what's the Exception

    """
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.2)
    time.sleep(0.2)
    os.system('cls' if os.name == 'nt' else 'clear')
    match code:
        case "UNDERVER":
            print(f"{Fore.LIGHTRED_EX}Error{Fore.WHITE}:")
            print(f"You're running on Python {sys.version_info[0]}.{sys.version_info[1]}. While the required one is 3.10+")
            i = input("Would you like to open a tab to download it? ")
            if i=='y':
                webbrowser.open_new_tab("https://www.python.org/downloads/release/python-3100/")
            else:
                exit()
        case "TIMED_OUT":
            print(Fore.LIGHTGREEN_EX + "Timed Out!" + Fore.WHITE)
            print(Fore.BLUE + "Common reasons:" + Fore.WHITE)
            print("""
            LOCAL:
             - Something failed in the loading function
             - Overflow
             - Disk might be too busy
             - Your memory doesn't have enough space to store variables
            
            INTERNET:
             - Unstable Connection
             - You have a Proxy/VPN on.
             - You live in an authoritarian country (Failed SSL connection and Active SmartFilter ISP)
             - Python must have farted
            """)
            print("The exception code generated might help: " + reason)
        case "!AUTH":
            print(f"Something went wrong, Are you{Fore.LIGHTRED_EX} authorized?" + Fore.WHITE)
            print("System halted.")
            print(code)
            print(reason)
        case "UNACCEPTABLE":
            print("Code is unacceptable, Please reinstall a CLEAN and GENUINE copy of ChungOSX.")
            print("Here's why this might've happened: " + reason)
        case "FILE404":
            print("Critical file 404. Put those back!")
            print(reason)
        case "SYNTAX400":
            print("Critical Syntax Error!")
            print("Here's the exception code: " + str(reason))
            print("ENTER to EXIT")
        case "UNADDED":
            print("Function or Feature " + message + " are NOT added yet!")
            print(reason)
        case "INDEX":
            print(Fore.CYAN + "IndexError" + Fore.WHITE)
            print("Index out of range or invalid.")
            print("You just ran into the most common error here")
            print("Exception: " + reason)
            if message == 'change' or message == 'edit':
                print("Might be because of a bugged command like \"Change\" or \"Edit\"")
            pass
            input()
            
        case "SMTH_WRONG":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Something went wrong.")
                print("Please create an issue in the repository if this happens without your modification to the code.")
                print("Additionally, read below for possible causes.")
                print("Latest Syntax Input: " + message if not message == "raise SMTH_WRONG".lower() else "MSG: None")
                print("ERROR CODE: " + code)
                print("EXCEPTION CODE: " + str(reason))
                input()
        case "!NET":
            os.system("cls" if os.name == 'nt' else 'clear')
            print(Fore.YELLOW + "WARNING:" + Fore.WHITE)
            print(f"We have tried, but no. Connection to Internet failed.")
            print("Online services might have been discontinued or temporarily unavailable.")
            print("Please consult making an issue at the repository if you can connect to other sites")
            print("ENTER TO EXIT" if os.name == 'nt' else "[RETURN] TO EXIT")
            input()
            exit()
        case "OSFLICT":
            while True:
                print(Fore.LIGHTRED_EX + "OPERATING SYSTEM" + Fore.RED + " ERROR")
                input()
                os.system('cls' if os.name == 'nt' else 'clear')
        case "UNDERAGE":
            print("I'm sorry, but it seems that you're below the age of consent in GitHub.")
            if locale.getlocale()[0] == 'English_United States':
                print("[US], To comply with COPPA Laws, We have an request.")
                input()
                print("Please grow up to 13 and then come back")
            else:
                print("Please age to your country's age of consent then come back.")
        case _:
            print("We've encountered an error, this is strange.")
            print("Seeing this screen means there is a rare error that we haven't caught yet.")
            time.sleep(0.1)
            print("Report back to https://github.com/Special-Rocket-Agents/ChungOSX/issues/new/choose")
            print("Check the below report to find a possible cause.")
            time.sleep(0.2)
            print("Error Code: " + code)
            print("Exception: " + str(reason))
            print("Your last message: " + message)
            time.sleep(2)
     
        
    
    input()
    exit()