# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
from PyQt4 import QtGui
import modules.calc.dpsCalc as dpsCalc
from modules.classes.custom.QTableWidgetItem import QCustomTableWidgetItem as QCI

def setItemDpsPdpsEdpsFdpsLdpsCdpsChDps(form, itemIndex, dataPropertiesImplicitExplicit):
    valueType = unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text())
    valueRarity = form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Rarity']).text()
    if 'H Weapon' in valueType and ('Rare' in valueRarity or 'Unique' in valueRarity):
        dataQuality = form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Quality'])
        if dataQuality:
           dataQuality = dataQuality.text()
        else:
            dataQuality = '0'
        dataQuality = 'Quality: +' + dataQuality + '\n'
        data = dataQuality + unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['PropertiesImplicitExplicit']).text())
        _dpsCalc = dpsCalc.dpsCalc()
        if _dpsCalc.Calc(unicode(data)):
            if _dpsCalc.totalDPS:
                form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['DPS'], QCI(_dpsCalc.totalDPS))
            if _dpsCalc.valueElemental:
                form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['eDPS'], QCI(_dpsCalc.valueElemental))
            if _dpsCalc.valuePhysical:
                form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['pDPS'], QCI(_dpsCalc.valuePhysical))
            if _dpsCalc.valueFire:
                form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['fDPS'], QCI(_dpsCalc.valueFire))
            if _dpsCalc.valueLightning:
                form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['lDPS'], QCI(_dpsCalc.valueLightning))
            if _dpsCalc.valueCold:
                form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['cDPS'], QCI(_dpsCalc.valueCold))
            if _dpsCalc.valueChaos:
                form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['ChDPS'], QCI(_dpsCalc.valueChaos))
        else:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['DPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['eDPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['pDPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['fDPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['lDPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['cDPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['ChDPS'], QtGui.QTableWidgetItem('0'))
