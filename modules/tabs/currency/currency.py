# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PyQt4 import QtGui
from modules.classes.custom.QTableWidgetItem import QCustomTableWidgetItem as QCI

def setCurrency(form):
    currency = {}
    itemsCount = form.tableWidget.rowCount()
    for itemIndex in range(itemsCount):
        if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()) == 'Currency':
            if (not form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Name'])) or (not form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Qty'])):
                continue
            dataCurrency = unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Name']).text())
            dataQty = int(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Qty']).text())
            if not currency.has_key(dataCurrency):
                currency[dataCurrency] = dataQty
            else:
                currency[dataCurrency] += dataQty
    l = len(currency)
    for keys in currency.keys():
        i = 0
        form.statusbar.showMessage('Processing currency' + ' (item ' + str(i+1) + ' of ' + str(l) + ')')
        form.tableWidgetCurrency.insertRow(i)
        setItem(form, i, keys, currency[keys])
        i += 1

def setItem(form, itemIndex, currencyName, currencyValue):
    form.tableWidgetCurrency.setItem(itemIndex, form.ig.columnNameToIndexCurrency['Name'], QtGui.QTableWidgetItem(currencyName))
    form.tableWidgetCurrency.setItem(itemIndex, form.ig.columnNameToIndexCurrency['Total'], QCI(currencyValue))
