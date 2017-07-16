# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemAttributes(form, itemIndex, dataPropertiesImplicitExplicitLinesList):
    if dataPropertiesImplicitExplicitLinesList:
        #if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()).find('H Weapon)') >= 0:
        #if dataPropertiesImplicitExplicitLines.find('Resistance') >= 0:
        temp = dataPropertiesImplicitExplicitLinesList
        #data = []
        #dataTotal = ''
        dataAll = []
        dataS = []
        dataD = []
        dataI = []
        #dataCh = []
        valueTotal = 0
        valueAll = 0
        valueS = 0
        valueD = 0
        valueI = 0
        #valueCh = 0

        for i in range (len(temp)):
            if (' to ' in temp[i]) and ('Strength' in temp[i]) and not ('Level' in temp[i]):
                dataS.append(int(temp[i].split(' to ')[0]))

            if (' to ' in temp[i]) and ('Dexterity' in temp[i]) and not ('Level' in temp[i]):
                dataD.append(int(temp[i].split(' to ')[0]))

            if (' to ' in temp[i]) and ('Intelligence' in temp[i]) and not ('Level' in temp[i]):
                dataI.append(int(temp[i].split(' to ')[0]))

            # if (' to ' in temp[i]) and ('Strength' in temp[i]) and not ('Level' in temp[i]):
            #     dataCh.append(int(temp[i].split('%')[0]))

            elif (' to all Attributes' in temp[i]):
                dataAll.append(int(temp[i].split(' to ')[0]))


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

        # if dataCh:
        #     valueCh = sum(dataCh)

        valueTotal = valueS + valueD + valueI #+ valueCh

                # dataCsCh = temp[i].split(':')[1]
                # dataCsCh = dataCsCh.split('%')
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toAttrTotal'], QtGui.QTableWidgetItem(str(valueTotal)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resAll'], QtGui.QTableWidgetItem(str(valueAll)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toStr'], QtGui.QTableWidgetItem(str(valueS)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toDex'], QtGui.QTableWidgetItem(str(valueD)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['toInt'], QtGui.QTableWidgetItem(str(valueI)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resCh'], QtGui.QTableWidgetItem(str(valueCh)))
        #form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['csCh'], QtGui.QTableWidgetItem(str(dataCsCh[0])))
        # dataAPS = sum(data)
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['APS'], QtGui.QTableWidgetItem(str(dataAPS)))


