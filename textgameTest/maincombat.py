from random import randint
import generalfunctions, actions, party, enemies
currentlocation = 'forest'

def maincombat(party, enemylst):
    turnorder = actions.turnorder(party, enemylst)
    dead = []
    turn = 1
    loop = 1
    while loop == 1:
        totalhp = 0
        totalhpe = 0
        subturn = 1
        for each in turnorder:
            for hpcheck in turnorder:
                if hpcheck['stats']['hp'] <= 0:
                    dead.append(hpcheck)
                    turnorder.remove(hpcheck)
                    if hpcheck['realplayer'] == 1:
                        party.remove(hpcheck)
                    elif hpcheck['realplayer'] == 0:
                        enemylst.remove(hpcheck)
            if len(enemylst) == 0:
                loop = 0
            elif len(party) == 0:
                print("Game over!")
                loop = 0
            elif each['turn'] == subturn:
                if each['realplayer'] == 1:
                    print(len(enemylst))
                    print("Turn {} for {}".format(turn, each['name']))
                    subturn +=1
                    combatmenu(each, party, enemylst)
                else:
                    if len(party) == 0:
                        print("Game over!")
                        break
                    subturn += 1
                    enemy = actions.enemyattack(party)
                    print("{} attacks {}!".format(each['name'], enemy['name']))
                    actions.takedmg(each, enemy, enemylst)

        turn += 1


def combatmenu(each, party,enemylst):
        print('What do you want to do? \n1. Fight\n2. Use item\n3. Run')
        choice = input('Choice : ')
        if '1' in choice:
            choice1(each, party, enemylst)
        elif '2' in choice:
            choice2(each)
        elif '3' in choice:
            choice3(each)
        else:
            exit()

def choice1(each, party, enemylst): #Fight an enemy
    generalfunctions.clearScreen()
    actions.shenemies(enemylst)
    enemy = actions.chenemy(enemylst)
    actions.takedmg(each, enemy, party)
    generalfunctions.clearScreen()

def choice2(each): # Use item
    print("Not implemented")
def choice3(): #run from fight
    generalfunctions.clearScreen()
    print('You run away from the fight.')