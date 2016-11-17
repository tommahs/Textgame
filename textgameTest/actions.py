# import generalfunctions, enemies, combat
###### Perception ####

def lookingaround(currloc,party):
    import generalfunctions, actions, maincombat
    enemyamount = generalfunctions.dice6()
    fight = generalfunctions.diceEncounter()
    if fight < 5:
        enemylst = actions.findenemy(currloc, 2)
        print("You got an encounter with an {}".format(enemylst[0]['name']))
        maincombat.maincombat(party, enemylst)
        return enemylst
    if fight < 15:
        enemylst = actions.findenemy(currloc, 1)
        print("You got an encounter with an {}".format(enemylst[0]['name']))
        maincombat.maincombat(party, enemylst)
    elif fight <= 25:
        enemylst = actions.findenemy(currloc, 0)
        print("You got an encounter with an {}".format(enemylst[0]['name']))
        maincombat.maincombat(party, enemylst)
    else:
        print('No monster can be found')
        generalfunctions.anyKey()


####
##  Player Functions
####
def showplayers(party):
    playernum = 0
    for each in party:
        playernum += 1
        print('{}. {}'.format(playernum, each['name']))


def chplayer(party):
    import generalfunctions
    playernum = 0
    chplayer = (input("Type playername :").lower()).capitalize()
    for each in party:
        if chplayer == each['name']:
            curplayer = party[playernum]
        else:
            playernum += 1
        generalfunctions.clearScreen()
    return curplayer

def showstats(char):
    import generalfunctions
    generalfunctions.clearScreen()
    print('Character name : {}     lvl {}'.format(char['name'], char['lvl']))
    # print('Character class: {}'.format(char['class']))   <=== Not implemented
    print('Current xp: {}  Req. for next lvl: {}\n'.format(char['xp'], char['xptonextlvl']))
    print('HP : {}'.format(char['stats']['hp']))
    print('STR: {}   INT: {}'.format(char['stats']['str'], char['stats']['int']))
    print('DEX: {}   WIS: {}'.format(char['stats']['dex'], char['stats']['wis']))
    print('CON: {}   CHA: {}'.format(char['stats']['con'], char['stats']['cha']))
    if char['skillpoints'] == 1:
        print('Skillpoint available for use : {}'.format(char['skillpoints']))
    elif char['skillpoints'] > 1:
        print('Skill points available for use : {}'.format(char['skillpoints']))

def spendsp(char):
    import generalfunctions, actions
    availablestats = ['str', 'int', 'dex', 'wis', 'con', 'cha', 'hp']
    availableSP = char['skillpoints']
    while True:
        generalfunctions.clearScreen()
        actions.showstats(char)
        statinput = input('Which stat do you wish to increase? :').lower()
        statUp = int(input('How many points would you like to use?'))
        if statUp < 0 or statUp > availableSP:
            print("You do not have enough skillpoints!")
            input('Press enter to continue.')
            break
        if statinput in availablestats:
            stat = statinput
            char['stats'][stat] += statUp
            availableSP -= statUp
            char['skillpoints'] = availableSP
            print('You have succesfully added {} to your {}'.format(statUp, stat))
        if availableSP == 0:
            break
        continu = input('Do you want to continue spending skillpoints? yes/no'.lower())
        if 'no' in continu:
            break
        elif continu is ValueError or continu is TypeError:
            break

def classcheck(char):
    import playerclasses
    global nHp, nStr, nDex, nCon, nInt, nWis, nCha
    growthlist = []
    if char['special'] == 'None':
        if char['class'] == 'Noob':
            growthlist = (playerclasses.noobGrowth())
        elif char['class'] == 'Warrior':
            growthlist = (playerclasses.warriorGrowth())
        elif char['class'] == 'Roque':
            growthlist = (playerclasses.roqueGrowth())
        elif char['class'] == 'Mage':
            growthlist = (playerclasses.mageGrowth())
    nStr = round(float(growthlist[0]))
    nDex = round(float(growthlist[1]))
    nCon = round(float(growthlist[2]))
    nInt = round(float(growthlist[3]))
    nWis = round(float(growthlist[4]))
    nCha = round(float(growthlist[5]))
    nHp = round(float(growthlist[6]))

def level(char):
    import generalfunctions, actions
    generalfunctions.clearScreen()

    if char['xp'] >= char['lvlNext']:
        char['lvl'] +=1
        char['skillpoints'] += 5
        char['xp'] = char['xp'] - char['lvlNext']
        char['lvlNext'] = round(char['lvlNext'] *1,5)
        classcheck(char)
        print('Character name & level: {} {}'.format(char['name'], char['lvl']))
        print('Current xp: {}  Req. for next lvl: {}\n'.format(char['xp'], char['lvlNext']))
        print('HP : {} + {}'.format(char['stats']['hp'], nHp))
        print('STR: {} + {}   INT: {} + {}'.format(char['stats']['str'], nStr, char['stats']['int'], nInt))
        print('DEX: {} + {}   WIS: {} + {}'.format(char['stats']['dex'], nDex, char['stats']['wis'], nWis))
        print('CON: {} + {}   CHA: {} + {}'.format(char['stats']['con'], nCon, char['stats']['cha'], nCha))
        print('Skill points available for use : {}'.format(char['skillpoints']))
        char['stats']['hp'] += nHp
        char['stats']['str'] += nStr
        char['stats']['int'] += nInt
        char['stats']['dex'] += nDex
        char['stats']['wis'] += nWis
        char['stats']['con'] += nCon
        char['stats']['cha'] += nCha
        useSP =input('Do you wish to use your skillpoints? yes/no'.lower())
        if 'yes' in useSP:
            spendsp(char)
        else:
            pass
    else:
        pass

def definiative(lst):
    import generalfunctions
    for char in lst:
        iniative = generalfunctions.abilitymodifier(char['stats']['dex'])
        char['iniative'] = (iniative + generalfunctions.dice20())
    return lst

def turnorder(players, enemies):
    from operator import itemgetter
    combat = []
    enemynum = int(0)
    turn = 0
    for player in players:
        player['realplayer'] = 1
        combat.append(player)
    for enemy in enemies:
        enemynum += 1
        enemy['enemynum'] = enemynum
        enemy['realplayer'] = 0
        combat.append(enemy)
    turnorderlst = definiative(combat)
    sorted(turnorderlst, key=itemgetter('iniative', 'name'))
    for each in turnorderlst:
        turn += 1
        each['turn'] = turn
    return turnorderlst

def shenemies(enemylst):
    enemynum = 0
    print(enemylst)
    for each in enemylst:
        enemynum += 1
        print("{}. {}".format(each['enemynum'], each['name']))

def chenemy(enemylst):
    try:
        fightinput = int(input("Which enemy would you like to attack?"))
        for each in enemylst:
            if fightinput == each['enemynum']:
                print("You've chosen {} as your target!".format(each['enemynum']))
                return each
    except:
        if TypeError:
            print('type error')
        elif ValueError:
            print('value error')
        elif UnboundLocalError:
            print('unbounderror')


##
def fight(player, enemy):
    print('A wild {} appears!' .format(enemy['name']))
    print('-----------------')
    takedmg(player, enemy)

def takedmg(attacker, defender, party):
    from random import randint
    dmg = randint(attacker['stats']['atk'][0], attacker['stats']['atk'][1])
    defender['stats']['hp'] = defender['stats']['hp'] - dmg
    if defender['stats']['hp'] <=  0:
        print('{} has been slain\n'.format(defender['name']))
        for each in party:
            each['xp'] += defender['rewardXp']
        if attacker['realplayer'] == 1:
            print("Everyone receive {} EXP!".format(defender['rewardXp']))
            input('Press any key to continue')
            record(defender,party)
    else:
        print('{} takes {} damage!'.format(defender['name'], dmg))

def record(defender, party):
    for each in party:
        try:
            if defender['name'] in each['record']:
                each['record'][defender['name']] = + 1
                print(each['record']['name'])
            elif defender['name'] in each['record']:
                print('No update!')
                each['record'].update({'{}'.format(defender['name']): 1})
        except:
            if KeyError:
                print("error")
def hpcheck(lst):
    for each in lst:
        if each['stats']['hp'] <= 0:
            lst.remove(each)
    return lst

######
# Enemy functions
###


def findenemy(currentlocation, num):
    import enemies
    enemyparty = []
    if currentlocation == 'forest':
        if num == 2:
            mob = enemies.enemies['kingworm'].copy()
        elif num == 1:
            mob = enemies.enemies['bigworm'].copy()
            enemyparty.append(mob)
        elif num == 0:
            mob = enemies.enemies['worm'].copy()
        enemyparty.append(mob)
    elif currentlocation == 'cave':
        if num == 2:
            mob = enemies.enemies['kingbat'].copy()
        elif num == 1:
            mob = enemies.enemies['bigbat'].copy()
        elif num == 0:
            mob = enemies.enemies['bat'].copy()
        enemyparty.append(mob)
    else:
        mob = enemies.worm.copy()
        enemyparty.append(mob)
    return enemyparty

def enemyattack(party):
    count = -1
    playerhp = 0
    for each in party:
        eachhp = (each['stats']['hp']/ each['stats']['maxhp'] * 100)
        if eachhp > playerhp:
            playerhp = eachhp
            count += 1
    return party[count]
