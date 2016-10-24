import generalfunctions, enemies, combat
###### Perception ####

def lookingAround(currloc,char):
    import generalfunctions
    enemyamount = generalfunctions.dice6()
    fight = generalfunctions.diceEncounter()
    if fight < 5:
        enemy = enemies.findenemy(currloc, 2)
        combat.fight(char, enemy)
    if fight < 15:
        enemy = enemies.findenemy(currloc, 1)
        combat.fight(char, enemy)
    elif fight <= 25:
        enemy = enemies.findenemy(currloc, 0)
        combat.fight(char, enemy)
    else:
        print('No monster can be found')
        generalfunctions.anyKey()