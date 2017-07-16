# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemResistances(form, itemIndex, strengthValue, intelligenceValue, dataPropertiesImplicitExplicitLinesList):
    if dataPropertiesImplicitExplicitLinesList:
        #if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()).find('H Weapon)') >= 0:
        if dataPropertiesImplicitExplicitLines.find('Resistance') >= 0:
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
            if not strengthValue:
                strengthValue = 0


            for i in range (len(temp)):
                if ('% to' in temp[i]) and ('Fire' in temp[i]) and ('Resistance' in temp[i]):
                    dataF.append(int(temp[i].split('%')[0]))

                if ('% to' in temp[i]) and ('Lightning' in temp[i]) and ('Resistance' in temp[i]):
                    dataL.append(int(temp[i].split('%')[0]))

                if ('% to' in temp[i]) and ('Cold' in temp[i]) and ('Resistance' in temp[i]):
                    dataC.append(int(temp[i].split('%')[0]))

                if ('% to' in temp[i]) and ('Chaos' in temp[i]) and ('Resistance' in temp[i]):
                    dataCh.append(int(temp[i].split('%')[0]))

                elif ('% to all Elemental Resistances' in temp[i]):
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

                    # dataCsCh = temp[i].split(':')[1]
                    # dataCsCh = dataCsCh.split('%')
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resTotal'], QtGui.QTableWidgetItem(str(valueTotal)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resAll'], QtGui.QTableWidgetItem(str(valueAll)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resF'], QtGui.QTableWidgetItem(str(valueF)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resL'], QtGui.QTableWidgetItem(str(valueL)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resC'], QtGui.QTableWidgetItem(str(valueC)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resCh'], QtGui.QTableWidgetItem(str(valueCh)))
            #form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['csCh'], QtGui.QTableWidgetItem(str(dataCsCh[0])))
            # dataAPS = sum(data)
            # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['APS'], QtGui.QTableWidgetItem(str(dataAPS)))


