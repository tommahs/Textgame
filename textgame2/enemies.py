# def findenemy(currentlocation):
#     global WormCounter, BatCounter
#     if currentlocation == 'Forest':
#         mob = worm.copy()
#     elif currentlocation == 'Cave':
#         mob = bat.copy()
#     else:
#         mob ='none'
#     return mob



worm = {'name' : 'Worm',
        'class' : 'Warrior',
        'lvl' : 1,
        'xp' : 0,
        'rewardXp' : 25,
        'lvlNext' : 25,
        'stats' : {'str' : 1,
                'dex' : 1,
                'int' : 1,
                'hp' : 20,
                'maxhp' : 20,
                'atk' : [5, 12]},
        }

bigworm = {'name': 'Big Worm',
        'class': 'Warrior',
        'lvl': 2,
        'xp': 0,
        'rewardXp': 50,
        'lvlNext': 50,
        'stats': {'str': 3,
                'dex': 5,
                'int': 5,
                'hp': 35,
                'maxhp': 35,
                'atk': [7, 14]},
        }
kingworm = {'name': 'King Worm',
        'class': 'Warrior',
        'lvl': 5,
        'xp': 0,
        'rewardXp': 200,
        'lvlNext': 50,
        'stats': {'str': 6,
                'dex': 8,
                'int': 7,
                'hp': 50,
                'maxhp': 50,
                'atk': [10, 18]},
        }

bat = {'name': 'Bat',
        'class': 'Warrior',
        'lvl': 1,
        'xp': 0,
        'rewardXp': 5,
        'lvlNext': 25,
        'stats': {'str': 1,
                'dex': 1,
                'int': 1,
                'hp': 20,
                'atk': [5, 12]},
       }

bigbat = {'name': 'Big Bat',
        'class': 'Warrior',
        'lvl': 2,
        'xp': 0,
        'rewardXp': 50,
        'lvlNext': 50,
        'stats': {'str': 3,
                'dex': 5,
                'int': 5,
                'hp': 35,
                'maxhp': 35,
                'atk': [7, 14]},
          }

kingbat = {'name': 'King Bat',
           'class': 'Warrior',
            'lvl' : 5,
        'xp': 0,
        'rewardXp': 200,
        'lvlNext': 50,
        'stats': {'str': 6,
                'dex': 8,
                'int': 7,
                'hp': 50,
                'maxhp': 50,
                'atk': [10, 18]}}