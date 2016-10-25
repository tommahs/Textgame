# from random import randint

# def fight(party, enemylst):

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
    playernum = 0
    turn = 0
    for player in players:
        print(player[playernum]['name'])
        player[playernum]['realplayer'] = 1
        playernum += 1
        combat.append(player)
    for enemy in enemies:
        print(enemy[0]['name'])
        print(enemy[0]['realplayer'])
        enemy[enemynum]['realplayer'] = 0
        enemy[enemynum]['enemynum'] = enemynum + 1
        combat.append(enemy[enemynum])
        enemynum += 1
    turnorderlst = definiative(combat)
    sorted(turnorderlst, key=itemgetter('iniative', 'name'))
    for each in turnorderlst:
        turn += 1
        each['turn'] = turn
    return turnorderlst


def chenemy(player, enemylst):
    try:
        fightinput = int(input("Which enemy would you like to attack?"))
    except:
        if TypeError:
            print('type error')
        elif ValueError:
            print('value error')
        elif UnboundLocalError:
            print('unbounderror')
    for each in enemylst:
        enemynum = each['enemynum']
        if enemynum == fightinput:
            enemy = each
        print("great success", each['name'], player['name'])
    fight(player, enemy)






def fight(player, enemy):
    print('A wild {} appears!' .format(enemy['name']))
    enemy['stats']['hp'] = enemy['stats']['maxhp']
    while True:
        print('-----------------')
        if enemy['stats']['hp'] <= 0:
            break
        cmd = input('Do you want to attack? yes/no: ').lower()
        if 'yes' in cmd:
            takedmg(player, enemy)
        elif 'no' in cmd:
            print('{} takes the opportunity to attack!'.format(enemy['name']))
            takedmg(enemy, player)
        else:
            pass
def takedmg(attacker, defender):
    from random import randint
    dmg = randint(attacker['stats']['atk'][0], attacker['stats']['atk'][1])
    defender['stats']['hp'] = defender['stats']['hp'] - dmg
    if defender['stats']['hp'] <=  0:
        print('{} has been slain\n'.format(defender['name']))
        attacker['xp'] += defender['rewardXp']
        print("You receive {} EXP!".format(defender['rewardXp']))
        input('Press any key to continue')
        record(attacker, defender)
    else:
        print('{} takes {} damage!'.format(defender['name'], dmg))

def record(attacker, defender):
    if defender['name'] in attacker['record']:
        print("success!")
        attacker['record'][defender['name']] = + 1
        print(attacker['record']['name'])
    elif KeyError:
        attacker['record'].update({'{}'.format(defender['name']): 1})
        print("Keyerror")
        print(attacker['record'])
    elif defender['name'] in attacker['record']:
        print('No update!')

