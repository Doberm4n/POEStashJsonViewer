# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemApsCsch(form, itemIndex, dataPropertiesImplicitExplicitLinesList):
    if dataPropertiesImplicitExplicitLinesList:
        if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()).find('H Weapon)') >= 0:
            temp = dataPropertiesImplicitExplicitLinesList
            data = []
            dataAPS = ''
            dataCsCh = ''
            for i in range (len(temp)):
                if temp[i].find('Attacks per Second:') >= 0:
                    data.append(float(temp[i].split(':')[1]))
                elif temp[i].find('Critical Strike Chance: ') >= 0:
                    dataCsCh = temp[i].split(':')[1]
                    dataCsCh = dataCsCh.split('%')
                    form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['csCh'], QtGui.QTableWidgetItem(str(dataCsCh[0])))
            dataAPS = sum(data)
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['APS'], QtGui.QTableWidgetItem(str(dataAPS)))


