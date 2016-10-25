from random import randint
import actions, map, player, enemies, combat, generalfunctions, playerfunctions
currentlocation = 'Forest'
character = player.player
def main():
    while True:
        generalfunctions.clearScreen()
        playerfunctions.level(character)
        generalfunctions.clearScreen()
        print('You are currently in {}'.format(currentlocation.capitalize()))
        print('What do you want to do? \n1. Look around\n2. Run\n3. View stats\n4. Teleport')
        choice = input('Choice : ')
        if '1' in choice:
            choice1()
        elif '2' in choice:
            choice2()
        elif '3' in choice:
            choice3(character)
        elif '4' in choice:
            choice4()
        else:
            exit()

def choice1(): #Look if there is anything nearby
    generalfunctions.clearScreen()
    actions.lookingAround(currentlocation,character)
    generalfunctions.clearScreen()
def choice2(): #run from fight
    generalfunctions.clearScreen()
    print('You run away from the fight.')

def choice3(char): #Show stats
    playerfunctions.stats(char)
    generalfunctions.anyKey()

def choice4():  # teleport
    generalfunctions.clearScreen()
    global currentlocation
    currentlocation = map.chloc()
    generalfunctions.clearScreen()
main()