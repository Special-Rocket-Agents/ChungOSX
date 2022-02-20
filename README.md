# ChungOS

## What is this?
Python Script to stand as a terminal Operating system. But instead of being booted off your PC. It runs STRAIGHT on your Terminal/Command Prompt!

## How to use?

When you run ChungOS. You appear with something similar to this:
```
__main__>
```

To interact, run commands like 
```sh
mkdir <your-dir-name>
run-lua
run-luafile
cmd # ONLY FOR WINDOWS
bash # ONLY FOR LINUX
terminal # ONLY FOR MAC (DARWIN)
```
# Installation

1. Make sure you have [Python 3.9](https://www.python.org/downloads/) or greater installed.

2. CD Into the ChungOS Folder

3. type in `pip3 install -r requirements.txt` to install the required modules.

4. Launch the Main.py file in your ways
   
    WINDOWS: `py Main.py`
  
    LINUX: Ditto
  
    MAC: @ImNew123 Please make a PR here
    
5. Profit

# Lua Stuff

You can run lua scripts in chungOS, just add them in `assets/preload/raw_scripts/` and make sure they end with `.lua`.

Let's look at this basic script:
```lua
print("hi")
```

That would print hi in chungOS. You can run unmodified lua (using `lupa`)

To run lua scripts, you can do `run-lua` and it will automatically look for every file in `assets/preload/raw_scripts/` that ends with .lua and run it
