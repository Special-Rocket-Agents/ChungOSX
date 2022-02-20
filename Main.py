import datetime
import logging
import os
import json
import time
import colorama
import random
import webbrowser
import platform
import sys
import Brug

from configparser import ConfigParser
from colorama import Fore, Back, Style
from lupa import LuaRuntime
from playsound import playsound

colorama.init(
    autoreset=True
)  # initialize the fucking thing since im an asshole - mini LFMAOAOAOO
shit = False
doneIntro = False
lua = LuaRuntime()
config = ConfigParser()

###### INTERNAL SETTINGS ######
sysdir = "assets"  # SysDir. This Directory contains Chn.Preloader and Datadir.
preloader = (
    sysdir + "/preload"
)  # Chn.Preloader. This PATH holds all the important directories
datadir = preloader + "/data"  # Datadir, The OS will not operate without this directory
osName = "ChungOS"  # Keep in mind that this is shitto different than os.name
fallBackToTERMINAL = False  # (False by Default) If set to true, uses your OS's terminal instead, whatever it may be bash, or CMD, or pw3yyyyysh
Diagnostics = True  # More Important version of Debug Mode in Settings


def get_split(obj, symbol, idx, returnBool: bool):
    if returnBool:
        return bool(obj.split(symbol)[idx].title())
    else:
        return obj.split(symbol)[idx]


def get_option(obj):
    os.chdir("assets/preload/")
    with open("config.json", "r") as f:
        fileData = json.load(f)
        for i in range(2):
            os.chdir("..")
        return fileData[obj]


while not shit:
    if not fallBackToTERMINAL is True:
        try:
            if get_option("colors") == "true":
                msg = input(
                    Fore.YELLOW + __name__ + Fore.RED + ">>>" + Fore.GREEN + " "
                ).lower()
            else:
                msg = input(Fore.WHITE + __name__ + ">>>").lower()
        except PermissionError:
            msg = input(osName.lower() + "$")

        if msg == "time":
            print(datetime.datetime.now())
        elif msg.startswith("playsound"):
            os.chdir("assets/sounds/")
            if "--bg" in msg.split(" "):
                for thing in msg.split(" "):
                    if not thing.startswith("--") and thing.endswith(".wav"):
                        playsound(thing, False)
            else:
                for thing in msg.split(" "):
                    if not thing.startswith("--") and thing.endswith(".wav"):
                        playsound(thing)
            for i in range(2):
                os.chdir("..")
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

        elif msg.startswith("change"):
            try:
                os.chdir("assets/preload/")
                with open("config.json", "r") as f:
                    filedata = json.load(f)
                    filedata[get_split(msg, " ", 1, False).lower()] = get_split(
                        msg, " ", 2, True
                    )
                with open("config.json", "w") as f:
                    json.dump(filedata, f)

                for i in range(2):
                    os.chdir("..")
            except IndexError as e:
                if get_option("colors") == "true":
                    print(Fore.RED + "Error: " + Fore.WHITE + str(e))
                else:
                    print("Error: " + str(e))

        elif msg == "settings":
            print("Welcome to the settings menu.")
            time.sleep(1)
            print("Here you are able to customize your experience.")
            time.sleep(1)
            print("Continue to go to the settings menu?")
            thefuckinginputsinceyallareass = input().lower()

            if thefuckinginputsinceyallareass == "y":
                os.chdir("assets/preload/data")
                print(
                    "Ok, let's input the new options you want. One second let me prepare the list."
                )
                time.sleep(1)  # ffs lets make the usr not wait for long
                killMe = input(
                    "Aha! Got it! Would you like colors to be enabled? (y/n)\n"
                ).lower()
                os.chdir("assets/preload/")
                with open("config.json", "r") as f:
                    curOptions = json.load(f)
                if killMe == "y":
                    curOptions["colors"] = "true"
                elif killMe == "n":
                    curOptions["colors"] = "false"
                # Writes to it
                with open("options.json", "w") as d:
                    json.dump(curOptions, d)
                input()
                for i in range(3):
                    os.chdir("..")

            else:
                pass

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
            exit()

        elif msg.startswith("chung --"):
            if msg[8:] == "discord":
                webbrowser.open_new_tab("https://discord.gg/mz3HmzP5ac")
            elif msg[8:] == "version":
                print(
                    "Nug ChungOS Version - 1.0\nChungOS version - 0.0.1\nBrug Bootloader v0.1"
                )

        elif msg == "run-lua":
            for i in os.listdir("assets/preload/raw_scripts/"):
                os.chdir("assets/preload/raw_scripts/")
                if i.endswith(".lua"):
                    with open(i, "r") as f:
                        lua.eval(str(f.read()))
                for i in range(2):
                    os.chdir("..")
        elif msg.startswith("run-luafile") and msg.endswith(".lua"):
            if Diagnostics is True:
                if random.randint(1, 50) == 1 and get_option("eastereggs") == "true":
                    logging.debug("Ran the " + msg + " with our Trusty Lua Runtime!")
                else:
                    logging.debug("Ran:", msg)
            os.chdir("assets/preload/raw_scripts/")
            with open(msg[12:], "r") as f:
                try:
                    lua.eval(str(f.read()))
                except Exception as errno:
                    print("Unfortunately, " + errno)
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

        elif msg[0:3] in ("exit", "quit"):
            exit()

        elif msg == "power":

            try:
                print("What would you like to do?", os.getlogin() + "?")
                if os.name == "nt":
                    print(
                        """
                    1. Shutdown
                    2. Reboot
                    3. Log Out
                    """
                    )
                killMe = int(input(""))
                if killMe == 1:
                    print("Are you sure you want to shut down? (y/n)")
                    confirm = input().lower()
                    if confirm == "y":
                        os.system(
                            'shutdown /s /hybrid /c "MiniOS has shutdown this P" /t 005'
                        )
                    else:
                        print("Ok then.")
                elif killMe == 2:
                    os.system('shutdown /r /c "MiniOS has reboot this PC" /t 005')
                elif killMe == 3:
                    os.system("shutdown /l /t 000")
                else:
                    print("What would you like to do?", os.getlogin() + "?")
                    print(
                        """
                            1. Reboot
                            2. Lock
                            3. Freeze Computer (Halt)
                        """
                    )
                    killMe = input()
                    if killMe == 1 and not os.name == "nt":
                        if platform.system() == "Darwin":
                            os.system("sudo reboot")
                        else:
                            os.system("reboot")
                    elif killMe == 2 and not os.name == "nt":
                        print(
                            "Are you sure you want to lock miniOS (and potentially your PC too?)"
                        )
                        confirm = input().lower()
                        if confirm == "y":
                            if platform.system() == "Darwin":  # Basically mac
                                os.system(
                                    "/System/Library/CoreServices/Menu\ Extras/user.menu/Contents/Resources/CGSession -suspend"
                                )  # ? Unsure about this...
                            else:
                                os.system("loginctl lock-screen")
                    elif killMe == 3 and not os.name == "nt":
                        print(
                            "Your Computer is Unresponsive now, You must force-shutdown your Mac/PC"
                        )
                        time.sleep(0.5)
                        os.system("halt")

            except Exception as e:
                if get_option("colors") == "true":
                    print(Fore.RED + "ERROR:" + Fore.WHITE + str(e))
                else:
                    print(Fore.WHITE + "ERROR:" + str(e))

        elif msg == "cmd" and platform.system == "Windows":
            try:
                os.system("start")
            except:
                os.system("cmd")
        elif msg == "bash" or msg == "terminal" and platform.system == "Linux":
            os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
        elif msg == "terminal" and platform.system == "Darwin":
            os.system("start")  #! HELP, I NEED HELP WHAT SHOULD I TYPE HERE AAAA

        else:
            print(Fore.WHITE + "'" + msg + "' Command or LuaRT File could not be found")

    else:  # Fallback
        if doneIntro is False:
            if os.name == "nt":
                print(
                    "Welcome to " + osName + "! Use this Terminal to Perform CMD Tasks!"
                )
            else:
                print(
                    "Welcome to "
                    + osName
                    + "! Use the Prompt Below to Perform your Bash/Mac Terminal Tasks!"
                )
        doneIntro = True
        msg = input(">>> ")
        os.system(msg)


def Settings():
    Settings = []  # known to be unused for now...

    print("")
