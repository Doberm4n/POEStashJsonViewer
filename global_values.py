# -*- coding: utf-8 -*-


class globalValues():
	def __init__(self):
		self.columnsHeaders = [{'columnHeader' : 'Name', 'jsonName' : 'name'  , 'type' : 'str', 'isCalc' : False},

							 {'columnHeader' : 'Type', 'jsonName' : 'None'  , 'type' : 'None', 'isCalc' : None},

						   #{'columnHeader' : 'Type', 'jsonName' : 'typeLine'  , 'type' : 'str', 'isCalc' : False},

						   {'columnHeader' : 'iLvl', 'jsonName' : 'ilvl'  , 'type' : 'int', 'isCalc' : False},

						   {'columnHeader' : 'Rarity', 'jsonName' : 'frameType'  , 'type' : 'str', 'isCalc' : False}

						  # {'columnHeader' : 'Sockets', 'jsonName' : 'sockets'  , 'type' : 'str', 'isCalc' : False}


						   ]

		self.columnNameToIndex = {}
		for i in range (len(self.columnsHeaders)):
			self.columnNameToIndex[self.columnsHeaders[i]['columnHeader']] = i

		self.rarity = ['unknown', 'unknown', 'unknown', 'unknown', 'Uniquie']