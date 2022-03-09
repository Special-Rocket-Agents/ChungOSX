#####################
# Built-In Modules
from calendar import c
from errno import errorcode
import logging
from operator import sub
import os
import random
import subprocess
import webbrowser
from xml.etree.ElementTree import TreeBuilder
import colorama
import json
import sys
import time
###################

#############################
from psutil import Process
from datetime import datetime # Clock 
from colorama import Fore, Back, Style # Color
#############################


###### CHUNGUS UI ######
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QKeySequence
######            ######


#### VARIABLES, DO NOT MIND ####
shit = False
quoteshit = False
doneIntro = False
curMemory = Process(os.getpid())
####                        ####

##### SYSTEM STUFF #####
from platform import system as cliOS # Standing for ClientOS
from pathlib import Path # Path
from webbrowser import open_new_tab # Your Browser



### LUA STUFF ###
from lupa import LuaRuntime
lua = LuaRuntime()
###           ###

###### INTERNAL SETTINGS ######
osName = "ChungOS"  # Keep in mind that this is shitto different than os.name
version = "1.0.0"
username = os.getlogin()
fallBackToTERMINAL = False  # (False by Default) If set to true, uses your OS's terminal instead, whatever it may be bash, or CMD, or pw3yyyyysh
branch = 'master' # GitHub Main Branch.

startingquotes = [
    "Too stuck? Check out the discord page by 'chung --discord'!",
    "You can simulate the error screens by the \"raise <code>\" command!",
    "If you need a live-ISO-like mode, try 'fall'",
    "ChungOS relies on git and stable internet connection!",
    "It would be a chad move if you suggested us REAL COOL features",
    "As always, This project is open-source and FREE, if you paid for it, YOU GOT SCAMMED!",
    "Don't worry, Big Chungus has a huge compatiblity with other OSes!",
    "There's this little cool command called \"do\", You can use this to perform bash/cmd/zsh tasks! like clear/cls.",
    "Do People Actually Read These?",
    "Remember, Python 3.10 or later!",
    "Imagine if we made Chungus bootable, that would be impossible since python's too high-level'd",
    "Chungle is VERY fast, Try running discord on it ;)",
    "don't forget pythonOS! pythonOS too! https://github.com/Iemane291/pythonOS",
    "You know Chungus has lua support, right? right??",
    "Did you know Chungus was originally called OS, then MiniOS?",
    "NUG (Mini, Arezalgamer89)'s first product was a viruslib.",
    "If one of the NUG's products are not in GitHub, they're coded together by Mini and Arezal using live share!"
]
errorcodes = [
        "FILE404", # 0
        "DIR404", # 1
        "TIMED_OUT", # 2
        "SYNTAX_400", # 3
        "401ACTION_!AUTH", # 4
        "FEATURE_402", # 5
        "FUNCTION_403", # 6
        "CODINGSTYLE_405", # 7
        "UNACCEPTABLE", # 8
        "408", # 9
        "SMTH_WRONG_409", # 10
        "R/WHOOSH_410", # 11
        "GIANTLY_FAILURE_413", # 12
        "YOUR_DADS_EXPECTAIONS_ARE_TOO_HIGH_417", # 13
        "IDFK_500", # 14
        "STILL_NOT_THAT_ONE_501", # 15
        "NOPE_NOT_RN_503", # 16
        "WTF_IS_THAT_HTML?_505", # 17
        "DO_NOT_BASTARDIZE_CONSENT_511", # 18
        "OH_WAIT_NOTHING'S_WRONG_100" # 19
    ]










def setOption(optionName, option):

    weirdPath = "files/data"


    with open(weirdPath + "/config.json", "r") as f:
        data = json.load(f)
        data[optionName] = option
    with open(weirdPath + "/config.json", "w") as f:
        json.dump(data, f, indent=4)
        

def reload():
    os.execl(sys.executable, sys.executable, *sys.argv)

def Update():
    updateVar = False
    
    os.system('git pull origin ' + branch + ' --quiet')

    while updateVar is not True:
        os.system('clear')
    updateVar = True

def clear():
    cls = "cls" if os.name == "nt" else "clear"
    os.system(cls)

def get_split(obj, symbol, idx, returnBool: bool):
    if returnBool:
        return bool(obj.split(symbol)[idx].title())
    else:
        return obj.split(symbol)[idx]


def versionCheck():
    if sys.version_info[0] > 3 or sys.version_info[1] < 10:
        print(
            "NOTE: You are running on Python "
            + str(sys.version_info[0])
            + "."
            + str(sys.version_info[1])
        )
        print("Some features might not be working correctly.")
    elif sys.version_info[3] != "final":
        print(
            "WARNING: Your Python "
            + str(sys.version_info[0])
            + "."
            + str(sys.version_info[1])
            + " is not on the FINAL level and you might encounter Unfixable bugs..."
        )
    elif sys.version_info[0] < 3 or sys.version_info[1] < 10:
        raise SystemError(
            "ERROR: ChungOS requires Python 3.10 or higher! You can't run this on "
            + str(sys.version_info[0])
            + "."
            + str(sys.version_info[1])
            + " you idot!"
        )


def get_option(option):
    #coolpath = Path("files/data")
    with open("files/data/config.json", "r") as f:
        data = json.load(f)
        if data.get(option) == "on": return True
        elif data.get(option) == "off": return False
        else: return data.get(option) # Will also return None if can't find!


class errors(): # NOTE: Gus will assume that Github CLI is installed on the computer
    """
    # ERRORS CLASS

    This Class contains all the G/BS's of Death
    """
    def error(code):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.2)
        time.sleep(0.2)
        os.system('cls' if os.name == 'nt' else 'clear')
        match code:
            case "TIMED_OUT":
                print("Timed Out!")
                print("Common reasons:")
                print("""
                LOCAL:
                 - Loading was for was out of 35 range.
                 - A File or Directory caused an overflow
                 - Your HDD/SDD may be slow
                 - Your memory doesn't have enough space to store variables
                
                INTERNET:
                 - Urllib has failed to do just the one job he had.
                 - Your Internet connection is unstable or limited.
                 - You have a Proxy/VPN on.
                 - Unknown.
                 - Python Intrepeter must have made a mistake...
                """)
            case "!AUTH":
                print("Something went wrong, Are you authorized?")
                print("unauthorized")
            case "UNACCEPTABLE":
                print("Code is unacceptable, Please remove any code you added if you did, or contact the devs if you didn't")
                print("Please press enter to quit")
            case "FILE404":
                print("Critical file not found. Please put them back if you removed them")
            case "SYNTAX400":
                print("Critical Syntax Error!")
                print("ENTER to EXIT")
            case "UNADDED":
                print("Function or Feature " + msg +  "are NOT added yet!")
            case "INDEX":
                print(Fore.CYAN + "IndexError" + Fore.WHITE)
                print("Index out of range or invalid.")
                if msg == 'change' or msg == 'edit':
                    print("This is might be because of a bugged command like \"Change\" or \"Edit\"")
                pass
                reload()
            case "SMTH_WRONG":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Something went wrong.")
                    print("MSG: " + msg if not msg == "raise SMTH_WRONG" else "MSG: None")
                    print("ERROR CODE: " + code)
                    print("OS Name " + osName)
                    print("Fallen back to Terminal" if fallBackToTERMINAL is True else "Not fallen to Terminal.")
                    input()
            case "!NET":
                os.system("cls" if os.name == 'nt' else 'clear')
                print(Fore.YELLOW + "WARNING:" + Fore.WHITE)
                print(f"{osName} has made it's attempts and could not connect to the internet.")
                print("Do not worry about this error screen, as it is to inform you that")
                print("you might not be able to perform any online actions and LIKELY CAN get this error repeatedly")
                print("NUG FKM cannot procced any further and needs to be restarted.")
                print("ENTER TO REBOOT" if os.name == 'nt' else "[RETURN] TO REBOOT")
                input()
                reload()
            case "OSFlict":
                while True:
                    print(Fore.LIGHTRED_EX + "OPERATING SYSTEM" + Fore.RED + " ERROR")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    input()
            case _:
                print("the carrot fat fucking bitch has gained down weight, too much tho.")
                time.sleep(0.1)
                print("if you not arezal nor mini get the fuck outta here and explain at https://github.com/ArezalGame89/ChungOS/issues/new/choose")
                time.sleep(0.2)
                i = code # can't fix this
                print("if you are, fix the fucking error [" + i + "]")
                time.sleep(2)
         
            
        

        input()
        exit()
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
def loading():
    lquotes = [
        "Came from a error screen? You can make an issue on the GitHub page.",
        "Love these loading screens? Please contribute if you can and make them better.",
        "Go support Ukraine please. 💛💙",
        "Running out of quotes!",
	    "null",
	    "Make some backup of Settings/Config.JSON if it's Important",
	    "Ran on -4 Billion Devices!",
	    "Logging is very important! As you may find cool stuff",
	    "hi this is arezal editing this on GNU nano <3",
	    "If it weren't obvious, Chungus does have RSS. (its broken)",
	    "Want a challenge? Port this to the NT Framework and make it bootable >:)",
	    "os.system('cls' if os.name == 'nt' else 'clear') IS THE MOST USED LINE!",
	    f"{hostname}, Is this {os.getlogin()}?",
        f"yo mama, {ip_address}, {socket.getaddrinfo}, fatherless.",
        "Unfortunately, These quotes repeating again and again may be annoytin\nsorry.",
        Fore.WHITE + "THIS IS A " + Fore.RED + "TEST" + Fore.WHITE,
    ]
    j = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    if sys.version_info[0] < 3 or sys.version_info[1] < 10:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""

                Little Chungus OS
                    Arezalgamer89
                    Unsupported Python (less-than 3.10)

            """)
            input()
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(random.randint(1, 7)):
        os.system("cls" if os.name == 'nt' else 'clear')
        print(f"""

            Little Chungus OS
              Arezalgamer89
                    Loading...            {lquotes[random.randint(0, 13)]}

        """)
        time.sleep(random.randint(5, 10))
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
loading()

def wait(a):
        time.sleep(a)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""

                                Little Chungus OS
                                  Arezalgamer89
                                 [ Please Wait... ]

        """)


from urllib import request
from urllib import response

if cliOS == 'Windows':
    os.system("title " + osName)
if get_option("debug"):
    Diagnostics = True
else:
    Diagnostics = False
if get_option("security"):
    su = False
else:
    su = True

cwd = os.getcwd()


print("NUG ChungusOS Team 2021-2022")
print(startingquotes[random.randint(0, 16)])
if get_option('autoupdate'): #! PLEASE TURN THIS OFF IF YOU'RE DOING YOUR OWN STUFF.
    Update()
while not shit:
    versionCheck()
    msg = input(Fore.BLUE + username + Fore.YELLOW + "@" + Fore.CYAN + osName + Fore.LIGHTGREEN_EX + "$" + Fore.WHITE + " ")
    try:
        if msg == "time":
            import datetime
            from datetime import *
            print(datetime.datetime.now())
        elif msg == "r":
            reload()
            os.system('cls' if os.name == 'nt' else 'clear')
            wait(random.randint(0, 1))
        elif msg == "fall":
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')
            
            fall = True
            shit = True
        elif msg.startswith('raise'):
            errors.error(msg[6:])

        elif msg.startswith("regedit"):
            fuck = False
            print("WARNING: Editing system variables may result in an error, use this at your own risk.")
            print("WELCOME TO REGEDIT. You can edit keys (in-code variables) in here!")
            while not fuck:
                cocaine = input("What do you want to edit? > ")
                if cocaine in globals():
                    newValue = input(f"What do you want to edit {cocaine} (currently {str(globals()[cocaine])}) to? ")
                    globals()[cocaine] =  newValue
                elif cocaine == '':
                    print()
                elif cocaine == 'exit':


                    pass
                    break
                elif cocaine == 'list': print('\n'.join(globals()))
                else:
                     print(f"could not find \"{cocaine}\"")
        elif msg.startswith("help"):
            match msg[5:]:
                case ".":
                    print(Fore.WHITE + "." + Fore.YELLOW + "<" + Fore.BLUE + "app" + Fore.YELLOW + ">" + Fore.WHITE)
                    print("Starts a program file in files/programs")
                    print("Only the filename (Case-Sensitive) should be typen, and the extension MUST be .py")
                    print("If you're looking for lua scripts, that's run-lua(file)")
        elif msg.startswith("."):
            os.chdir("files/programs")
            if os.name == 'nt':
                os.system('py ' + msg[1:] + '.py')
            else:
                os.system('python3 ' + msg[1:] + '.py')
            for i in range(2):
                os.chdir("..")
        elif msg == "browser" or msg == 'chungle':
            match cliOS():
                case "Windows": os.system("py files/programs/Chungle.py")
                case "Darwin": os.system("python3 files/programs/Chungle.py")
                case "Linux": os.system("python files/programs/Chungle.py")
        elif msg == "update":
            os.system("git pull origin master --quiet")
            if cliOS() == "Windows":
                os.system("py Main.py")
            elif cliOS() == "Darwin":
                os.system("python3 Main.py")
        elif msg.startswith("do"):
            if cliOS() == "Darwin" or cliOS() == "Linux" and doneIntro == False:
                if get_option('colors') is True:
                    print(Fore.YELLOW + "WARNING: " + Fore.WHITE + "you're on mac or linux so be sure to type sudo")
                else:

                    print(Fore.WHITE + "WARNING: " + Fore.WHITE + "you're on mac or linux so be sure to type sudo")
            print(Fore.WHITE)
            os.system(msg[3:])
            if random.randint(0, 100000000000000000000000000) == 1:
                fallBackToTERMINAL = True

#           elif msg.startswith("playsound"):
#               os.chdir("assets/sounds/")
#               if "--bg" in msg.split(" "):
#                   for thing in msg.split(" "):
#                       if not thing.startswith("--") and thing.endswith(".wav"):
#                           playsound(thing, False)
#               else:
#                   for thing in msg.split(" "):
#                       if not thing.startswith("--") and thing.endswith(".wav"):
#                           playsound(thing)
#               for i in range(2):
#                   os.chdir("..")

        elif msg == "ls" or msg == "dir":
            # print("Directory " + os.curdir + " is " + os.path + " and has nil volume.")
            print(Fore.WHITE + "Listing PATH where the Main.py executes in.")
            print("\n".join(os.listdir()))
        elif msg == "version":
            print(
                """
            ChungOS (ChungusOS) 1.1.0

            Under MIT License by
            Mini & Arezalgamer89
            """
            )
        elif msg.startswith("settings --"):
            if msg[11:] == "help":
                print(
                    "colors - Change if you want colored text or not. Recommended to turn off if colorblind or causes eyestrains"
                )
            elif msg[11:] == "version":
                print("NUG ChungOS version: 1.0\nChungOS version: 0.0.1")
            else:
                print(Fore.WHITE + "Wrong Syntax")
                pass
        elif msg.endswith("()"):
            {msg}()
        elif msg == "memory":
            from psutil import Process
            curMemory = Process(os.getpid())
            if get_option("colors"):
                print(Fore.LIGHTBLUE_EX + "Memory in kilobytes: " + str(curMemory.memory_info().rss / 1000))
            else:
                print("Memory in kilobytes: " + str(curMemory.memory_info().rss / 1000))

        elif msg == "reload":
            os.system("py main.py" if os.name == 'nt' else 'python3 main.py')

        elif msg.startswith("change"):
            if msg.split(" ")[1] == "--help":
                print(
                    "colors - This affects if you want colored text or not, recommended to turn off incase this causes eyestrains or if your colorblind.\n"
                )
            else:
                newoption = None
                if msg.split(" ")[2].lower() == "false":
                    newoption = False
                elif msg.split(" ")[2].lower() == "true":
                    newoption = True
                if get_option(msg.split(" ")[1].lower()) is not None:
                    setOption(msg.split(" ")[1].lower(), newoption)
                    try:
                        print("Changed option [ " + msg.split(" ")[1].lower() + " ] --> " + newoption)
                    except:
                        print("Changed Option.")
                else:
                    print("That is not a valid option.")
        elif msg.startswith('~'):
            lua.eval(msg[1:])

        elif msg == "halt": # There's a few ways we can do this, so let's make it random!
            if cliOS() == "Darwin" or cliOS() == "Mac" or cliOS() == "Linux":
                os.system("halt")
                exit()
            choice = random.randint(1, 3)

            if choice == 1:
                if Diagnostics:
                    print("Chose 1")
                shit = False
            elif choice == 2:
                if Diagnostics:
                    print("Chose 2")
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
            elif choice == 3: # just... exit?
                if Diagnostics:
                    print("Chose 3")
                exit()
        elif msg == "exit":
            if Diagnostics is True and random.randint(1, 1000) == 1:
                print(
                    Fore.RED
                    + "G"
                    + Fore.BLUE
                    + "o"
                    + Fore.GREEN
                    + "o"
                    + Fore.CYAN
                    + "d"
                    + Fore.LIGHTMAGENTA_EX
                    + "b"
                    + Fore.LIGHTYELLOW_EX
                    + "y"
                    + Fore.LIGHTRED_EX
                    + "e"
                    + Fore.WHITE
                    + " User! <3"
                )
            if get_option('acpi'):
                exit()
            else:
                time.sleep(random.randint(1, 10))
                equotes = [
                    "Safe and Sound!",
                    "Cya next time!",
                    "Off to other stuff...",
                    "You better disown ACPI.",
                    "Also check PythonOS [https://github.com/Iemane291/pythonOS]",
                    "Off to needing help? Check our discord {https://discord.gg/yN7D4hnJQ6}",
                    f"I am rapidly approaching your location right now {ip_address}"
                    ]
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""

                    Little Chungus OS
                    Arezalgamer89
                            It's safe to exit the terminal now            
                        {equotes[random.randint(0, 6)]}

                    """)
                    time.sleep(99999)

        elif msg.startswith("chung --"):
            if msg[8:] == "discord":
                webbrowser.open_new_tab("https://discord.gg/mz3HmzP5ac")
            elif msg[8:] == "version":
                print("NUG ChungOS version - 0.0.1\nBrug Bootloader v0.1")
        elif msg == "run-lua":
            os.chdir("files/scripts/")
            for i in os.listdir("files/scripts/"):
                if i.endswith(".lua"):
                    with open(i, "r") as f:
                        lua.eval(str(f.read()))
            for i in range(3):
                os.chdir("..")
        elif msg == "os":
            print(cliOS().replace("Darwin", "Mac"))
        elif msg.startswith("run-luafile") and msg.endswith(".lua"): 
            if Diagnostics is True:
                if random.randint(1, 50) == 1 and get_option("easter"):
                    logging.debug("Ran the " + msg + " with our Trusty Lua Runtime!")
                else:
                    logging.debug("Ran:", msg)
            os.chdir("files/scripts/")
            with open(msg[12:], "r") as f:
                try:
                    lua.eval(str(f.read()))
                except Exception as errno:
                    print("Unfortunately, " + errno)
                except:
                    print(f"Unluafortunately, bad stuff happened and we can't show it :p")
            for i in range(3):
                os.chdir("..")

        elif msg.startswith("mkdir"):
            try:
                os.system(
                    "mkdir " + str(msg[6:])
                )  # we are using str() method incase the directory name is a number lol.
            except IndexError:
                print("Could not make directory.")
        elif bool(msg) is False:  # i love overcomplicating things.
            # This basically means '' - Arezalgamer89
            pass

        else:
            qmiss = [
                f"{msg}'s not really a thing y'know...",
                f"Never heard of {msg}.",
                f"{msg}, must be a typo?",
                f"Is {msg} even added?",
                f"if you want {msg} and it's not a typo. open up a issue!",
                "Yeah no, that doesn't exist bro...",
                None,
                1,
                f"{msg}... *sad noises*"
            ]
            print(qmiss[random.randint(0,9)])
    except ModuleNotFoundError:
        errors.error("FILE404")
    except IndexError:
        errors.error("INDEX")
    except PermissionError:
        errors.error("!AUTH")
    except OSError:
        errors.error("OSFlict")
    except IndentationError:
        errors.error("SYNTAX400")
    except SystemError:
        errors.error("SMTH_WRONG")
    except TypeError:
        errors.error("SYNTAX400")
    except NameError:
        errors.error("UNACCEPTABLE")
    except KeyboardInterrupt:
        if get_option("easter") and random.randint(1, 100000) == 1:
            print("Bro you should have just used exit :/")
        exit()
    except EOFError:
        errors.error('INDEX')
    except Exception as err:
        print(Fore.RED + "Error: " + Fore.LIGHTYELLOW_EX + err + Fore.WHITE)

while shit and fall:
    msg = ""
    msg = input(Fore.LIGHTWHITE_EX + "$ " + Fore.WHITE)
    match msg:
        case "unfall":
            os.system("cls" if os.name == 'nt' else "clear")
            shit = False
            msg = ""
            fall = False
            os.system('py Main.py' if os.name == 'nt' else 'clear')
        case _:
            os.system(msg)