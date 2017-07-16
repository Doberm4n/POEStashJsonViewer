# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemArmEvEsChtb(form, itemIndex, dataPropertiesImplicitExplicitLinesList):
    if dataPropertiesImplicitExplicitLinesList:
        #if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()).find('H Weapon)') >= 0:
        #if dataPropertiesImplicitExplicitLines.find('Resistance') >= 0:
        temp = dataPropertiesImplicitExplicitLinesList
        #data = []
        #dataTotal = ''
        # data =
        # data =
        # data =
        # data =
        # dataCh = []
        valueArmour = ''
        valueEvasion = ''
        valueEnergyShield = ''
        valueChanceToBlock = ''
        # valueC = 0
        # valueCh = 0

        for i in range (len(temp)):
            if 'Armour:' in temp[i]:
                valueArmour = int(temp[i].split(':')[1].split('%')[0])
                continue

            if 'Evasion Rating:' in temp[i]:
                valueEvasion = int(temp[i].split(':')[1].split('%')[0])
                continue

            if 'Energy Shield:' in temp[i]:
                valueEnergyShield = int(temp[i].split(':')[1].split('%')[0])
                continue

            if 'Chance to Block:' in temp[i]:
                valueChanceToBlock = int(temp[i].split(':')[1].split('%')[0])
                continue




        # if dataAll:
        #     valueAll = sum(dataAll)

        # if dataF:
        #     valueF = sum(dataF) + valueAll
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

        # valueTotal = valueF + valueL + valueC + valueCh

                # dataCsCh = temp[i].split(':')[1]
                # dataCsCh = dataCsCh.split('%')
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Arm'], QtGui.QTableWidgetItem(str(valueArmour)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Ev'], QtGui.QTableWidgetItem(str(valueEvasion)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['ES'], QtGui.QTableWidgetItem(str(valueEnergyShield)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['ChtB'], QtGui.QTableWidgetItem(str(valueChanceToBlock)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resC'], QtGui.QTableWidgetItem(str(valueC)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resCh'], QtGui.QTableWidgetItem(str(valueCh)))
        #form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['csCh'], QtGui.QTableWidgetItem(str(dataCsCh[0])))
        # dataAPS = sum(data)
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['APS'], QtGui.QTableWidgetItem(str(dataAPS)))


