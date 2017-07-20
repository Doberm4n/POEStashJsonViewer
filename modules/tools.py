# -*- coding: utf-8 -*-
import os
from PyQt4 import QtGui
from json import load
from json import loads
import json
from time import time

def readJson(json_file):
        if json_file:
            #try:
                with open(json_file) as data_file:
                    return load(data_file)
            #except Exception, e:
                 #print "Error: " + str(e)

def writeJson(dump, json_file):
    if json_file:
        #try:
            #print ""
            with open(json_file, 'w') as outfile:
                    json.dump(dump, outfile)
        #except Exception, e:
             #print "Error: " + str(e)

def getSingleJsonFileName():
    return QtGui.QFileDialog.getSaveFileName(None, 'Save to single json', directory=os.getcwd(), filter='*.single_json')

def getMySQLDatabaseFileName():
    return QtGui.QFileDialog.getSaveFileName(None, 'Save to MySQL Database', directory=os.getcwd(), filter='*.db')

def openSingleJsonFileName(directoryName):
    return unicode(QtGui.QFileDialog.getOpenFileName(None, "Select json", directory=directoryName, filter='*.single_json'))

def printTime(start):
    end = time()
    duration = end - start
    if duration < 60:
        return "used: " + str(round(duration, 2)) + "s."
    else:
        mins = int(duration / 60)
        secs = round(duration % 60, 2)
        if mins < 60:
            return "used: " + str(mins) + "m " + str(secs) + "s."
        else:
            hours = int(duration / 3600)
            mins = mins % 60
            return "used: " + str(hours) + "h " + str(mins) + "m " + str(secs) + "s."


# def tableWidgetSetResizeMode(form):

#         for i in range (form.tableWidget.columnCount()):
#             # if self.ig.columnsHeaders[i]['columnHeader'] == 'iLvl' or \
#             # self.ig.columnsHeaders[i]['columnHeader'] == 'Rarity':
#             #      self.tableWidget.setColumnWidth(i, 27)
#             #      self.tableWidget.item(0,2).setTextAlignment(QtCore.Qt.AlignCenter)
#             #      continue
#             #print unicode(self.tableWidget.item(0,0).text())

#             form.tableWidget.horizontalHeader().setResizeMode(i, QtGui.QHeaderView.ResizeToContents)
#         for j in range (form.tableWidget.rowCount()):
#         #print ""
#             form.tableWidget.verticalHeader().setResizeMode(j, QtGui.QHeaderView.ResizeToContents)

