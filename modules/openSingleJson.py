# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PyQt4 import QtGui
#import json
import modules.tools as tools
import ui.main_layout as UIMainLayout

def openSingleJson(form):

    if form.ig.jsonConfig['curGuide']:
        directoryName = os.path.dirname(form.ig.jsonConfig['curGuide'])
    else:
        directoryName = ''

    fileName = tools.openSingleJsonFileName(directoryName)
    if fileName:

        jsonData = tools.readJson(fileName)
        form.ig.jsonConfig['curGuide'] = fileName
        tools.writeJson(form.ig.jsonConfig, 'Configs\config.json')


        if not form.ig.jsonConfig['common']['configVersion'] == jsonData['common']['singleJsonVersion']:
            QtGui.QMessageBox.warning(None, "Open single json", "Version mismatch. Single json cannot be opened. Please export to single json and then retry.")
            return

        form.tableWidget.setEnabled(False)
        form.tableWidget.setRowCount(0)
        UIMainLayout.tableWidgetDisableResizeToContents(form)

        for i in range(len(jsonData['rows'])):
                #jsonItemValues = []
                #jsonData['rows'].append([])
                form.tableWidget.insertRow(i)
                for j in range(len(jsonData['rows'][i])):
                    itemValue = jsonData['rows'][i][j]
                    print itemValue
                    if itemValue:
                        form.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(unicode(itemValue)))
                    else:
                        form.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(''))
                #tools.writeJson(jsonData, fileName)

        UIMainLayout.tableWidgetContentsAutoSize(form)


        form.tableWidget.setEnabled(True)