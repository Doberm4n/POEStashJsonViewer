# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemApS(form, itemIndex, dataPropertiesImplicitExplicitLinesList):
    if dataPropertiesImplicitExplicitLinesList:
        if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()).find('H Weapon)') >= 0:
            temp = dataPropertiesImplicitExplicitLinesList
            data = []
            value = ''
            for i in range (len(temp)):
                if temp[i].find('Attacks per Second:') >= 0:
                    data.append(float(temp[i].split(':')[1]))
            value = sum(data)
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['APS'], QtGui.QTableWidgetItem(str(value)))


