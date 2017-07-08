# -*- coding: utf-8 -*-


class globalValues():
	def __init__(self):
		self.columnsHeaders = [{'columnHeader' : 'Name', 'jsonName' : 'name'  , 'type' : 'str', 'isCalc' : False },

						   {'columnHeader' : 'Type', 'jsonName' : 'typeLine'  , 'type' : 'str', 'isCalc' : False},

						   {'columnHeader' : 'iLvl', 'jsonName' : 'ilvl'  , 'type' : 'int', 'isCalc' : False},

						   {'columnHeader' : 'Rarity', 'jsonName' : 'frameType'  , 'type' : 'str', 'isCalc' : False},

						   {'columnHeader' : 'Sockets', 'jsonName' : 'sockets'  , 'type' : 'str', 'isCalc' : False}


						   ]

		self.rarity = ['unknown', 'unknown', 'unknown', 'unknown', 'Uniquie']