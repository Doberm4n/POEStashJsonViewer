# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemArmEvEsChtbGcscGcsmCscfsCspSpdQty(form, itemIndex, dataPropertiesImplicitExplicitLinesList):
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

        dataGcsc = []
        dataGcsm = []
        dataCscfs = []
        dataCsp = []
        dataSpd = []
        # valueC = 0
        # valueCh = 0
        valueGcsc = 0
        valueGcsm = 0
        valueCscfs = 0
        valueCsp = 0
        valueSpd = 0

        valueStackQuantity = ''


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


            if '% increased Global Critical Strike Chance' in temp[i]:
                    dataGcsc.append(int(temp[i].split('%')[0]))
                    continue

            if '% to Global Critical Strike Multiplier' in temp[i]:
                    dataGcsm.append(int(temp[i].split('%')[0]))
                    continue

            if '% increased Critical Strike Chance for Spells' in temp[i]:
                    dataCscfs.append(int(temp[i].split('%')[0]))
                    continue

            if '% increased Cast Speed' in temp[i]:
                    dataCsp.append(int(temp[i].split('%')[0]))
                    continue

            if '% increased Spell Damage' in temp[i]:
                    dataSpd.append(int(temp[i].split('%')[0]))
                    continue

            if 'Stack Size' in temp[i]:
                valueStackQuantity = temp[i].split(':')[1].split('/')[0]






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

        # valueTotal = valueF + valueL + valueC + valueCh

                # dataCsCh = temp[i].split(':')[1]
                # dataCsCh = dataCsCh.split('%')
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
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resC'], QtGui.QTableWidgetItem(str(valueC)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resCh'], QtGui.QTableWidgetItem(str(valueCh)))
        #form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['csCh'], QtGui.QTableWidgetItem(str(dataCsCh[0])))
        # dataAPS = sum(data)
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['APS'], QtGui.QTableWidgetItem(str(dataAPS)))


