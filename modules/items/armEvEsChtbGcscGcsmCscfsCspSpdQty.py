# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemArmEvEsChtbGcscGcsmCscfsCspSpdQty(form, itemIndex, dataPropertiesImplicitExplicitLinesList, typeName):
    if dataPropertiesImplicitExplicitLinesList:
        temp = dataPropertiesImplicitExplicitLinesList
        valueArmour = ''
        valueEvasion = ''
        valueEnergyShield = ''
        valueChanceToBlock = ''
        dataGcsc = []
        dataGcsm = []
        dataCscfs = []
        dataCsp = []
        dataSpd = []
        valueGcsc = 0
        valueGcsm = 0
        valueCscfs = 0
        valueCsp = 0
        valueSpd = 0
        valueStackQuantity = ''
        for i in range (len(temp)):
            if 'Stack Size' in temp[i]:
                valueStackQuantity = temp[i].split(':')[1].split('/')[0]
            if typeName == 'Essence':
                break
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
            if '% increased Global Critical Strike Chance' in temp[i]:
                    dataGcsc.append(int(temp[i].split('%')[0]))
                    continue
            if '% to Global Critical Strike Multiplier' in temp[i]:
                    dataGcsm.append(int(temp[i].split('%')[0]))
                    continue
            if '% increased Critical Strike Chance for Spells' in temp[i]:
                    dataCscfs.append(int(temp[i].split('%')[0]))
                    continue
            if ('% increased Cast Speed' in temp[i]) and not ('Minions' in temp[i]) and not ('nearby' in temp[i]):
                    dataCsp.append(int(temp[i].split('%')[0]))
                    continue
            if '% increased Spell Damage' in temp[i]:
                    dataSpd.append(int(temp[i].split('%')[0]))
                    continue

        if dataGcsc:
            valueGcsc = sum(dataGcsc)

        if dataGcsm:
            valueGcsm = sum(dataGcsm)

        if dataCscfs:
            valueCscfs = sum(dataCscfs)

        if dataCsp:
            valueCsp = sum(dataCsp)

        if dataSpd:
            valueSpd = sum(dataSpd)
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Arm'], QtGui.QTableWidgetItem(str(valueArmour)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Ev'], QtGui.QTableWidgetItem(str(valueEvasion)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['ES'], QtGui.QTableWidgetItem(str(valueEnergyShield)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['ChtB'], QtGui.QTableWidgetItem(str(valueChanceToBlock)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['GcsC'], QtGui.QTableWidgetItem(str(valueGcsc)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['GcsM'], QtGui.QTableWidgetItem(str(valueGcsm)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['CscfS'], QtGui.QTableWidgetItem(str(valueCscfs)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Csp'], QtGui.QTableWidgetItem(str(valueCsp)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['SpD'], QtGui.QTableWidgetItem(str(valueSpd)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Qty'], QtGui.QTableWidgetItem(str(valueStackQuantity)))
