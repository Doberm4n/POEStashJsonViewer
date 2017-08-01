# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PyQt4 import QtGui
from PyQt4 import QtCore
import os
import modules.filter as tableWidgetFilters
import modules.tools as tools

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def applyLayout(self):
    self.tabWidget.show()
    self.tabsStash = QtGui.QWidget()
    self.tabsStash.setObjectName(_fromUtf8("tab"))
    self.tabsCurrency = QtGui.QWidget()
    self.tabsCurrency.setObjectName(_fromUtf8("tabCurrency"))
    self.verticalLayout = QtGui.QVBoxLayout(self.tabsStash)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.verticalLayoutCurrency = QtGui.QVBoxLayout(self.tabsCurrency)
    self.verticalLayoutCurrency.setObjectName(_fromUtf8("verticalLayoutCurrency"))
    self.groupBox = QtGui.QGroupBox(self.tabsStash)
    self.groupBox.setObjectName(_fromUtf8("groupBox"))
    self.groupBoxCurrency = QtGui.QGroupBox(self.tabsCurrency)
    self.groupBoxCurrency.setObjectName(_fromUtf8("groupBoxCurrency"))
    self.verticalLayout2 = QtGui.QVBoxLayout(self.groupBox)
    self.verticalLayout2.setObjectName(_fromUtf8("verticalLayout2"))
    self.verticalLayoutCurrency2 = QtGui.QVBoxLayout(self.groupBoxCurrency)
    self.verticalLayoutCurrency2.setObjectName(_fromUtf8("verticalLayoutCurrency2"))
    self.tabWidget.addTab(self.tabsStash, _fromUtf8(""))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabsStash), _translate("MainWindow", "Stash", None))
    self.tabWidget.addTab(self.tabsCurrency, _fromUtf8(""))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabsCurrency), _translate("MainWindow", "Currency", None))
    self.verticalLayout.addWidget(self.groupBox)
    self.verticalLayoutCurrency.addWidget(self.groupBoxCurrency)
    self.tableWidget = QtGui.QTableWidget(self.groupBox)
    self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
    self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
    self.tableWidget.setShowGrid(True)
    self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
    self.tableWidgetCurrency = QtGui.QTableWidget(self.groupBoxCurrency)
    self.tableWidgetCurrency.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
    self.tableWidgetCurrency.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
    self.tableWidgetCurrency.setShowGrid(True)
    self.tableWidgetCurrency.setObjectName(_fromUtf8("tableWidgetCurrency"))
    self.verticalLayout2.addWidget(self.tableWidget)
    self.verticalLayoutCurrency2.addWidget(self.tableWidgetCurrency)
    self.tableWidget.horizontalHeader().setVisible(True)
    self.tableWidget.verticalHeader().setVisible(True)
    self.tableWidget.setSortingEnabled(True)
    self.tableWidget.setEnabled(False)
    self.tableWidgetCurrency.horizontalHeader().setVisible(True)
    self.tableWidgetCurrency.verticalHeader().setVisible(True)
    self.tableWidgetCurrency.setSortingEnabled(True)
    self.tableWidgetCurrency.setEnabled(False)

    #add defined columns with headers from global_values for Stash
    for columns in range (len(self.ig.columnsHeaders)):
        self.tableWidget.insertColumn(columns)
        item = QtGui.QTableWidgetItem(self.ig.columnsHeaders[columns]['columnHeader'])
        self.tableWidget.setHorizontalHeaderItem(columns, item)
        item = self.tableWidget.horizontalHeaderItem(columns)
    self.savedFiltersComboBox.currentIndexChanged.connect(lambda: loadAndApplyFilter(self))

    #add defined columns with headers from global_values for Currency
    for columns in range (len(self.ig.columnsHeadersCurrency)):
        self.tableWidgetCurrency.insertColumn(columns)
        item = QtGui.QTableWidgetItem(self.ig.columnsHeadersCurrency[columns]['columnHeader'])
        self.tableWidgetCurrency.setHorizontalHeaderItem(columns, item)
        item = self.tableWidgetCurrency.horizontalHeaderItem(columns)
    #self.savedFiltersComboBox.currentIndexChanged.connect(lambda: loadAndApplyFilter(self))

def tableWidgetContentsAutoSize(form):
    scrollToTopLeftItem(form)
    form.statusbar.showMessage('Autosizing rows and columns...')
    form.tableWidget.resizeColumnsToContents()
    form.tableWidget.resizeRowsToContents()
    form.tableWidgetCurrency.resizeColumnsToContents()
    form.tableWidgetCurrency.resizeRowsToContents()
    form.statusbar.showMessage('Ready')

def scrollToTopLeftItem(form):
    if form.tableWidget.rowCount() > 0:
        column = None
        for i in range(len(form.ig.jsonConfig['view']['columns'])):
            if form.ig.jsonConfig['view']['columns'][i]['isHidden'] == False:
                column = i
                break
        if column == None:
            return
        if form.tableWidget.isRowHidden(0):
            form.tableWidget.showRow(0)
            form.tableWidget.scrollToItem(form.tableWidget.item(0, i))
            form.tableWidget.hideRow(0)
        else:
           form.tableWidget.scrollToItem(form.tableWidget.item(0, i))

def tableWidgetSetResizeMode(form):

    for i in range (form.tableWidget.columnCount()):
        form.tableWidget.horizontalHeader().setResizeMode(i, QtGui.QHeaderView.ResizeToContents)
    for j in range (form.tableWidget.rowCount()):
        form.tableWidget.verticalHeader().setResizeMode(j, QtGui.QHeaderView.ResizeToContents)

def setFixedColumnsWidth(self):
    for i in range (self.tableWidget.columnCount()):
        self.tableWidget.setColumnWidth(i, 125)
        self.tableWidget.item(0,2).setTextAlignment(QtCore.Qt.AlignCenter)

def tableWidgetDisableResizeToContents(form):
    for i in range (form.tableWidget.columnCount()):
        form.tableWidget.horizontalHeader().setResizeMode(i, QtGui.QHeaderView.Interactive)
    for j in range (form.tableWidget.rowCount()):
        form.tableWidget.verticalHeader().setResizeMode(j, QtGui.QHeaderView.Interactive)

def tableWidgetSetColumnsSelected(form):
     for i in range (form.tableWidget.columnCount()):
            if form.ig.jsonConfig['view']['columns'][i]['isHidden']:
                form.tableWidget.hideColumn(i)

def loadFiltersToSavedFiltersComboBox(form):
        form.savedFiltersComboBox.clear()
        form.savedFiltersComboBox.addItem('Saved filter selection')
        for file in os.listdir(form.ig.filtersDir):
            if os.path.isfile(os.path.join(form.ig.filtersDir, file)) and (file.endswith('.filter')):
                form.savedFiltersComboBox.addItem(os.path.splitext(file)[0])
        if not form.savedFiltersComboBox.currentText():
            return

def loadAndApplyFilter(form):
    if (form.savedFiltersComboBox.currentText()) and (form.savedFiltersComboBox.currentText() != 'Saved filter selection'):
        filterJsonFileName = os.path.join(form.ig.filtersDir, unicode(form.savedFiltersComboBox.currentText()) + '.filter')
        if os.path.isfile(filterJsonFileName):
            filterJsonData = tools.readJson(filterJsonFileName)
            applyFilter(form, filterJsonData)

def applyFilter(form, filterJsonData):
    form.statusbar.showMessage('Applying filter...')
    tableWidgetDisableResizeToContents(form)
    tableWidgetFilters.resetFilter(form)
    tableWidgetFilters.applyFilter(form, filterJsonData['filter']['filterLines'])
    tableWidgetContentsAutoSize(form)
    form.statusbar.showMessage('Filter applied' + ' (' + str(form.ig.itemFound) + ' items found)')
