# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
from PyQt4 import QtGui
import modules.calc.dpsCalc as dpsCalc

def setItemDpsPdpsEdpsFdpsLdpsCdpsChDps(form, itemIndex, dataPropertiesImplicitExplicit):
    if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()).find('H Weapon)') >= 0:
        dataQuality = form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Quality']).text()
        if dataQuality:
            dataQuality = 'Quality: +' + dataQuality + '\n'
        data = dataQuality + unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['PropertiesImplicitExplicit']).text())
        _dpsCalc = dpsCalc.dpsCalc()
        if _dpsCalc.Calc(unicode(data)):
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['DPS'], QtGui.QTableWidgetItem(str(_dpsCalc.totalDPS)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['eDPS'], QtGui.QTableWidgetItem(str(_dpsCalc.valueElemental)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['pDPS'], QtGui.QTableWidgetItem(str(_dpsCalc.valuePhysical)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['fDPS'], QtGui.QTableWidgetItem(str(_dpsCalc.valueFire)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['lDPS'], QtGui.QTableWidgetItem(str(_dpsCalc.valueLightning)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['cDPS'], QtGui.QTableWidgetItem(str(_dpsCalc.valueCold)))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['ChDPS'], QtGui.QTableWidgetItem(str(_dpsCalc.valueChaos)))
        else:
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['DPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['eDPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['pDPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['fDPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['lDPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['cDPS'], QtGui.QTableWidgetItem('0'))
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['ChDPS'], QtGui.QTableWidgetItem('0'))
