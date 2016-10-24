import combatfunctions

# turn-based combat
# 0. party-up before combat
# 1. Define iniative per player & enemy
# 2. Options per turn in battle
# 3. Result
import player, enemies, generalfunctions

players = [[player.player]]
enemies = [[enemies.kingbat],[enemies.worm]]
combat = []

#####
# 0. Creating the turnorder
#
def combat(playerlst, enemylst):
    iniativelst = combatfunctions.definiative(playerlst, enemylst)
    # defturnorders = turnorder(iniativelst)
    combatfunctions.fight2(playerlst, enemylst,iniativelst)
    return iniativelst

def main(playerlst, enemylst):
    turnorderlst = combatfunctions.turnorder(playerlst, enemylst)
    enemylst = []
    for enemy in turnorderlst:
        if enemy['realplayer'] == 0:
            enemylst.append(enemy)
            # print("{}. {} ".format(enemy['enemynum'], enemy['name']))
    for player in turnorderlst:
        if player['realplayer'] == 1:
            combatfunctions.chenemy(player, enemylst)

print(main(players, enemies))
# print(combat(players, enemies))