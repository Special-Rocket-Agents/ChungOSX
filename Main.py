import errorc
from errorc import error
osName = "ChungOSX"  # Keep in mind that this is shitto different than os.name
version = "1.0"
fall = False
branch = 'master' # GitHub Main Branch.


startingquotes = [
    "Too stuck? Make another issue! We don't have a Discord Guild",
    "You can simulate the error screens by the \"raise <code>\" command!",
    "If you need a buggier version of ChungOSB, go try FALL command.",
    "ChungOSB relies on git",
    "Suggest us features.",
    "Yes it is free.",
    "Worry, ChungOS is incompatible with other OSes",
    "There's this little cool command called \"do\", You can use this to perform bash/cmd/zsh tasks! like clear/cls.",
    "So People Actually Read These.",
    "Remember, Python 3.10 or later!",
    "Imagine if we made ChungOS bootable, that would be impossible since python's too high-level",
    "Chungle is MegaFast™ Certified",
    "PythonOS is dead.",
    "You know ChungOSX has lua support, right? right??",
    "ChungOSX is not ChungOSB",
    "SRA's first product was KawaiiXOR.",
    "If one of the SRA's products are not in GitHub, they're coded together by Mini and Arezal using live share!"
]







import os
import sys
import time


def setOption(optionName, option):

    weirdPath = "files/data"


    with open(weirdPath + "/config.json", "r") as f:
        data = json.load(f)
        data[optionName] = option
    with open(weirdPath + "/config.json", "w") as f:
        json.dump(data, f, indent=4)
        
shit = False
quoteshit = False
doneIntro = False


def reload():
    os.execl(sys.executable, sys.executable, *sys.argv)

def clear():
    cles = "cls" if os.name == "nt" else "clear"
    os.system(cles)

def get_split(obj, symbol, idx, returnBool: bool):
    if returnBool:
        return bool(obj.split(symbol)[idx].title())
    else:
        return obj.split(symbol)[idx]

def Update():
    updateVar = False
    
    os.system('git pull origin ' + branch + ' --quiet')

    while updateVar is not True:
        clear()
    updateVar = True


def versionCheck():
    if sys.version_info[3] != "final":
        print(
            "WARNING: Your Python "
            + str(sys.version_info[0])
            + "."
            + str(sys.version_info[1])
            + " is not on the FINAL level and you might encounter Unfixable bugs..."
        )
    elif sys.version_info[0] < 3 or sys.version_info[1] < 10:
        error("UNDERVER", "UNDERVER", msg)


def get_option(option):
    #coolpath = Path("files/data")
    with open("files/data/config.json", "r") as f:
        data = json.load(f)
        if data.get(option) == "on": return True
        elif data.get(option) == "off": return False
        else: return data.get(option) # Will also return None if can't find!



import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
from colorama import Fore, Back, Style # Color
import random
##### LOADING
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
    f"yo mama ain't fat",
    "Unfortunately, These quotes repeating again and again may be annoying sorry.",
    Fore.WHITE + "THIS IS A " + Fore.RED + "TEST" + Fore.WHITE,
]
j = 0
os.system('cls' if os.name == 'nt' else 'clear')
os.system("cls" if os.name == 'nt' else 'clear')
print(f"""
        The ChungOSX
    Arezalgamer89 x SRA
        Loading...            {lquotes[random.randint(0, 13)]}
    """)
from calendar import c
from errno import errorcode
import locale
import logging
from operator import sub
import random
import subprocess
import webbrowser
from xml.etree.ElementTree import TreeBuilder
import colorama
import json
import sys
import time
from datetime import datetime # Clock 

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from lupa import LuaRuntime
from PyQt5.QtGui import QIcon, QKeySequence
from platform import system as cliOS # Standing for ClientOS
from pathlib import Path # Path
from webbrowser import open_new_tab # Your Browser
lua = LuaRuntime()
username = os.getlogin()
curMemory = Process(os.getpid())
time.sleep(0.2)
os.system('cls' if os.name == 'nt' else 'clear')

def wait(a):
        time.sleep(a)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""

                                     ChungOSX
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


print("SRA ChungOS Team 2021-2023")
print("Courtesy of Arezalgamer89")
print(startingquotes[random.randint(0, 16)])
if get_option('autoupdate'): #! PLEASE TURN THIS OFF IF YOU'RE DOING YOUR OWN STUFF.
    Update()
while True:
    versionCheck()
    msg = input(Fore.BLUE + username + Fore.YELLOW + "@" + Fore.CYAN + osName + Fore.LIGHTGREEN_EX + "$" + Fore.WHITE + " ")
    try:
        if msg == "date":
            from datetime import *
            print(date.today())
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
            error(msg.upper()[6:], "EXCEPTION_INTUNED", msg)

        elif msg.startswith("regedit"):
            wait(0.4)
            if msg[7:].lower() == "list":
                print('\n'.join(globals()))
                pass
            fuck = False
            print("WARNING: Editing system variables may result in an error, use this at your own risk.")
            print("WELCOME TO REGEDIT. You can edit keys (in-code variables) in here!")
            while not fuck:
                cocaine = input("What do you want to edit? > ")
                if cocaine in globals():
                    newValue = input(f"What do you want to edit {cocaine} (currently {str(globals()[cocaine])}) to? ")
                    globals()[cocaine] = newValue
                elif cocaine == '':
                    print()
                elif cocaine == 'exit':


                    pass
                    break
                elif cocaine == 'list': print('\n'.join(globals()))
                else:
                     print(f"could not find \"{cocaine}\"")
        elif msg.lower() in globals():
            print(globals()[msg])
        elif msg.startswith("help"):
            match msg[5:]:
                case ".":
                    print(Fore.WHITE + "." + Fore.YELLOW + "<" + Fore.BLUE + "app" + Fore.YELLOW + ">" + Fore.WHITE)
                    print("Starts a program file in files/programs")
                    print("Only the filename (Case-Sensitive) should be typen, and the extension MUST be .py")
                    print("If you're looking for lua scripts, that's run-lua(file)")
        elif msg.startswith("."):
            os.chdir("files/programs")
            try:
                if os.name == 'nt':
                    os.system('py ' + msg[1:] + '.py')
                else:
                    os.system('python3 ' + msg[1:] + '.py')
            except Exception as err:
                print(f"{osName} was unable to launch {msg[1:]}.")
                error('SMTH_WRONG', f"ChungOSX was unable to launch a Python program. Exception: {err}", msg)
            finally:
                for i in range(2):
                    os.chdir("..")
        elif msg == "browser" or msg == 'chungle':
            match cliOS():
                case "Windows": os.system("py files/programs/Chungle.py")
                case "Darwin": os.system("python3 files/programs/Chungle.py")
                case "Linux": os.system("python files/programs/Chungle.py")
        elif msg.startswith("do"):
            if cliOS() == "Darwin" or cliOS() == "Linux" and doneIntro == False:
                if get_option('colors') is True:
                    print(Fore.YELLOW + "WARNING: " + Fore.WHITE + "you're on mac or linux so be sure to type sudo")
                else:

                    print(Fore.WHITE + "WARNING: " + Fore.WHITE + "you're on mac or linux so be sure to type sudo")
            print(Fore.WHITE)
            os.system(msg[3:])


        elif msg == "ls" or msg == "dir":
            # print("Directory " + os.curdir + " is " + os.path + " and has nil volume.")
            print(Fore.WHITE + "Listing PATH where the Main.py executes in.")
            print("\n".join(os.listdir()))
        
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
            try:
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
            except Exception as errno:
                error("INDEX", errno, msg)
        elif msg.startswith('~'):
            try:
                lua.eval(msg[1:])
            except Exception as er:
                error("SMTH_WRONG", er, msg)

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
                time.sleep(random.randint(1, 5))
                equotes = [
                    "Safe to quit",
                    "Will see you come, go and come and again...",
                    "Now onto that line of code...",
                    "No ACPI huh?",
                    "PythonOS... does not exist.",
                    "Off to needing help? Check out non-existent wiki!",
                    f"Did you know that I am rapidly approaching your location right now {ip_address}?"
                    "Stop messing brother, We must fight the MPLA!"
                    "Big big chungus, big chungus big chungus!"
                    "Remember, This is a buggy mess!"
                    "halt"
                    ]
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(equotes[random.randint(0, 10)])
                    time.sleep(1)

        elif msg.startswith("chung"):
            if msg[6:] == "discord":
                # webbrowser.open_new_tab("https://discord.gg/mz3HmzP5ac")
                print("That server does not exist!")
            elif msg[6:] == "version":
                print(f"SRA {osName} 2021 - 2023")
                print("MIT License")
                print("~ Arezalgamer89")
            elif msg[6:] == "os":
                print("You're running on " + cliOS().replace("Darwin", "Mac"))
                if os.name == 'nt':
                    print("Would you like more graphical info? (y/n)")
                    i = input("").lower()
                    if i == 'y':
                        subprocess.run('winver')
                    else:
                        pass
            elif msg[6:].lower() == "sra":
                print("(c) Special Rocket Agency 2021 - 2023")
                print("ChungOS and ChungOSX are MIT Licensed")
                print("KawaiiXOR and Hookies are not related to this.")
            else:
                print("The ChungOS Infosystem")
                print("Usage: chung <discord | version | os | sra>")
        elif msg == "run-lua":
            os.chdir("files/scripts/")
            for i in os.listdir("files/scripts/"):
                if i.endswith(".lua"):
                    with open(i, "r") as f:
                        lua.eval(str(f.read()))
            for i in range(3):
                os.chdir("..")
        elif msg == "os":
            print("You're running on " + cliOS().replace("Darwin", "Mac"))
            if os.name == 'nt':
                print("Would you like more graphical info? (y/n)")
                i = input("").lower()
                if i == 'y':
                    subprocess.run('winver')
                else:
                    pass
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
                f"{msg}... *sad noises*"
            ]
            print(qmiss[random.randint(0,4)])
    except ModuleNotFoundError as err:
        error("FILE404", err, msg)
    except IndexError as err:
        error("INDEX", err, msg)
    except PermissionError as err:
        error("!AUTH", err, msg)
    except OSError as err:
        error("OSFLICT", err, msg)
    except IndentationError as err:
        error("SYNTAX400", err, msg)
    except SystemError as err:
        error("SMTH_WRONG", err, msg)
    except TypeError as err:
        error("SYNTAX400", err, msg)
    except AttributeError as err:
        error("SYNTAX400", err, msg)
    except NameError as err:
        error("UNACCEPTABLE", err, msg)
    except KeyboardInterrupt:
        if get_option("easter"):
            print("Bro you should have just used exit :/")
        exit()
    except EOFError:
        error('END_OF_FILE_AND_LIFE')
    except Exception as err:
        print("EXCEPTION_OCCURED", err, msg)

while shit and fall:
    msg:str = ""
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
