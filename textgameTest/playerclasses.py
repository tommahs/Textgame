##############################
# Current implemented classes:
# Noob - adminonly
# Warrior - STR/CON
# Roque - DEX
# Mage - INT

def noob():
    template = {'name': 'Hero',
                'class' : 'Noob',
                'special': 'None',
                'lvl': 1,
                'xp': 0,
                'lvlNext': 25,
                'skillpoints': 0,
                'stats': {'str': 1,
                        'dex': 1,  # not implemented in combat
                        'con': 1,  # not implemented in combat
                        'int': 1,
                        'wis': 1,  # not implemented in combat
                        'cha': 1,  # not implemented in combat
                        'hp': 20,
                        'maxhp': 20,  # not implemented
                        'atk': [5, 12]},
                'record': {'', 0}}
    return template

def noobGrowth():
    dStr = 3
    dDex = 2
    dCon = 3
    dInt = 3
    dWis = 2
    dCha = 3
    # 16 points
    dHp = 4
    return dStr, dDex, dCon, dInt, dWis, dCha, dHp


def warriortemplate():
    template = {'name': 'Hero',
                'class': 'Warrior',
                'special': 'None',
                'lvl': 1,
                'xp': 0,
                'lvlNext' : 25,
                'skillpoints': 0,
                'stats': {'str': 7,
                          'dex': 4,  # not implemented in combat
                          'con': 6,  # not implemented in combat
                          'int': 3,
                          'wis': 3,  # not implemented in combat
                          'cha': 8,  # not implemented in combat
                          'hp': 40,
                          'maxhp': 20,  # not implemented
                          'atk': [9, 15]},
                'record': {'', 0}}
    return template


def warriorGrowth():
    dStr = 4
    dDex = 2
    dCon = 3
    dInt = 1.5
    dWis = 1.5
    dCha = 4
    # 16 points
    dHp = 6
    return dStr, dDex, dCon, dInt, dWis, dCha, dHp


def roquetemplate():
    template = {'name': 'Hero',
                'class': 'Roque',
                'special': 'None',
                'lvl': 1,
                'xp': 0,
                'lvlNext' : 25,
                'skillpoints': 0,
                'stats': {'str': 7,
                          'dex': 4,  # not implemented in combat
                          'con': 6,  # not implemented in combat
                          'int': 3,
                          'wis': 3,  # not implemented in combat
                          'cha': 8,  # not implemented in combat
                          'hp': 40,
                          'maxhp': 20,  # not implemented
                          'atk': [9, 15]},
                'record': {'', 0}}
    return template


def roqueGrowth():
    dStr = 2
    dDex = 4
    dCon = 3
    dInt = 1.5
    dWis = 1.5
    dCha = 4
    # 16 points
    dHp = 6
    return dStr, dDex, dCon, dInt, dWis, dCha, dHp


def mage():
    template = {'name': 'Hero',
                'class' : 'Mage',
                'special': 'None',
                'lvl': 1,
                'xp': 0,
                'lvlNext' : 25,
                'skillpoints': 0,
                'stats': {'str': 4,
                          'dex': 3,  # not implemented in combat
                          'con': 3,  # not implemented in combat
                          'int': 8,
                          'wis': 7,  # not implemented in combat
                          'cha': 6,  # not implemented in combat
                          'hp': 20,
                          'maxhp': 20,  # not implemented
                          'atk': [9, 15]},
                'record': {'', 0}}
    return template


def mageGrowth():
    dStr = 2
    dDex = 2
    dCon = 2
    dInt = 4
    dWis = 4
    dCha = 2
    # 16 points
    dHp = 3
    return dStr, dDex, dCon, dInt, dWis, dCha, dHp
