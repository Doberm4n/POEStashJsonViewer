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
    self.setWindowTitle(self.windowTitle)
    # self.buttonsText = None
    # self.buttonsComplete = None
    # self.buttonsText = {}
    # self.buttonsComplete = {}
    #self.tabs = {}
    #self.verticalLayout = {}
    # self.scrollArea = {}
    # self.scrollAreaWidgetContent = {}
    # self.groupBox = {}
    # self.formLayout = {}
    # self.gridLayout = {}
    # self.firstTab = False
    self.tabWidget.show()
    self.tabs = QtGui.QWidget()
    self.tabs.setObjectName(_fromUtf8("tab"))
    self.verticalLayout = QtGui.QVBoxLayout(self.tabs)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.groupBox = QtGui.QGroupBox(self.tabs)
    self.groupBox.setObjectName(_fromUtf8("groupBox"))
    self.verticalLayout2 = QtGui.QVBoxLayout(self.groupBox)
    self.verticalLayout2.setObjectName(_fromUtf8("verticalLayout2"))
    self.tabWidget.addTab(self.tabs, _fromUtf8(""))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs), _translate("MainWindow", "Stash", None))
    self.verticalLayout.addWidget(self.groupBox)
    #add tableWidget
    self.tableWidget = QtGui.QTableWidget(self.groupBox)
    self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
    self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
    self.tableWidget.setShowGrid(True)
    self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
    self.verticalLayout2.addWidget(self.tableWidget)
    self.tableWidget.horizontalHeader().setVisible(True)
    self.tableWidget.verticalHeader().setVisible(True)
    self.tableWidget.setSortingEnabled(True)
    self.tableWidget.setVisible(False)
    self.tableWidget.setEnabled(False)
    #add defined columns with headers from global_values
    for columns in range (len(self.ig.columnsHeaders)):
        # if (not self.ig.jsonConfig['common']['calculateSpecifiedColumns']) and (self.ig.columnsHeaders[columns]['isCalc']):
        #     continue
        self.tableWidget.insertColumn(columns)
        item = QtGui.QTableWidgetItem(self.ig.columnsHeaders[columns]['columnHeader'])
        self.tableWidget.setHorizontalHeaderItem(columns, item)
        item = self.tableWidget.horizontalHeaderItem(columns)

    self.savedFiltersComboBox.currentIndexChanged.connect(lambda: loadAndApplyFilter(self))


    #self.savedFiltersComboBox.setMinimumWidth(700)
    # self.openGuidePushButton.setMaximumHeight(20)
    # self.savedFiltersComboBox.setMaximumHeight(18)

    #self.toolBar.addWidget(self.openGuidePushButton)
    #self.toolBar.addSeparator()
    #self.toolBar.addWidget(self.savedFiltersComboBox)
    #self.toolBar.setMinimumHeight(25)
    #self.toolBar.setStyleSheet('QToolBar{spacing:5px;}')
    # self.openGuidePushButton.setGeometry(5, 5, 20, 20)
    # self.savedFiltersComboBox.setGeometry(5,20, 20, 20)

    # self.tableWidget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
    # self.tableWidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
    # self.tableWidget.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
    # self.tableWidget.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
    # self.tableWidget.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
    # self.tableWidget.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
    # self.tableWidget.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
    # self.tableWidget.horizontalHeader().setResizeMode(7, QtGui.QHeaderView.ResizeToContents)
    # self.tableWidget.horizontalHeader().setResizeMode(8, QtGui.QHeaderView.ResizeToContents)
    #set autoSize
    #self.tableWidget.resizeColumnsToContents()
    #self.tableWidget.resizeRowsToContents()

def tableWidgetContentsAutoSize(form):
    form.tableWidget.resizeColumnsToContents()
    form.tableWidget.resizeRowsToContents()
    print "Auto sized"


def tableWidgetSetResizeMode(form):

    for i in range (form.tableWidget.columnCount()):
        # if self.ig.columnsHeaders[i]['columnHeader'] == 'iLvl' or \
        # self.ig.columnsHeaders[i]['columnHeader'] == 'Rarity':
        #      self.tableWidget.setColumnWidth(i, 27)
        #      self.tableWidget.item(0,2).setTextAlignment(QtCore.Qt.AlignCenter)
        #      continue
        #print unicode(self.tableWidget.item(0,0).text())

        form.tableWidget.horizontalHeader().setResizeMode(i, QtGui.QHeaderView.ResizeToContents)
    for j in range (form.tableWidget.rowCount()):
    #print ""
        form.tableWidget.verticalHeader().setResizeMode(j, QtGui.QHeaderView.ResizeToContents)
        #self.tableWidget.horizontalHeader().setDefaultSectionSize(20)

def tableWidgetDisableResizeToContents(form):
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

def tableWidgetSetColumnsSelected(form):
     for i in range (form.tableWidget.columnCount()):
            if form.ig.jsonConfig['view']['columns'][i]['isHidden']:
            #self.columnsSelectListWidget.item(i).checkState() == Qt.Checked:
                form.tableWidget.hideColumn(i)

            # else:
            #     form.tableWidget.hideColumn(i)
            #     self.jsonConfig['view']['columns'][i]['isHidden'] = True
            #     print "Checked " + self.columnsSelectListWidget.item(i).text()

def loadFiltersToSavedFiltersComboBox(form):
        form.savedFiltersComboBox.clear()
        form.savedFiltersComboBox.addItem('No filters selected')
        for file in os.listdir(form.ig.filtersDir):
            if os.path.isfile(os.path.join(form.ig.filtersDir, file)) and (file.endswith('.filter')):
                print os.path.splitext(file)[0]
                form.savedFiltersComboBox.addItem(os.path.splitext(file)[0])
        if not form.savedFiltersComboBox.currentText():

            print ""


def loadAndApplyFilter(form):
    print "Checking currentIndex"
    if (form.savedFiltersComboBox.currentText()) and (form.savedFiltersComboBox.currentText() != 'No filters selected'):
        filterJsonFileName = os.path.join(form.ig.filtersDir, unicode(form.savedFiltersComboBox.currentText()) + '.filter')
        if os.path.isfile(filterJsonFileName):
            print "Current text"
            filterJsonData = tools.readJson(filterJsonFileName)
            applyFilter(form, filterJsonData)


def applyFilter(form, filterJsonData):
    tableWidgetFilters.resetFilter(form)
    tableWidgetFilters.applyFilter(form, filterJsonData['filter']['filterLines'])
    tableWidgetContentsAutoSize(form)
