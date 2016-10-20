from random import randint
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

#### Defining ability modifier:
## ability score -10, /2 + extra modifiers if applyable

def abilitymodifier(ability):
    modifier = round((ability -10) /2)
    return modifier