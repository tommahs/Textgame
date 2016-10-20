def findenemy(currentlocation, num):
    import enemies
    if currentlocation == 'Forest':
        if num == 2:
            mob = enemies.kingworm.copy()
        elif num == 1:
            mob = enemies.bigworm.copy()
        elif num == 0:
            mob = enemies.worm.copy()
    elif currentlocation == 'Cave':
        if num == 2:
            mob = enemies.kingbat.copy()
        elif num == 1:
            mob = enemies.bigbat.copy()
        elif num == 0:
            mob = enemies.bat.copy()
    else:
        mob = enemies.worm.copy()
    return mob