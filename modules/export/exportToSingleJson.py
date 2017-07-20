# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
sys.path.insert(0,os.path.dirname(parentdir))
#from PyQt4 import QtGui
import json
import modules.tools as tools

def exportToSingleJson(form):
    fileName = tools.getSingleJsonFileName()
    if fileName:
        form.tableWidget.setEnabled(False)
        data = {"common":{"singleJsonVersion":""},"rows": []}
        temp = json.dumps(data)
        jsonData = json.loads(temp)

        #with open(unicode(fileName), 'wb') as stream:

        jsonData['common']['singleJsonVersion'] = form.ig.jsonConfig['common']['configVersion']


        l = form.tableWidget.rowCount()
        for i in range(l):
                form.statusbar.showMessage('Processing ' + os.path.basename(unicode(fileName))  + ' (item ' + str(i+1) + ' of ' + str(l) + ')')
                #jsonItemValues = []
                jsonData['rows'].append([])
                for j in range(form.tableWidget.columnCount()):
                    itemValue = form.tableWidget.item(i, j)
                    if itemValue:
                        jsonData['rows'][i].append(unicode(itemValue.text()))
                    else:
                        jsonData['rows'][i].append('')
        tools.writeJson(jsonData, unicode(fileName))
        form.statusbar.showMessage('Export complete')
        form.tableWidget.setEnabled(True)
