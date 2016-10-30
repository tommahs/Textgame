from random import randint
import generalfunctions, party, actions, enemies
generalfunctions.clearScreen()
currentlocation = 'forest'
party = party.createparty()
curplayer = party[0]
# enemies = enemies.createenemies()
def main(party):
    generalfunctions.clearScreen()
    while True:
        print("You are currently in: {}".format(currentlocation.capitalize()))
        print('What do you want to do? \n1. Looking for trouble\n2. Use item\n3. Run\n4. Change location\n5. Party')
        choice = input('Choice : ')
        if '1' in choice:
            generalfunctions.clearScreen()
            choice1(party)
        elif '2' in choice:
            generalfunctions.clearScreen()
            choice2()
        elif '3' in choice:
            generalfunctions.clearScreen()
            choice3()
        elif '4' in choice:
            generalfunctions.clearScreen()
            choice4(currentlocation)
        elif '5' in choice:
            generalfunctions.clearScreen()
            choice5(party)
        else:
            exit()

def choice1(party): #:Looking around
    generalfunctions.clearScreen()
    actions.lookingaround(currentlocation, party)
    generalfunctions.clearScreen()

def choice2(): # Use item
    print("Not implemented")
def choice3(): #run from fight
    generalfunctions.clearScreen()
    print('You run away from the fight.')

def choice4(curloc): #Change location
    global currentlocation
    generalfunctions.clearScreen()
    currentlocation = generalfunctions.chloc(curloc)
    return currentlocation

def choice5(party): #Playerstuff

    global curplayer
    loop = 0
    while loop == 0:
        print("Currently selected : {}".format(curplayer['name']))
        print('1. Change player')
        print('2. Show stats')
        print('3. Show inventory')
        print('3. exit')
        print('')
        choice = input("What would you like to do?")
        if '1' in choice:
            generalfunctions.clearScreen()
            print('Which player would you like to select?')
            actions.showplayers(party)
            curplayer = actions.chplayer(party)

        elif '2' in choice:
            generalfunctions.clearScreen()
            actions.showstats(curplayer)
            generalfunctions.anyKey()
        elif '3' in choice:
            generalfunctions.clearScreen()
            loop = 1
    # loop = 0
    # while loop == 0:
    #     if '1' in choice:
    #         playernum = 0
    #         menunum = 1
    #         for each in party:
    #             try:
    #                 if choice == each['name']:
    #                     chplayer = party[playernum]
    #                     playernum += 1
    #                     menunum +=1




# def showstats(char): #Show stats
#     # playerfunctions.stats(char)
#     generalfunctions.anyKey()
#
# def choice4():  # teleport
#     generalfunctions.clearScreen()
#     global currentlocation
#     # currentlocation = map.chloc()
#     generalfunctions.clearScreen()
main(party)