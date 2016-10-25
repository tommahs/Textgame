from random import randint
import generalfunctions, party, actions
currentlocation = 'forest'
party = party.createparty()
def maincombat(party, enemies):
    # Turnorder
    # Per turn -> players get menu
    #          -> enemies attack player
    # if hp reaches 0, turn gets skipped
    #

    while True:
        print('What do you want to do? \n1. Fight\n2. Use item\n3. Run')
        choice = input('Choice : ')
        if '1' in choice:
            choice1()
        elif '2' in choice:
            choice2()
        elif '3' in choice:
            choice3()
        # elif '4' in choice:
        #     choice4()
        else:
            exit()

def choice1(): #Fight an enemy
    generalfunctions.clearScreen()
    fight.chooseenemy()
    fight.combat(enemy, char)
    generalfunctions.clearScreen()

def choice2(): # Use item
    print("Not implemented")
def choice3(): #run from fight
    generalfunctions.clearScreen()
    print('You run away from the fight.')


# def showstats(char): #Show stats
#     # playerfunctions.stats(char)
#     generalfunctions.anyKey()
#
# def choice4():  # teleport
#     generalfunctions.clearScreen()
#     global currentlocation
#     # currentlocation = map.chloc()
#     generalfunctions.clearScreen()
main()