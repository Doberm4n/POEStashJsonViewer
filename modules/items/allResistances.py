# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemResistances(form, itemIndex, dataPropertiesImplicitExplicitLines, dataPropertiesImplicitExplicitLinesList, typeName):
    if dataPropertiesImplicitExplicitLinesList:
        if dataPropertiesImplicitExplicitLines.find('Resistance') >= 0:
            temp = dataPropertiesImplicitExplicitLinesList
            dataAll = []
            dataF = []
            dataL = []
            dataC = []
            dataCh = []
            valueTotal = 0
            valueAll = 0
            valueF = 0
            valueL = 0
            valueC = 0
            valueCh = 0
            for i in range (len(temp)):
                if typeName == 'Essence':
                    break
                if ('% to' in temp[i]) and ('Fire' in temp[i]) and ('Resistance' in temp[i]) and not ('enemies' in temp[i]):
                    dataF.append(int(temp[i].split('%')[0]))
                if ('% to' in temp[i]) and ('Lightning' in temp[i]) and ('Resistance' in temp[i]) and not ('enemies' in temp[i]):
                    dataL.append(int(temp[i].split('%')[0]))
                if ('% to' in temp[i]) and ('Cold' in temp[i]) and ('Resistance' in temp[i]) and not ('enemies' in temp[i]):
                    dataC.append(int(temp[i].split('%')[0]))
                if ('% to' in temp[i]) and ('Chaos' in temp[i]) and ('Resistance' in temp[i]):
                    dataCh.append(int(temp[i].split('%')[0]))
                elif ('% to all Elemental Resistances' in temp[i]) and not ('nearby' in temp[i]) and not ('Minions' in temp[i]) and not ('Totems' in temp[i]):
                    dataAll.append(int(temp[i].split('%')[0]))
            if dataAll:
                valueAll = sum(dataAll)
            if dataF:
                valueF = sum(dataF) + valueAll
            else:
                valueF = valueAll
            if dataL:
                valueL = sum(dataL) + valueAll
            else:
                valueL = valueAll
            if dataC:
                valueC = sum(dataC) + valueAll
            else:
                valueC = valueAll
            if dataCh:
                valueCh = sum(dataCh)
            valueTotal = valueF + valueL + valueC + valueCh
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resTotal'], QtGui.QTableWidgetItem(str(valueTotal)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resAll'], QtGui.QTableWidgetItem(str(valueAll)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resF'], QtGui.QTableWidgetItem(str(valueF)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resL'], QtGui.QTableWidgetItem(str(valueL)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resC'], QtGui.QTableWidgetItem(str(valueC)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resCh'], QtGui.QTableWidgetItem(str(valueCh)))
