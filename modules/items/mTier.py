# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from modules.classes.custom.QTableWidgetItem import QCustomTableWidgetItem as QCI

def setItemMapTier(form, itemIndex, dataPropertiesImplicitExplicitLinesList, typeName):
    if dataPropertiesImplicitExplicitLinesList and typeName == 'Map':
            temp = dataPropertiesImplicitExplicitLinesList
            valueMTier = None
            for i in range (len(temp)):
                if ('Tier:' in temp[i]):
                    valueMTier = int(temp[i].split(':')[1])
            if valueMTier:
                form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['mTier'], QCI(str(valueMTier)))

