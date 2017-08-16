# -*- coding: utf-8 -*-
import operator
import modules.tools as tools
import os

class globalValues():
    def __init__(self):
        #load config
        self.jsonConfig = tools.readJson('Configs\config.json')

        #Stash tab columns
        self.columnsHeaders = [{'columnHeader' : 'Name', 'jsonName' : 'name'  , 'type' : 'String', 'isCalc' : False},

                            {'columnHeader' : 'Location', 'jsonName' : 'None'  , 'type' : 'String', 'isCalc' : False},

                             {'columnHeader' : 'Type', 'jsonName' : 'None'  , 'type' : 'String', 'isCalc' : False},

                           {'columnHeader' : 'iLvl', 'jsonName' : 'ilvl'  , 'type' : 'Integer', 'isCalc' : False},

                           {'columnHeader' : 'mTier', 'jsonName' : 'ilvl'  , 'type' : 'Integer', 'isCalc' : False},

                           {'columnHeader' : 'Rarity', 'jsonName' : 'frameType'  , 'type' : 'String', 'isCalc' : False},

                           {'columnHeader' : 'Quality', 'jsonName' : ''  , 'type' : 'Integer', 'isCalc' : False},

                           {'columnHeader' : 'Qty', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

                           {'columnHeader' : 'Sockets', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

                           {'columnHeader' : 'Linked', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

                           {'columnHeader' : 'LinksVisual', 'jsonName' : 'None'  , 'type' : 'String', 'isCalc' : False},

                           {'columnHeader' : 'sStr', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

                           {'columnHeader' : 'sDex', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

                           {'columnHeader' : 'sInt', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

                           {'columnHeader' : 'sWh', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

                            {'columnHeader' : 'rLvl', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

                             {'columnHeader' : 'rStr', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

                              {'columnHeader' : 'rDex', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

                               {'columnHeader' : 'rInt', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : False},

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

                              {'columnHeader' : 'ChDPS', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                               {'columnHeader' : 'APS', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                               {'columnHeader' : 'csCh', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                               {'columnHeader' : 'resTotal', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'resAll', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'resF', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'resL', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'resC', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'resCh', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'toAttrTotal', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'toStr', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'toDex', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'toInt', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'toMaxLife', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                               {'columnHeader' : 'toMaxMana', 'jsonName' : 'None'  , 'type' : 'Float', 'isCalc' : True},

                               {'columnHeader' : 'Arm', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'Ev', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'ES', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                               {'columnHeader' : 'ChtB', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                                {'columnHeader' : 'GcsC', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                                 {'columnHeader' : 'GcsM', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                                  {'columnHeader' : 'CscfS', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                                   {'columnHeader' : 'Csp', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True},

                                    {'columnHeader' : 'SpD', 'jsonName' : 'None'  , 'type' : 'Integer', 'isCalc' : True}

                          ]

        #Currency tab columns
        self.columnsHeadersCurrency = [{'columnHeader' : 'Name', 'jsonName' : 'name'  , 'type' : 'String', 'isCalc' : False},

                                    {'columnHeader' : 'Total', 'jsonName' : 'name'  , 'type' : 'Integer', 'isCalc' : False}

                          ]

        #assign columns headers to columns indices for Stash
        self.columnNameToIndex = {}
        for i in range (len(self.columnsHeaders)):
            self.columnNameToIndex[self.columnsHeaders[i]['columnHeader']] = i

        #assign columns headers to columns indices for Currency
        self.columnNameToIndexCurrency = {}
        for i in range (len(self.columnsHeadersCurrency)):
            self.columnNameToIndexCurrency[self.columnsHeadersCurrency[i]['columnHeader']] = i

        self.rarity = ['Normal', 'Magic', 'Rare', 'Unique', 'Gem', 'Currency', 'Divination', 'Unknown', 'Prophecy']

        self.itemTypes = [
                        'Flask', #Flasks
                        'One Handed Mace', 'Two Handed Mace', #Maces
                        'Map', #Maps
                        'Boots', #Boots
                        'Gloves', 'Gauntlets', 'Mitts', #Gloves
                        'Buckler', 'Shield' #Shields
        ]


        self.itemTypes = [{'typeName' : 'Essence', 'items' : ['Essence']}, #Essences
                            {'typeName' : 'Divination', 'items' : ['Divination']}, #Divination
                            {'typeName' : 'Currency', 'items' : ['Currency']}, #Currency
                            {'typeName' : 'Quiver', 'items' : ['Quivers']}, #Quivers
                            {'typeName' : 'Belt', 'items' : ['Belts']}, #Belts
                          {'typeName' : 'Flask', 'items' : ['Flask']}, #Flasks
                          {'typeName' : 'One Handed Mace\n(1H Weapon)', 'items' : ['OneHandMaces']}, #Maces
                          {'typeName' : 'Two Handed Mace\n(2H Weapon)', 'items' : ['TwoHandMaces']},
                          {'typeName' : 'One Handed Sword\n(1H Weapon)', 'items' : ['OneHandSwords']}, #Swords
                          {'typeName' : 'Two Handed Sword\n(2H Weapon)', 'items' : ['TwoHandSwords']},
                           {'typeName' : 'One Handed Axe\n(1H Weapon)', 'items' : ['OneHandAxes']}, #Axes
                            {'typeName' : 'Two Handed Axe\n(2H Weapon)', 'items' : ['TwoHandAxes']},
                            {'typeName' : 'Wand\n(1H Weapon)', 'items' : ['Wands']}, #Wands
                            {'typeName' : 'Scepter\n(1H Weapon)', 'items' : ['Scepters']}, #Scepters
                            {'typeName' : 'Dagger\n(1H Weapon)', 'items' : ['Daggers']}, #Daggers
                            {'typeName' : 'Bow\n(2H Weapon)', 'items' : ['Bows']}, #Bows
                            {'typeName' : 'Stave\n(2H Weapon)', 'items' : ['Staves']}, #Staves
                             {'typeName' : 'Rapier\n(1H Weapon)', 'items' : ['Rapiers']}, #Rapiers
                             {'typeName' : 'Claw\n(1H Weapon)', 'items' : ['Claws']}, #Claws
                          {'typeName' : 'Map', 'items' : ['Map']},  #Maps
                          {'typeName' : 'Boots', 'items' : ['Boots']}, #Boots
                          {'typeName' : 'Gloves', 'items' : ['Gloves']}, #Gloves
                          {'typeName' : 'Body Armour', 'items' : ['BodyArmour']}, #BodyArmours
                          {'typeName' : 'Shield', 'items' : ['Shield']}, #Shields
                          {'typeName' : 'Helmet', 'items' : ['Helmet']}, #Helmets
                          {'typeName' : 'Amulet', 'items' : ['Amulet']}, #Amulets
                          {'typeName' : 'Ring', 'items' : ['Ring']}, #Rings
                          {'typeName' : 'Gem', 'items' : ['Gems']}, #Gems
                          {'typeName' : 'Jewel', 'items' : ['Jewels']} #Jewels
                         ]

        self.operandsText = {'String' : ['contains', 'match'], 'Integer' : ['>', '<', '=', '<>'], 'Float' : ['>', '<', '=', '<>']}

        self.operandsChars = {'>' : operator.gt, '<' : operator.lt, '=' : operator.eq, '<>' : operator.ne, 'contains' : operator.contains}

        self.filtersDir = os.getcwd() + '\\Filters'

        self.leagues = []

        self.itemCount = 0

        self.itemFound = 0
