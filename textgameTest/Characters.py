Characters = {'tommahs': {
                        'name' : 'Tommahs',
                        'class' : 'Warrior',
                        'lvl' : 1,
                        'xp' : 0,
                        'xptonextlvl' : 25,
                        'rewardXp': 0,
                        'skillpoints': 0,
                        'stats': {'str': 1,
                                  'dex' : 10,
                                  'con' : 1,
                                  'int' : 1,
                                  'wis' : 1,
                                  'cha' : 1,
                                  'hp' : 20,
                                  'maxhp': 20,
                                  'atk' : [5,12]},
                        'record' : {},
                        },
            'tess': {
                        'name' : 'Tess',
                        'class' : 'Mage',
                        'lvl' : 1,
                        'xp' : 0,
                        'xptonextlvl' : 25,
                        'rewardXp' : 0,
                        'skillpoints': 0,
                        'stats': {'str': 1,
                                  'dex' : 10,
                                  'con' : 1,
                                  'int' : 1,
                                  'wis' : 1,
                                  'cha' : 1,
                                  'hp' : 20,
                                  'maxhp': 20,
                                  'atk' : [5,12]},
                        'record': {}
                        }
            }


import xmltodict
def xmlreader():
    file = open('characters.xml', 'r')
    reader = file.read()
    xmldict = xmltodict.parse(reader)
    xmldict2 = xmldict['root']
    characters = xmldict2
    print(characters)
xmlreader()

char = {'tommahs' : {'test' : 1,
                     'test2' : 2}
        }
def xmlwriter(chardict):
    import dicttoxml
    from xml.dom.minidom import parseString

    with open('characters.xml', 'w') as file:
        xml = dicttoxml.dicttoxml(chardict)
        dom = parseString(xml)
        print(dom.toprettyxml())

# xmlwriter(char)