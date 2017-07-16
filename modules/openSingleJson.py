# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PyQt4 import QtGui
#import json
import modules.tools as tools

def openSingleJson(form):
	fileName = tools.openJsonFileName()
	if fileName:
		jsonData = tools.readJson(fileName)



		if not form.ig.jsonConfig['common']['configVersion'] == jsonData['common']['singleJsonVersion']:
			QtGui.QMessageBox.warning(None, "Open single json", "Version mismatch. Single json cannot be opened. Please export to single json and then retry.")
			return
			form.tableWidget.setRowCount(0)
			for i in range(len(jsonData['rows'])):
		            #jsonItemValues = []
		            #jsonData['rows'].append([])
		            for j in range(len(jsonData['rows'][i])):
		                itemValue = jsonData['rows'][i][j]
		                if itemValue:
		                    form.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(unicode(itemValue)))
		                else:
		                    form.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(''))
		            #tools.writeJson(jsonData, fileName)