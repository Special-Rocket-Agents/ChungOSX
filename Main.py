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
sysdir = "files"  # SysDir. This Directory contains Chn.Preloader and Datadir.
datadir = sysdir + "/data"  # Datadir, The OS will not operate without this directory
osName = "ChungOS"  # Keep in mind that this is shitto different than os.name
fallBackToTERMINAL = False  # (False by Default) If set to true, uses your OS's terminal instead, whatever it may be bash, or CMD, or pw3yyyyysh
branch = 'master' # GitHub Main Branch.


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
        



def Update():
    updateVar = False
    
    os.system('git pull origin ' + branch + ' --quiet')

    while updateVar is not True:
        os.system('clear')
    updateVar = True

def clear():
    cls = "cls" if os.name == "nt" else "clear"
    subprocess.run(cls)

def reset():
    shit = True
    shit = False
    return None


def get_split(obj, symbol, idx, returnBool: bool):
    if returnBool:
        return bool(obj.split(symbol)[idx].title())
    else:
        return obj.split(symbol)[idx]


def versionCheck():
    if sys.version_info[0] > 3 or sys.version_info[1] < 8:
        print(
            "NOTE: You are running on Python "
            + str(sys.version_info[0])
            + "."
            + str(sys.version_info[1])
        )
        print("Some features might not be working correctly.")
        pass
    elif sys.version_info[3] != "final":
        print(
            "WARNING: Your Python "
            + str(sys.version_info[0])
            + "."
            + str(sys.version_info[1])
            + " is not on the FINAL level and you might encounter Unfixable bugs..."
        )
    elif sys.version_info[0] < 3 or sys.version_info[1] < 7:
        raise SystemError(
            "ERROR: ChungOS requires Python 3.8 or higher! You can't run this on "
            + str(sys.version_info[0])
            + "."
            + str(sys.version_info[1])
            + " you idot!"
        )


def get_option(obj):
    os.chdir("files/data/")
    with open("config.json", "r") as f:
        fileData = json.load(f)
        for i in range(2):
            os.chdir("..")
        if fileData["colors"]:
            colors = True
            colorama.init(autoreset=True)
        else:
            colors = False
            colorama.init(
                autoreset=True, strip=True, convert=False
            )  # even if un-coloring proccess fails. colorama's not gonna touch a single color!
        return fileData.get(obj)  # returns none if cant find


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
                os.system("py Main.py" if os.name == 'nt' else "python3 Main.py")
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

def loading():
    j = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    if sys.version_info[0] < 3 or sys.version_info[1] < 10:
        print("""

                                Little Chungus OS
                                  Arezalgamer89
                                    [ ERROR ]
                               [ NOT_3.10_AND_L8ER ]
        """)
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(random.randint(0, 8)):
        os.system('cls' if os.name == 'nt' else 'clear')
        j = j + 1
        if j > 35:
            errors.error(str('TIMED_OUT'))
            #loadingTooLong()

        print("""

                                Little Chungus OS
                                  Arezalgamer89
                                       [ | ]

        """)
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""

                                Little Chungus OS
                                  Arezalgamer89
                                       [ / ]

        """)
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""

                                Little Chungus OS
                                  Arezalgamer89
                                       [ - ]

        """)
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""

                                Little Chungus OS
                                  Arezalgamer89
                                       [ \ ]

        """)
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
    print("""
                                Little Chungus OS
                                  Arezalgamer89
                                  [    Done   ]
    """)
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
def loadingTooLong():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""

                                Little Chungus OS
                                  Arezalgamer89
                            [ This is taking too long... ]

        """)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(random.randint(0, 10))
    for i in range(40):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""

                                Little Chungus OS
                                  Arezalgamer89
                                 [ Please Wait ]

        """)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.3)
        print("""

                                Little Chungus OS
                                  Arezalgamer89
                                 [ Please Wait. ]

        """)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.3)
        print("""

                                Little Chungus OS
                                  Arezalgamer89
                                 [ Please Wait.. ]

        """)
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""

                                Little Chungus OS
                                  Arezalgamer89
                                 [ Please Wait... ]

        """)
        os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""

                                Little Chungus OS
                                  Arezalgamer89
                                [ Done (TIMED_OUT) ]

        """)
    input()
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

        
if get_option("debug"):
    Diagnostics = True
else:
    Diagnostics = False
if get_option("security"):
    su = False
else:
    su = True







while not shit:
    versionCheck()
    user = os.getlogin()
    try:
        if get_option("colors"):
            msg = input(
                Fore.YELLOW + os.getcwd() + Fore.RED + ">>>" + Fore.WHITE + " "
            )
        else:
            if bool(Diagnostics) is False:
                msg = input(Fore.WHITE + user + "@" + osName + " >>> ")
            else:
                msg = input(Fore.WHITE + os.getcwd() + ">>> ")
    except PermissionError:
        msg = input(osName.lower() + "$")
    if msg == "time":
        import datetime
        from datetime import *
        print(datetime.datetime.now())
    elif msg == "r":
        reset()
        os.system('cls' if os.name == 'nt' else 'clear')
        wait(random.randint(0.1, 1))
    elif msg == "fall":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""

                                Little Chungus OS
                                  Arezalgamer89
                            [ Fallin' down terminal... ]

        """)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # shit = True
        # Uncommenting this would terminate the entire system!
        fallBackToTERMINAL = True
    elif msg.startswith('raise'):
        errors.error(msg[6:])
    
    elif msg.startswith("."):
        os.chdir("files/programs")
        if os.name == 'nt':
            os.system('py ' + msg[1:] + '.py')
        else:
            os.system('python3 ' + msg[1:] + '.py')
        for i in range(2):
            os.chdir("..")
    elif msg == "browser" or msg == 'chungle':
        class MainWindow(QMainWindow):
            def __init__(self):
                super(MainWindow, self).__init__()
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl("https://google.com"))
                self.setCentralWidget(self.browser)
                self.showMaximized()
                navbar = QToolBar()
                self.addToolBar(navbar)
                back_btn = QAction("Back", self)
                back_btn.triggered.connect(self.browser.back)
                navbar.addAction(back_btn)
                forward_btn = QAction("Foward", self)
                forward_btn.triggered.connect(self.browser.forward)
                navbar.addAction(forward_btn)
                reload_btn = QAction("Reload", self)
                reload_btn.triggered.connect(self.browser.reload)
                navbar.addAction(reload_btn)
                home_btn = QAction("Home", self)
                home_btn.triggered.connect(self.navigate_home)
                navbar.addAction(home_btn)
                self.url_bar = QLineEdit()
                self.url_bar.returnPressed.connect(self.nav_url)
                navbar.addWidget(self.url_bar)
            def navigate_home(self):
                self.browser.setUrl(QUrl("https://google.com"))
            def nav_url(self):
                url = self.url_bar.text()
                if url[0:7] != "https://":
                    self.browser.setUrl(QUrl("https://" + url))
                else:
                    self.browser.setUrl(QUrl(url))
                    for i in range(2):
                        print(url)
        app = QApplication(sys.argv)
        QApplication.setApplicationName("Chungle")
        window = MainWindow()
        app.exec_()
    elif msg == "update":
        subprocess.run("git pull origin master --quiet")
        if cliOS() == "Windows":
            subprocess.run("py Main.py")
        elif cliOS() == "Darwin":
            subprocess.run("python3 Main.py")
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
    
#       elif msg.startswith("playsound"):
#           os.chdir("assets/sounds/")
#           if "--bg" in msg.split(" "):
#               for thing in msg.split(" "):
#                   if not thing.startswith("--") and thing.endswith(".wav"):
#                       playsound(thing, False)
#           else:
#               for thing in msg.split(" "):
#                   if not thing.startswith("--") and thing.endswith(".wav"):
#                       playsound(thing)
#           for i in range(2):
#               os.chdir("..")

    elif msg == "ls" or msg == "dir":
        # print("Directory " + os.curdir + " is " + os.path + " and has nil volume.")
        print(Fore.WHITE + "Listing PATH where the Main.py executes in.")
        print("\n".join(os.listdir()))
    elif msg == "version":
        print(
            """
        ChungOS (ChungusOS) 0.0.1
        
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
        str(msg)
    elif msg == "memory":
        from psutil import Process
        curMemory = Process(os.getpid())
        if get_option("colors"):
            print(Fore.LIGHTBLUE_EX + "Memory in kilobytes: " + str(curMemory.memory_info().rss / 1000))
        else:
            print("Memory in kilobytes: " + str(curMemory.memory_info().rss / 1000))
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
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("""
                                Little Chungus OS
                                  Arezalgamer89
                    [    It is now safe to exit the terminal   ]
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

    elif msg.startswith('switch'):
        if msg[7:] == '--help':
            print("""
            Switch Versions of ChungOS!
            [ og ] - Original version. Maintained by Arezalgamer89
            [ rw ] - PythonOS, Starting out as an simple rewrite (WARNING: P-OS may not provide switching)
            NOTE: Requires Git and Stable Internet Connection
            """)
        else:
            if msg[7:] == 'og':
                # To do: erase the whole directory and git clone
                subprocess.run('git pull origin master')
                sys.exit(0)
            elif msg[7:] == 'rw':
                # doing this later cuz too hard
                pass
    elif msg.startswith("mkdir"):
        try:
            subprocess.run(
                "mkdir " + str(msg[6:])
            )  # we are using str() method incase the directory name is a number lol.
        except IndexError:
            print("Could not make directory.")
    elif bool(msg) is False:  # i love overcomplicating things.
        # This basically means '' - Arezalgamer89
        pass
            
    else:
        print(Fore.WHITE + "'" + msg + "' Command or LuaRT File could not be found")

