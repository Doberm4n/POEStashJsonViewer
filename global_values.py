# -*- coding: utf-8 -*-

class globalValues():
	def __init__(self):
		self.columnsHeaders = [{'columnHeader' : 'Name', 'jsonName' : 'name'  , 'type' : 'str', 'isCalc' : False},

							 {'columnHeader' : 'Type', 'jsonName' : 'None'  , 'type' : 'None', 'isCalc' : None},

						   #{'columnHeader' : 'Type', 'jsonName' : 'typeLine'  , 'type' : 'str', 'isCalc' : False},

						   {'columnHeader' : 'iLvl', 'jsonName' : 'ilvl'  , 'type' : 'int', 'isCalc' : False},

						   {'columnHeader' : 'Rarity', 'jsonName' : 'frameType'  , 'type' : 'int', 'isCalc' : False},

						   {'columnHeader' : 'Quality', 'jsonName' : ''  , 'type' : 'str', 'isCalc' : False},

						  # {'columnHeader' : 'Sockets', 'jsonName' : 'sockets'  , 'type' : 'str', 'isCalc' : False}

						  {'columnHeader' : 'Properties', 'jsonName' : ''  , 'type' : 'str', 'isCalc' : False}



						   ]
		#assign columns headers to columns indices
		self.columnNameToIndex = {}
		for i in range (len(self.columnsHeaders)):
			self.columnNameToIndex[self.columnsHeaders[i]['columnHeader']] = i

		self.rarity = ['unknown', 'unknown', 'unknown', 'unknown', 'Uniquie']

		self.itemTypes = [
						'Flask', #Flasks
						'One Handed Mace', 'Two Handed Mace', #Maces
						'Map', #Maps
						'Boots', #Boots
						'Gloves', 'Gauntlets', 'Mitts', #Gloves
						'Buckler', 'Shield' #Shields
		]


		self.itemTypes = [{'typeName' : 'Flask', 'items' : ['Flask']}, #Flasks
						  {'typeName' : 'One Handed Mace', 'items' : ['One Handed Mace']}, #Maces
						  {'typeName' : 'Two Handed Mace', 'items' : ['Two Handed Mace']},
						  {'typeName' : 'Map', 'items' : ['Map']},	#Maps
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



		#self.types.sort
		#print self.types