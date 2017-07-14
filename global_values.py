# -*- coding: utf-8 -*-
import operator
import modules.tools as tools
import os

#form = None
#t = None

class globalValues():
    def __init__(self):
        #load config
        self.jsonConfig = tools.readJson('Configs\config.json')

        self.columnsHeaders = [{'columnHeader' : 'Name', 'jsonName' : 'name'  , 'type' : 'String', 'isCalc' : False},

                             {'columnHeader' : 'Type', 'jsonName' : 'None'  , 'type' : 'String', 'isCalc' : None},

                           #{'columnHeader' : 'Type', 'jsonName' : 'typeLine'  , 'type' : 'str', 'isCalc' : False},

                           {'columnHeader' : 'iLvl', 'jsonName' : 'ilvl'  , 'type' : 'Integer', 'isCalc' : False},

                           {'columnHeader' : 'Rarity', 'jsonName' : 'frameType'  , 'type' : 'String', 'isCalc' : False},

                           {'columnHeader' : 'Quality', 'jsonName' : ''  , 'type' : 'Integer', 'isCalc' : False},

                          # {'columnHeader' : 'Sockets', 'jsonName' : 'sockets'  , 'type' : 'str', 'isCalc' : False}

                            {'columnHeader' : 'Properties', 'jsonName' : ''  , 'type' : 'String', 'isCalc' : False},




                          {'columnHeader' : 'Implicit Modifiers', 'jsonName' : 'implicitMods'  , 'type' : 'String', 'isCalc' : False},

                          {'columnHeader' : 'Explicit Modifiers', 'jsonName' : 'explicitMods'  , 'type' : 'String', 'isCalc' : False},

                          {'columnHeader' : 'PropertiesImplicitExplicit', 'jsonName' : 'None'  , 'type' : 'String', 'isCalc' : False},

                          {'columnHeader' : 'DPS', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                           {'columnHeader' : 'eDPS', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                           {'columnHeader' : 'pDPS', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                            {'columnHeader' : 'fDPS', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                             {'columnHeader' : 'lDPS', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                             {'columnHeader' : 'cDPS', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                              {'columnHeader' : 'ChDPS', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True}




                          ]
        #assign columns headers to columns indices
        self.columnNameToIndex = {}
        for i in range (len(self.columnsHeaders)):
            # if (not self.jsonConfig['common']['calculateSpecifiedColumns']) and (self.columnsHeaders[i]['isCalc']):
            #     continue
            self.columnNameToIndex[self.columnsHeaders[i]['columnHeader']] = i
        print self.columnNameToIndex

        self.rarity = ['Normal', 'Magic', 'Rare', 'Unique']

        self.itemTypes = [
                        'Flask', #Flasks
                        'One Handed Mace', 'Two Handed Mace', #Maces
                        'Map', #Maps
                        'Boots', #Boots
                        'Gloves', 'Gauntlets', 'Mitts', #Gloves
                        'Buckler', 'Shield' #Shields
        ]


        self.itemTypes = [{'typeName' : 'Flask', 'items' : ['Flask']}, #Flasks
                          {'typeName' : 'One Handed Mace\n(1H Weapon)', 'items' : ['One Handed Mace']}, #Maces
                          {'typeName' : 'Two Handed Mace\n(2H Weapon)', 'items' : ['Two Handed Mace']},
                          {'typeName' : 'Map', 'items' : ['Map']},  #Maps
                          {'typeName' : 'Boots', 'items' : ['Boots']}, #Boots
                          {'typeName' : 'Gloves', 'items' : ['Gloves']}, #Gloves
                          {'typeName' : 'Shield', 'items' : ['Shield']}, #Shields
                          {'typeName' : 'Body Armour', 'items' : ['BodyArmour']}, #BodyArmours
                          {'typeName' : 'Helmet', 'items' : ['Helmet']}, #Helmets
                          {'typeName' : 'Amulet', 'items' : ['Amulet']}, #Amulets
                          {'typeName' : 'Ring', 'items' : ['Ring']} #Rings
                         ]

                        # 'One Handed Mace', 'Two Handed Mace',
                        # '',
                        # '',
                        # '',

        self.operandsText = {'String' : ['contains', 'match'], 'Integer' : ['<', '>', '=', '<>'], 'Float' : ['<', '>', '=', '<>']}

        self.operandsChars = {'<' : operator.lt, '>' : operator.gt, '=' : operator.eq, '<>' : operator.ne, 'contains' : operator.contains}

        self.filtersDir = os.getcwd() + '\\Filters'



        #self.types.sort
        #print self.types