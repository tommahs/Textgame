import generalfunctions, playerclasses


def stats(char):
    generalfunctions.clearScreen()
    print('Character name & level: {} {}'.format(char['name'], char['lvl']))
    print('Character class: {}'.format(char['class']))
    print('Current xp: {}  Req. for next lvl: {}\n'.format(char['xp'], char['lvlNext']))
    print('HP : {}'.format(char['stats']['hp']))
    print('STR: {}   INT: {}'.format(char['stats']['str'], char['stats']['int']))
    print('DEX: {}   WIS: {}'.format(char['stats']['dex'], char['stats']['wis']))
    print('CON: {}   CHA: {}'.format(char['stats']['con'], char['stats']['cha']))
    if char['skillpoints'] == 1:
        print('Skillpoint available for use : {}'.format(char['skillpoints']))
    elif char['skillpoints'] > 1:
        print('Skill points available for use : {}'.format(char['skillpoints']))

def classcheck(char):
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


def spendsp(char):
    availablestats = ['str', 'int', 'dex', 'wis', 'con', 'cha', 'hp']
    availableSP = char['skillpoints']
    while True:
        generalfunctions.clearScreen()
        stats(char)
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
