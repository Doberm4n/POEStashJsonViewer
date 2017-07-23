# -*- coding: utf-8 -*-
import os
import csv
from PyQt4 import QtGui

#csv comma delimited with headers, UTF-8
def exportAllToCsv(form):
    fileName = getCsvFileName()
    if fileName:
            form.tableWidget.setEnabled(False)
            with open(unicode(fileName), 'wb') as stream:
                csvWriter = csv.writer(stream)
                rowdata = []

                #column headers
                for columns in range(form.tableWidget.columnCount()):
                    columnHeaderText = unicode(form.tableWidget.horizontalHeaderItem(columns).text())
                    rowdata.append(columnHeaderText.encode('utf-8'))
                csvWriter.writerow(rowdata)

                #rows
                l = form.tableWidget.rowCount()
                for rows in range(l):
                    form.statusbar.showMessage('Processing ' + os.path.basename(unicode(fileName))  + ' (item ' + str(rows+1) + ' of ' + str(l) + ')')
                    rowdata = []
                    for columns in range(form.tableWidget.columnCount()):
                        item = form.tableWidget.item(rows, columns)
                        if item:
                            rowdata.append(unicode(item.text()).encode('utf-8'))
                        else:
                            rowdata.append('')
                    csvWriter.writerow(rowdata)
                form.statusbar.showMessage('Export complete')
                form.tableWidget.setEnabled(True)


#csv comma delimited with headers, UTF-8
def exportViewToCsv(form):
    fileName = getCsvFileName()
    if fileName:
            form.tableWidget.setEnabled(False)
            with open(unicode(fileName), 'wb') as stream:
                csvWriter = csv.writer(stream)
                rowdata = []

                #column headers
                for columns in range(form.tableWidget.columnCount()):
                    if not form.tableWidget.isColumnHidden(columns):
                        columnHeaderText = unicode(form.tableWidget.horizontalHeaderItem(columns).text())
                        rowdata.append(columnHeaderText.encode('utf-8'))
                csvWriter.writerow(rowdata)

                #rows
                l = form.tableWidget.rowCount()
                for rows in range(l):
                    if not form.tableWidget.isRowHidden(rows):
                        form.statusbar.showMessage('Processing ' + os.path.basename(unicode(fileName))  + ' (item ' + str(rows+1) + ' of ' + str(l) + ')')
                        rowdata = []
                        for columns in range(form.tableWidget.columnCount()):
                            if not form.tableWidget.isColumnHidden(columns):
                                item = form.tableWidget.item(rows, columns)
                                if item:
                                    rowdata.append(unicode(item.text()).encode('utf-8'))
                                else:
                                    rowdata.append('')
                        csvWriter.writerow(rowdata)
                form.statusbar.showMessage('Export complete')
                form.tableWidget.setEnabled(True)

def getCsvFileName():
    newName = QtGui.QFileDialog.getSaveFileName(None, 'Export to .csv', directory=os.getcwd(), filter='*.csv')
    return newName
