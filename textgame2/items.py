# 4 dices die gerold worden om een random waarde te creeeren.
# uitkomst <=25 = monster encounter
# uitkomst <15 = sterker monster encounter
# record van type monster verslagen -> sterker monster, nieuwe diceset voor nodig
# uitkomst van <10 = Boss type
# uitkomst van

import combatfunctions, enemyfunctions, player
def lookingAround(currloc, party):
    import generalfunctions
    encounternum = generalfunctions.diceEncounter()
    if encounternum <= 25:
        encounter(currloc, party, encounternum)
    else:
    generalfunctions.anyKey()
    #testing
    # for a in enemylst:
    #     print(a)
    print(enemylst)
    return enemylst

def encounter(currloc, party, num):
    import generalfunctions
    enemylst = []
    enemyamount = generalfunctions.dice6()
    print(enemyamount)
    counter = 0
    if num < 5:
        enemy = enemyfunctions.findenemy(currloc, 2)
        enemystats = enemy['stats']
        enemylst.append(enemy)
        # enemylst.append(enemystats)
        # combatfunctions.fight(party, enemy)
        print("You find an {}!".format(enemy['name']))
    elif num < 15:
        while counter is not 4:
            enemy = enemyfunctions.findenemy(currloc, 1)
            enemystats = enemy['stats']
            enemylst.append(enemy)
            enemylst.append(enemystats)
            counter += 1
            # combatfunctions.fight(party, enemy)
            print("You find an {}!".format(enemy['name']))
    elif num <= 25:
        while counter is not enemyamount:
            enemy = enemyfunctions.findenemy(currloc, 0)
            enemystats = enemy['stats']
            enemylst.append(enemy)
            enemylst.append(enemystats)
            counter +=1
            # combatfunctions.fight(party, enemy)
            print("You find an {}!".format(enemy['name']))
    else:
        print('No monster can be found')
    print(enemylst)
    print(enemylst[0]['stats']['dex'])
    combatfunctions.fight(party, enemylst)
    return enemylst

lookingAround('Forest', player.player)