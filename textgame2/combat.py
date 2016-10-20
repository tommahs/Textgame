import combatfunctions

# turn-based combat
# 0. party-up before combat
# 1. Define iniative per player & enemy
# 2. Options per turn in battle
# 3. Result
import player, enemies, combatfunctions

players = [[player.player['name'].lower(), player.player['stats']['dex']]]
enemies = [[enemies.bat['name'].lower(), enemies.bat['stats']['dex']], [enemies.worm['name'].lower(),enemies.worm['stats']['dex']]]
combat = []

#####
# 0. Creating the turnorder
# def combinepe():

def definiative(char):
    for charlist in players:
        combat.append(charlist)
    for charlist in enemies:
        combat.append(charlist)
    for lst in combat:
        dex = lst[1]
        modifier = combatfunctions.abilitymodifier(dex)
        lst[1] = modifier
    print(combat)
    return combat

definiative(players)






