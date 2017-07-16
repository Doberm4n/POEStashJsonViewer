# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
#from PyQt4 import QtGui
import json
import tools

def exportToSingleJson(form):
    fileName = tools.getJsonFileName()
    if fileName:

        data = {"common":{"singleJsonVersion":""},"rows": []}
        temp = json.dumps(data)
        jsonData = json.loads(temp)

        #with open(unicode(fileName), 'wb') as stream:

        jsonData['common']['singleJsonVersion'] = form.ig.jsonConfig['common']['configVersion']

        for i in range(form.tableWidget.rowCount()):
                #jsonItemValues = []
                jsonData['rows'].append([])
                for j in range(form.tableWidget.columnCount()):
                    itemValue = form.tableWidget.item(i, j)
                    if itemValue:
                        jsonData['rows'][i].append(unicode(itemValue.text()))
                    else:
                        jsonData['rows'][i].append('')
                tools.writeJson(jsonData, fileName)