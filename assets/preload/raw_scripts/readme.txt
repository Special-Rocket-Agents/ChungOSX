This is the directory where you can write and put lua files to mod/change/remove your experiences

How does it work?

Put your lua scripts in this folder and the operating system will detect and execute it
NOTES:
    - Your files must end in .lua or ChungusOS cannot execute it. This Applies for both run-lua and run-luafile
    - There is no "DIFFERENT" API, It's the normal lua that you find at https://www.lua.org/

How to Execute?
    - run-lua
        This command takes /raw_scripts temporarily as *global* and launch all the scripts
        NOTE: This may be marked deprecated and soon-to-be-removed
    - run-luafile [file]
        This command executes the given filename of the script. 
        NOTE: Currently it only accepts string (words)
              The script MUST end in '.lua' otherwise even the command doesn't work!
              Turning on Diagnostics Mode will tell you what file you ran.