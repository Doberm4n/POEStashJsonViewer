# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from modules.classes.custom.QTableWidgetItem import QCustomTableWidgetItem as QCI

def setItemArmEvEsChtbGcscGcsmCscfsCspSpdQty(form, itemIndex, dataPropertiesImplicitExplicitLinesList, typeName):
    if dataPropertiesImplicitExplicitLinesList:
        temp = dataPropertiesImplicitExplicitLinesList
        valueArmour = 0
        valueEvasion = 0
        valueEnergyShield = 0
        valueChanceToBlock = 0
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
        valueStackQuantity = None
        for i in range (len(temp)):
            if 'Stack Size' in temp[i]:
                valueStackQuantity = int(temp[i].split(':')[1].split('/')[0])
                continue
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

        #non stackable currency
        if typeName == 'Currency' and not valueStackQuantity:
            valueStackQuantity = 1

        if valueArmour:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Arm'], QCI(valueArmour))
        if valueEvasion:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Ev'], QCI(valueEvasion))
        if valueEnergyShield:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['ES'], QCI(valueEnergyShield))
        if valueChanceToBlock:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['ChtB'], QCI(valueChanceToBlock))
        if valueGcsc:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['GcsC'], QCI(valueGcsc))
        if valueGcsm:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['GcsM'], QCI(valueGcsm))
        if valueCscfs:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['CscfS'], QCI(valueCscfs))
        if valueCsp:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Csp'], QCI(valueCsp))
        if valueSpd:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['SpD'], QCI(valueSpd))
        if valueStackQuantity:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Qty'], QCI(valueStackQuantity))
