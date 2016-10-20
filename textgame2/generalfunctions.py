# functions required in multiple occassions of the game

def clearScreen():
    import subprocess
    subprocess.call('clear', shell=True)
clearScreen()

def anyKey():
    import subprocess
    print('\nPress any key to continue.')
    subprocess.call('read', shell=True)
# anyKey()


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

