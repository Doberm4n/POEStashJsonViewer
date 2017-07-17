# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemRequirements(form, itemIndex):
    if form.stashTabJson['items'][itemIndex].has_key('requirements'):
        #if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()).find('H Weapon)') >= 0:
        #if dataPropertiesImplicitExplicitLines.find('Resistance') >= 0:
        #temp = dataPropertiesImplicitExplicitLinesList

        #data = []
        #dataTotal = ''
        # data =
        # data =
        # data =
        # data =
        # dataCh = []
        valueLvl = ''
        valueStr = ''
        valueInt = ''
        valueDex = ''

        # dataGcsc = []
        # dataGcsm = []
        # dataCscfs = []
        # dataCsp = []
        # dataSpd = []
        # # valueC = 0
        # # valueCh = 0
        # valueGcsc = 0
        # valueGcsm = 0
        # valueCscfs = 0
        # valueCsp = 0
        # valueSpd = 0

#         def setItemRequirementsLvl(self, itemIndex):
#     dataLvl = ''
#     if :
#         for i in range ():
#             if self.stashTabJson['items'][itemIndex]['properties'][i]['name'] == 'Quality':

# def setItemRequirementsStr(self, itemIndex):
#     dataStr = ''

# def setItemRequirementsDex(self, itemIndex):
#     dataDex = ''

# def setItemRequirementsInt(self, itemIndex):
#     dataInt = ''


        for i in range (len(form.stashTabJson['items'][itemIndex]['requirements'])):
            temp = form.stashTabJson['items'][itemIndex]['requirements'][i]['name']

            if 'Level' in temp:
                valueLvl = form.stashTabJson['items'][itemIndex]['requirements'][i]['values'][0][0]
                continue

            if 'Str' in temp:
                valueStr = form.stashTabJson['items'][itemIndex]['requirements'][i]['values'][0][0]
                continue

            if 'Dex' in temp:
                valueDex = form.stashTabJson['items'][itemIndex]['requirements'][i]['values'][0][0]
                continue

            if 'Int' in temp:
                valueInt = form.stashTabJson['items'][itemIndex]['requirements'][i]['values'][0][0]
                continue


            # if '% increased Global Critical Strike Chance' in temp[i]:
            #         dataGcsc.append(int(temp[i].split('%')[0]))
            #         continue

            # if '% to Global Critical Strike Multiplier' in temp[i]:
            #         dataGcsm.append(int(temp[i].split('%')[0]))
            #         continue

            # if '% increased Critical Strike Chance for Spells' in temp[i]:
            #         dataCscfs.append(int(temp[i].split('%')[0]))
            #         continue

            # if '% increased Cast Speed' in temp[i]:
            #         dataCsp.append(int(temp[i].split('%')[0]))
            #         continue

            # if '% increased Spell Damage' in temp[i]:
            #         dataSpd.append(int(temp[i].split('%')[0]))
            #         continue





        # if dataGcsc:
        #     valueGcsc = sum(dataGcsc)

        # if dataGcsm:
        #     valueGcsm = sum(dataGcsm)

        # if dataCscfs:
        #     valueCscfs = sum(dataCscfs)

        # if dataCsp:
        #     valueCsp = sum(dataCsp)

        # if dataSpd:
        #     valueSpd = sum(dataSpd)

        # valueTotal = valueF + valueL + valueC + valueCh

                # dataCsCh = temp[i].split(':')[1]
                # dataCsCh = dataCsCh.split('%')
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['rLvl'], QtGui.QTableWidgetItem(str(valueLvl)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['rStr'], QtGui.QTableWidgetItem(str(valueStr)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['rDex'], QtGui.QTableWidgetItem(str(valueDex)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['rInt'], QtGui.QTableWidgetItem(str(valueInt)))

        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['GcsC'], QtGui.QTableWidgetItem(str(valueGcsc)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['GcsM'], QtGui.QTableWidgetItem(str(valueGcsm)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['CscfS'], QtGui.QTableWidgetItem(str(valueCscfs)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Csp'], QtGui.QTableWidgetItem(str(valueCsp)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['SpD'], QtGui.QTableWidgetItem(str(valueSpd)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resC'], QtGui.QTableWidgetItem(str(valueC)))
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['resCh'], QtGui.QTableWidgetItem(str(valueCh)))
        #form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['csCh'], QtGui.QTableWidgetItem(str(dataCsCh[0])))
        # dataAPS = sum(data)
        # form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['APS'], QtGui.QTableWidgetItem(str(dataAPS)))