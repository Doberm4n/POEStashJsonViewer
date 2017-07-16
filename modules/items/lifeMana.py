# -*- coding: utf-8 -*-
from __future__ import division
from PyQt4 import QtGui

def setItemResistances(form, itemIndex, strengthValue, intelligenceValue, dataPropertiesImplicitExplicitLinesList):
    if dataPropertiesImplicitExplicitLinesList:
        #if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()).find('H Weapon)') >= 0:
        #if dataPropertiesImplicitExplicitLines.find('Resistance') >= 0:
        temp = dataPropertiesImplicitExplicitLinesList
        #data = []
        #dataTotal = ''
        dataLifeAll = []
        dataManaAll = []
        # dataF = []
        # dataL = []
        # dataC = []
        # dataCh = []
        valueLifeTotal = 0
        valueManaTotal = 0
        # valueAll = 0
        # valueF = 0
        # valueL = 0
        # valueC = 0
        # valueCh = 0

        for i in range (len(temp)):
            if ' to maximum Life' in temp[i]:
                dataLifeAll.append(int(temp[i].split(' to ')[0]))
            if ' to maximum Mana' in temp[i]:
                dataManaAll.append(int(temp[i].split(' to ')[0]))


        if dataLifeAll:
            valueLifeTotal = sum(dataLifeAll)

        if dataManaAll:
            valueManaTotal = sum(dataLifeAll)
        # else:
        #     valueF = valueAll

        # if dataL:
        #     valueL = sum(dataL) + valueAll
        # else:
        #     valueL = valueAll

        # if dataC:
        #     valueC = sum(dataC) + valueAll
        # else:
        #     valueC = valueAll

        # if dataCh:
        #     valueCh = sum(dataCh)

        valueLifeTotal = valueLifeTotal + (strengthValue / 2)
        valueManaTotal = valueManaTotal + (intelligenceValue / 2)


                # dataCsCh = temp[i].split(':')[1]
                # dataCsCh = dataCsCh.split('%')
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toMaxLife'], QtGui.QTableWidgetItem(str(valueLifeTotal)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toMaxMana'], QtGui.QTableWidgetItem(str(valueManaTotal)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resF'], QtGui.QTableWidgetItem(str(valueF)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resL'], QtGui.QTableWidgetItem(str(valueL)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resC'], QtGui.QTableWidgetItem(str(valueC)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resCh'], QtGui.QTableWidgetItem(str(valueCh)))
        #form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['csCh'], QtGui.QTableWidgetItem(str(dataCsCh[0])))
        # dataAPS = sum(data)
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['APS'], QtGui.QTableWidgetItem(str(dataAPS)))


