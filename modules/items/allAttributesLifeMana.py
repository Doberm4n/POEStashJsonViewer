# -*- coding: utf-8 -*-
from __future__ import division
from PyQt4 import QtGui

def setItemAttributesLifeMana(form, itemIndex, dataPropertiesImplicitExplicitLinesList):
    if dataPropertiesImplicitExplicitLinesList:
        temp = dataPropertiesImplicitExplicitLinesList
        dataAll = []
        dataS = []
        dataD = []
        dataI = []
        valueTotal = 0
        valueAll = 0
        valueS = 0
        valueD = 0
        valueI = 0
        dataLifeAll = []
        dataManaAll = []
        valueLifeTotal = 0
        valueManaTotal = 0
        for i in range (len(temp)):
            if (' to ' in temp[i]) and ('Strength' in temp[i]) and not ('Level' in temp[i]):
                dataS.append(int(temp[i].split(' to ')[0]))
            if (' to ' in temp[i]) and ('Dexterity' in temp[i]) and not ('Level' in temp[i]):
                dataD.append(int(temp[i].split(' to ')[0]))
            if (' to ' in temp[i]) and ('Intelligence' in temp[i]) and not ('Level' in temp[i]):
                dataI.append(int(temp[i].split(' to ')[0]))
            elif (' to all Attributes' in temp[i]):
                dataAll.append(int(temp[i].split(' to ')[0]))
            if ' to maximum Life' in temp[i]:
                dataLifeAll.append(int(temp[i].split(' to ')[0]))
                continue
            if ' to maximum Mana' in temp[i]:
                dataManaAll.append(int(temp[i].split(' to ')[0]))
                continue
        if dataAll:
            valueAll = sum(dataAll)
        if dataS:
            valueS = sum(dataS) + valueAll
        else:
            valueS = valueAll
        if dataD:
            valueD = sum(dataD) + valueAll
        else:
            valueD = valueAll
        if dataI:
            valueI = sum(dataI) + valueAll
        else:
            valueI = valueAll
        if dataLifeAll:
            valueLifeTotal = sum(dataLifeAll)
        if dataManaAll:
            valueManaTotal = sum(dataLifeAll)
        valueTotal = valueS + valueD + valueI
        valueLifeTotal = valueLifeTotal + (valueS / 2)
        valueManaTotal = valueManaTotal + (valueI / 2)
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toAttrTotal'], QtGui.QTableWidgetItem(str(valueTotal)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toStr'], QtGui.QTableWidgetItem(str(valueS)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toDex'], QtGui.QTableWidgetItem(str(valueD)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toInt'], QtGui.QTableWidgetItem(str(valueI)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toMaxLife'], QtGui.QTableWidgetItem(str(valueLifeTotal)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toMaxMana'], QtGui.QTableWidgetItem(str(valueManaTotal)))
