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
import subprocess

from configparser import ConfigParser
from colorama import Fore, Back, Style
from lupa import LuaRuntime
from playsound import playsound
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

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
    os.chdir("assets/preload/")
    with open("config.json", "r") as f:
        fileData = json.load(f)
        if fileData["colors"] == "true":
            colors = True
            colorama.init(autoreset=True)
        else:
            colors = False
            colorama.init(
                autoreset=True, strip=True, convert=False
            )  # even if un-coloring proccess fails. colorama's not gonna touch a single color!
        for i in range(2):
            os.chdir("..")
        return fileData.get(obj)  # returns none if cant find


while not shit:
    versionCheck()
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
        elif msg == "browser":

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

            while True:
                if platform.system() == "Darwin" or platform.system() == "Linux":
                    subprocess.run("clear")
                elif platform.system() == "Windows":
                    subprocess.run("cls")  # i used a windows laptop once

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
                print("NUG ChungOS version - 0.0.1\nBrug Bootloader v0.1")

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
                subprocess.run(
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
                        subprocess.run(
                            'shutdown /s /hybrid /c "MiniOS has shutdown this P" /t 005'
                        )
                    else:
                        print("Ok then.")
                elif killMe == 2:
                    subprocess.run('shutdown /r /c "MiniOS has reboot this PC" /t 005')
                elif killMe == 3:
                    subprocess.run("shutdown /l /t 000")
                else:
                    print("What would you like to do?", os.getlogin() + "?")
                    print(
                        """
                            1. Reboot
                            2. Lock
                            3. Freeze Computer (Halt)
                        """
                    )
                    killMe = int(input())
                    if killMe == 1 and os.name != "nt":
                        if platform.system() == "Darwin":
                            subprocess.run("sudo reboot")
                        else:
                            subprocess.run("reboot")
                    elif killMe == 2 and os.name != "nt":
                        print(
                            "Are you sure you want to lock miniOS (and potentially your PC too?)"
                        )
                        confirm = input().lower()
                        if confirm == "y":
                            if platform.system() == "Darwin":  # Basically mac
                                subprocess.run(
                                    "/System/Library/CoreServices/Menu\ Extras/user.menu/Contents/Resources/CGSession -suspend"
                                )  # ? Unsure about this...
                            else:
                                subprocess.run("loginctl lock-screen")
                    elif killMe == 3 and os.name != "nt":
                        print(
                            "Your Computer is Unresponsive now, You must force-shutdown your Mac/PC"
                        )
                        time.sleep(0.5)
                        subprocess.run("halt")

            except Exception as e:
                if get_option("colors") == "true":
                    print(Fore.RED + "ERROR:" + Fore.WHITE + str(e))
                else:
                    print(Fore.WHITE + "ERROR:" + str(e))

        elif msg == "cmd" and platform.system == "Windows":
            try:
                subprocess.run("start")
            except:
                subprocess.run("cmd")
        elif msg == "bash" or msg == "terminal" and platform.system == "Linux":
            subprocess.run(
                "gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'"
            )
        elif msg == "terminal" and platform.system == "Darwin":
            subprocess.run("start")  #! HELP, I NEED HELP WHAT SHOULD I TYPE HERE AAAA

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
        subprocess.run(msg)


def Settings():
    Settings = []  # known to be unused for now...

    print("")
