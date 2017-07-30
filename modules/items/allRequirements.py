# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from modules.classes.custom.QTableWidgetItem import QCustomTableWidgetItem as QCI

def setItemRequirements(form, itemIndex):
    if form.stashTabJson['items'][itemIndex].has_key('requirements'):
        valueLvl = ''
        valueStr = ''
        valueInt = ''
        valueDex = ''
        for i in range (len(form.stashTabJson['items'][itemIndex]['requirements'])):
            temp = form.stashTabJson['items'][itemIndex]['requirements'][i]['name']
            if 'Level' in temp:
                valueLvl = form.stashTabJson['items'][itemIndex]['requirements'][i]['values'][0][0]
                continue
            if 'Str' in temp:
                valueStr = form.stashTabJson['items'][itemIndex]['requirements'][i]['values'][0][0]
                continue
            if 'Dex' in temp:
                valueDex = form.stashTabJson['items'][itemIndex]['requirements'][i]['values'][0][0]
                continue
            if 'Int' in temp:
                valueInt = form.stashTabJson['items'][itemIndex]['requirements'][i]['values'][0][0]
                continue
        if valueLvl:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['rLvl'], QCI(valueLvl))
        if valueStr:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['rStr'], QCI(valueStr))
        if valueDex:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['rDex'], QCI(valueDex))
        if valueInt:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['rInt'], QCI(valueInt))
