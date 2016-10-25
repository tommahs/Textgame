enemies = {
'worm' : {'name' : 'Worm',
          # 'class' : 'Warrior',
          # 'lvl' : 1,
        'xp' : 0,
        'rewardXp' : 25,
        'lvlNext' : 25,
        'stats' : {'str' : 1,
                'dex' : 1,
                'int' : 1,
                'hp' : 20,
                'maxhp' : 20,
                'atk' : [5, 12]},
        },

'bigworm' : {'name': 'Big Worm',
        # 'class': 'Warrior',
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
        },
'kingworm' : {'name': 'King Worm',
        # 'class': 'Warrior',
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
        },

'bat' : {'name': 'Bat',
        # 'class': 'Warrior',
        'lvl': 1,
        'xp': 0,
        'rewardXp': 5,
        'lvlNext': 25,
        'stats': {'str': 1,
                'dex': 1,
                'int': 1,
                'hp': 20,
                'atk': [5, 12]},
       },

'bigbat' : {'name': 'Big Bat',
        # 'class': 'Warrior',
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
          },

'kingbat' : {'name': 'King Bat',
           # 'class': 'Warrior',
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
           }


def createenemies():
    import enemies
    global enemiesparty
    party = []
    addedtoparty = []
    loop = 1
    print("Enter exit to stop adding characters to the party")
    while loop == 1:
        partyadd = input("Please type in a character to join your party :\n").lower()
        player = partyadd
        try:
            if player == 'exit':
                loop = 0
            elif player not in addedtoparty:
                party.append(enemies.enemies[player])
                addedtoparty.append(player)
            elif player in addedtoparty:
                print("This player has already been added to the party!")
            else:
                pass
        except:
            if KeyError:
                print("This player does not exist.\n")
                continue
        import generalfunctions
        for char in party:
            iniative = generalfunctions.abilitymodifier(char['stats']['dex'])
            char['dexmod'] = iniative
    print("Good luck!")
    return party