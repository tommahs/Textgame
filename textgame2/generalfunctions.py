# functions required in multiple occassions of the game

def clearScreen():
    import subprocess
    subprocess.call('clear', shell=True)
# clearScreen()

def anyKey():
    import subprocess
    print('\nPress any key to continue.')
    subprocess.call('read', shell=True)
# anyKey()


#### Defining ability modifier:
## ability score -10, /2 + extra modifiers if applyable
def abilitymodifier(ability):
    modifier = round((ability -10) /2)
    return modifier


###### Fighting ######
def diceEncounter():
    import random
    dice = 0
    counter = 0
    while counter <= 3:
        roll = random.randrange(1,20)
        dice += roll
        counter +=1
    return dice

#####
def dice6():
    import random
    dice = 0
    roll = random.randint(1,7)
    dice = roll
    return dice

def dice20():
    import random
    dice = 0
    roll = random.randint(1,21)
    dice = roll
    return dice