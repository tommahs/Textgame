import Characters

def currentparty(lst):
    import Characters
    print("Your current team consists of:")
    for char in lst:
        print(char['name'])
    print()
def createparty():
    import Characters, generalfunctions
    global party
    party = []
    addedtoparty = []
    loop = 1
    while loop == 1:
        print("Enter exit to stop adding characters to the party")
        partyadd = input("Please type in a character to join your party :\n").lower()
        player = partyadd
        try:
            if player == 'exit':
                loop = 0
            elif player not in addedtoparty:
                party.append(Characters.Characters[player])
                addedtoparty.append(player)
            elif player in addedtoparty:
                print("This player has already been added to the party!")
            else:
                pass
        except:
            if KeyError:
                print("This player does not exist.\n")
                continue
        generalfunctions.clearScreen()
        currentparty(party)
        import generalfunctions
        for char in party:
            iniative = generalfunctions.abilitymodifier(char['stats']['dex'])
            char['dexmod'] = iniative
    print("Good luck!")
    return party

def showparty():
    import Characters
    count = 0
    print('The party consists of:')
    for chardict in party:
        count +=1
        print("{}. {} lvl:{}".format(count, chardict['name'], chardict['lvl']))
