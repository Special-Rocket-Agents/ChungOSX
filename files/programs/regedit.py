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