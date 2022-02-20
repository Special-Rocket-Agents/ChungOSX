# ChungOS
Python (Terminal) Operating System. AKA LilChungus, ChungusOS.


# Lua Stuff

You can run lua scripts in chungOS, just add them in `assets/preload/raw_scripts/` and make sure they end with `.lua`.

Let's look at this basic script:
```lua
print("hi")
```

That would print hi in chungOS. You can run unmodified lua (using `lupa`)

To run lua scripts, you can do `run-lua` and it will automatically look for every file in `assets/preload/raw_scripts/` that ends with .lua
