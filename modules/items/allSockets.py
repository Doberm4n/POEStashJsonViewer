# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def setItemSockets(form, itemIndex):
    if form.stashTabJson['items'][itemIndex].has_key('sockets'):
        valueColorStr = 0
        valueColorDex = 0
        valueColorInt = 0
        valueColorWhite = 0
        groups = [0]*7
        colors = [0]*7
        valueMaxLinked = 0
        valueSocketsCount = len(form.stashTabJson['items'][itemIndex]['sockets'])
        dataVisualSockets = []
        valueVisualSockets = ''
        for i in range(valueSocketsCount):
            tempGroup = form.stashTabJson['items'][itemIndex]['sockets'][i]['group']
            tempColor = form.stashTabJson['items'][itemIndex]['sockets'][i]['attr']
            if tempColor == 'S': valueColorStr += 1
            elif tempColor == 'D': valueColorDex += 1
            elif tempColor == 'I': valueColorInt += 1
            else: valueColorWhite += 1
            groups[tempGroup] += 1
            if colors[tempGroup] == 0:
                colors[tempGroup] = tempColor
            else:
                colors[tempGroup] += ('-' + tempColor)
        for i in range(len(colors)):
            if colors[i] != 0:
                dataVisualSockets.append(colors[i])
        l = len(dataVisualSockets)
        for i in range(l):
            if i < (l-1):
                if len(dataVisualSockets[i]) > 1:
                    valueVisualSockets = valueVisualSockets + dataVisualSockets[i] + '\n'
                else:
                    valueVisualSockets = valueVisualSockets + dataVisualSockets[i] + ', '
            else:
                valueVisualSockets = valueVisualSockets + dataVisualSockets[i]
        valueMaxGroups = max(groups)
        if  valueMaxGroups > 1:
            valueMaxLinked = valueMaxGroups
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Sockets'], QtGui.QTableWidgetItem(str(valueSocketsCount)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['Linked'], QtGui.QTableWidgetItem(str(valueMaxLinked)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['LinksVisual'], QtGui.QTableWidgetItem(str(valueVisualSockets)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['sStr'], QtGui.QTableWidgetItem(str(valueColorStr)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['sDex'], QtGui.QTableWidgetItem(str(valueColorDex)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['sInt'], QtGui.QTableWidgetItem(str(valueColorInt)))
        form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['sWh'], QtGui.QTableWidgetItem(str(valueColorWhite)))



