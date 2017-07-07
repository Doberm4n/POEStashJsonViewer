# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore

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
    self.buttonsText = None
    self.buttonsComplete = None
    self.buttonsText = {}
    self.buttonsComplete = {}
    self.tabs = {}
    self.verticalLayout = {}
    self.scrollArea = {}
    self.scrollAreaWidgetContent = {}
    self.groupBox = {}
    self.formLayout = {}
    self.gridLayout = {}
    self.firstTab = False
    self.tabWidget.show()
    tabs_count = self.tabWidget.count()
    #print "tabs_count init = " + str(tabs_count)
    #tabsCount = len(guideJson['guide']['tabs'])
    #for tabs in range (tabsCount):
    #guideActKey = 'act_' + str(tabs + 1)
    #if not guideJson['guide']['tabs'][tabs]['text']:
        #print "tabs " + str(tabs)
    self.tabs = QtGui.QWidget()
    self.tabs.setObjectName(_fromUtf8("tab"))
    self.verticalLayout = QtGui.QVBoxLayout(self.tabs)
    self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
    self.verticalLayout.setSpacing(11)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.scrollArea = QtGui.QScrollArea(self.tabs)
    self.scrollArea.setWidgetResizable(True)
    self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
    self.scrollAreaWidgetContent = QtGui.QWidget()
    self.scrollAreaWidgetContent.setGeometry(QtCore.QRect(0, 0, 0, 0))
    self.scrollAreaWidgetContent.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
    self.formLayout = QtGui.QFormLayout(self.scrollAreaWidgetContent)
    self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
    self.formLayout.setObjectName(_fromUtf8("formLayout"))
    self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContent)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
    self.groupBox.setSizePolicy(sizePolicy)
    self.groupBox.setObjectName(_fromUtf8("groupBox"))
    self.gridLayout = QtGui.QGridLayout(self.groupBox)
    self.gridLayout.setVerticalSpacing(2)
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox)
    self.scrollArea.setWidget(self.scrollAreaWidgetContent)
    self.verticalLayout.addWidget(self.scrollArea)
    self.tabWidget.addTab(self.tabs, _fromUtf8(""))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs), _translate("MainWindow", "Stash", None))
    self.gridLayout.setColumnStretch(0, 0)
    #self.gridLayout.setVerticalSpacing(2)

    #add tableWidget
    self.tableWidget = QtGui.QTableWidget(self.groupBox)
    #self.tableWidget.setGeometry(QtCore.QRect(15, 20, 100, 100))
    self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
    self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
    self.tableWidget.setShowGrid(True)
    self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
    self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
    self.tableWidget.horizontalHeader().setVisible(True)
    self.tableWidget.verticalHeader().setVisible(True)

     #add defined columns
            textLength = len(stashJson[0]['items'])
            for columns in range (len(self.ig.columnsHeaders)):
                self.tableWidget.insertColumn(columns)