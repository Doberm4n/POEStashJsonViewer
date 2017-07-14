# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PyQt4.QtCore import *
import ui.main_layout as UIMainLayout
import modules.filter as tableWidgetFilters
import global_values

class filterThread(QThread):

    disableResizeSignal = pyqtSignal(object)
    resizeSignal = pyqtSignal(object)
    #resizeRowsSignal = pyqtSignal(object)

    def __init__(self, form, filterLines, minValue, maxValue):
        QThread.__init__(self)
        self.form = form
        self.minValue = minValue
        self.maxValue = maxValue
        self.filterLines = filterLines
        print self.filterLines
        # self.
        # self.
        #global form

    def run(self):
        self.setFilter()

        #self.downloadURL(self.url, self.filename)

    def setFilter(self):
        print ""
        #UIMainLayout.tableWidgetDisableResizeToContentsThreaded(self.form, self.minValue, self.maxValue)
        #tableWidgetFilters.resetFilter(self.form)

        self.disableResizeSignal.emit(str(self.minValue) + 'to' + str(self.maxValue))

        self.applyFilter(self.form, self.filterLines)

        # print self.form.tableWidget.isRowHidden(0)
        # print self.form.tableWidget.rowCount()
        # print unicode(self.form.tableWidget.item(0, self.form.ig.columnNameToIndex['Name']))
        # print unicode(self.form.tableWidget.item(0, self.form.ig.columnNameToIndex['Name']).text())
        #timers error self.form.tableWidget.hideRow(0)
        #form.repaint()
        #UIMainLayout.tableWidgetContentsAutoSizeThreaded(self.form)
        self.resizeSignal.emit('')

        #self.resizeRowsSignal.emit(str(self.minValue) + 'to' + str(self.maxValue))
        #self.form.tableWidget.resizeColumnsToContents()
        #self.tableWidgetContentsAutoSizeThreaded(0)
        # self.form.tableWidget.hideRow(0)
        # print unicode(self.form.tableWidget.item(0, self.form.ig.columnNameToIndex['Name']).text())

        #self.form.setEnabled(False)
        #form.setEnabled(False)

        #self.enableButtons()

    def disableButtons(self):
        form.downloadcoverpushButton.setEnabled(False)
        form.downloadtrailerpushButton.setEnabled(False)

    def enableButtons(self):
        form.downloadcoverpushButton.setEnabled(True)
        form.downloadtrailerpushButton.setEnabled(True)
        #form.setEnabled(True)

    def tableWidgetContentsAutoSizeThreaded(self, form):
        self.form.tableWidget.resizeColumnsToContents()
        self.form.tableWidget.resizeRowsToContents()
        print "Auto sized"

    def tableWidgetDisableResizeToContentsThreaded(form, minValue, maxValue):
        for i in range (form.tableWidget.columnCount()):
            # if self.ig.columnsHeaders[i]['columnHeader'] == 'iLvl' or \
            # self.ig.columnsHeaders[i]['columnHeader'] == 'Rarity':
            #      self.tableWidget.setColumnWidth(i, 27)
            #      self.tableWidget.item(0,2).setTextAlignment(QtCore.Qt.AlignCenter)
            #      continue
            #print unicode(self.tableWidget.item(0,0).text())

            form.tableWidget.horizontalHeader().setResizeMode(i, QtGui.QHeaderView.Fixed)
        for j in range (form.tableWidget.rowCount()):
        #print ""
            form.tableWidget.verticalHeader().setResizeMode(j, QtGui.QHeaderView.Fixed)
            #self.tableWidget.horizontalHeader().setDefaultSectionSize(20)


    def applyFilter(self, form, filterLines):
        print filterLines
        if filterLines != '':
            filters = {}
            filters.update({'filters' : []})

            #filterLines = filterLines
            print 'Length: ' + str(len(filterLines))
            for i in range (len(filterLines)):
                filters['filters'].append({'columnHeader' : None, 'operand' : None, 'filterValue' : None, 'filterType' : None})

                temp = filterLines[i].split(' [')
                filters['filters'][i]['columnHeader'] = temp[0]
                filters['filters'][i]['operand'] = temp[1].split('] ')[0]

                filters['filters'][i]['filterType'] = form.ig.columnsHeaders[form.ig.columnNameToIndex[temp[0]]]['type']

                # if (filters['filters'][i]['operand'].find('contains') >= 0) or (filters['filters'][i]['operand'].find('match') >=0):
                #     filters['filters'][i]['operand'] = filters['filters'][i]['operand'].replace('match', '=')
                #     filters['filters'][i]['filterType'] = 'String'
                # else:
                #     filters['filters'][i]['filterType'] = 'Integer'

                if filters['filters'][i]['filterType'] == 'String':
                    filters['filters'][i]['operand'] = filters['filters'][i]['operand'].replace('match', '=')

                filters['filters'][i]['filterValue'] = temp[1].split('] ')[1]

                filters['filters'][i]['operand'] = form.ig.operandsChars[filters['filters'][i]['operand']]

            print filters['filters']
            self.filterTable(form, filters)

    def filterTable(self, form, filters):
        for i in range (len(filters['filters'])):
            columnHeader = filters['filters'][i]['columnHeader']
            filterType = filters['filters'][i]['filterType']
            filterValue = filters['filters'][i]['filterValue']

            operand = filters['filters'][i]['operand']

            #print unicode(form.tableWidget.item(0, form.ig.columnNameToIndex[columnHeader]).text())
            print columnHeader
            print filterType
            print filterValue
            print operand
            for j in range (form.tableWidget.rowCount()):
                print "=======================================Row " + " ======================================="
                if form.tableWidget.isRowHidden(j) == True:
                    continue
                if form.tableWidget.item(j, form.ig.columnNameToIndex[columnHeader]):
                    itemValue = form.tableWidget.item(j, form.ig.columnNameToIndex[columnHeader]).text()
                else:
                    itemValue = ''
                #if not itemValue:
                if (filterType == 'String') and (filters['filters'][i]['operand'] == operator.contains):
                    if (not operand(unicode(itemValue).lower(), filterValue.lower())):
                        form.tableWidget.hideRow(j)
                elif (filterType == 'String'):
                        if (not operand(unicode(itemValue), filterValue)):
                            form.tableWidget.hideRow(j)
                else:
                    if not itemValue:
                        form.tableWidget.hideRow(j)
                    else:
                        filterValue = float(filterValue)
                        if (not operand(float(itemValue), filterValue)):
                            form.tableWidget.hideRow(j)
        print "Applied"

    def resetFilterThreaded(form):
        for i in range (form.tableWidget.rowCount()):
            print "=======================================Reset " + str(i) + " ======================================="
            #if form.tableWidget.isRowHidden(i):
            form.tableWidget.showRow(i)



