# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemResistances(form, itemIndex, dataPropertiesImplicitExplicitLines, dataPropertiesImplicitExplicitLinesList):
    if dataPropertiesImplicitExplicitLinesList:
        #if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()).find('H Weapon)') >= 0:
        if dataPropertiesImplicitExplicitLines.find('Resistance') >= 0:
            temp = dataPropertiesImplicitExplicitLinesList
            data = []
            dataTotal = ''
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
                if (temp[i].find('Fire') >= 0) and (temp[i].find('Resistance') >= 0):
                    dataF.append(int(temp[i].split('%')[0]))

                if (temp[i].find('Lightning') >= 0) and (temp[i].find('Resistance') >= 0):
                    dataL.append(int(temp[i].split('%')[0]))

                if (temp[i].find('Cold') >= 0) and (temp[i].find('Resistance') >= 0):
                    dataC.append(int(temp[i].split('%')[0]))

                if (temp[i].find('Chaos') >= 0) and (temp[i].find('Resistance') >= 0):
                    dataCh.append(int(temp[i].split('%')[0]))

                elif temp[i].find('% to all Elemental Resistances') >= 0:
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


