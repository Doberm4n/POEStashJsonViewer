# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PyQt4 import QtGui
from PyQt4 import QtCore
import json
from json import loads
import generated.form_filter as GUIFilter

import modules.tools as tools
import modules.filter as tableWidgetFilters

import ui.main_layout as UIMainLayout

#import ui.main_layout as UIMainLayout

class filterDialog(QtGui.QDialog, GUIFilter.Ui_Dialog):
    def __init__(self, form):
        #global version
        #global link
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.closePushButton.clicked.connect(self.close)
        #form.tableWidget.setVisible(False)
        #print form.tableWidget.columnsCount()
        #self.linkLabel.linkActivated.connect(self.openURL)
        #self.versionLabel.setText("v." + version)
        #self.linkLabel.setText(link)
        #pic = self.picLabel
        #pic.setPixmap(QtGui.QPixmap(":todo-icon32.png"))
        #print form.ig.operandsText
        self.columnsHeadersComboBox.currentIndexChanged.connect(lambda: self.loadOperandsText(form))

        self.addFilterStringPushButton.clicked.connect(self.addFilterLine)
        self.applyFilterPushButton.clicked.connect(lambda: self.applyFilter(form))

        self.saveFilterPushButton.clicked.connect(lambda: self.saveFilter(form))
        self.loadFilterPushButton.clicked.connect(lambda: self.loadFilter(form))

        #self.filtersDir = parentdir + '\\Filters'

        self.prepareGui(form)




        #print form.tableWidget.horizontalHeaderItem(0).text()
        #print unicode(form.tableWidget.item(0, 0).text())

    def prepareGui(self, form):
        self.filterLinesTextEdit.setEnabled(False)
        self.valueLineEdit.setFocus()
        self.loadColumnsToFilterComboBox(form)
        self.loadFiltersToSavedFiltersComboBox(form)


    def loadColumnsToFilterComboBox(self, form):
        for i in range (form.tableWidget.columnCount()):
           self.columnsHeadersComboBox.addItem(form.tableWidget.horizontalHeaderItem(i).text())
        print ""

    def loadOperandsText(self, form):
        self.operandsComboBox.clear()
        #print form.ig.operandsText
        currentText = unicode(self.columnsHeadersComboBox.currentText())
        #print currentText
        #print form.ig.columnNameToIndex[currentText]

         #['type']

        #print form.ig.operandsText[form.ig.columnsHeaders[form.ig.columnNameToIndex[self.columnsHeadersComboBox.currentText()]]['type']]
        operandsText = form.ig.operandsText[form.ig.columnsHeaders[form.ig.columnNameToIndex[currentText]]['type']]
        for i in range (len(operandsText)):
            self.operandsComboBox.addItem(operandsText[i])

    def addFilterLine(self, main):
        #check isDigit
        print self.filterLinesTextEdit.toPlainText()
        if self.filterLinesTextEdit.toPlainText() == '':
            self.filterLinesTextEdit.setText(self.columnsHeadersComboBox.currentText() + ' [' + self.operandsComboBox.currentText() + '] ' + self.valueLineEdit.text())
        else:
            self.filterLinesTextEdit.setText(self.filterLinesTextEdit.toPlainText() + '\n' + self.columnsHeadersComboBox.currentText() + ' [' + self.operandsComboBox.currentText() + '] ' + self.valueLineEdit.text())
        print "rewrklwekrlewk;l"



    def getFilterFileName(self):
        newName = QtGui.QFileDialog.getSaveFileName(None, 'Save filter', directory=os.getcwd() + '\\Filters', filter='*.filter')
        return newName

    def saveFilter(self, form):
        print currentdir
        print parentdir
        print os.getcwd()

        filterLines = self.filterLinesTextEdit.toPlainText()
        if filterLines:
            data = {"filter":{"filterLines":[]}}
            temp = json.dumps(data)
            jsonData = loads(temp)
            filterLines = unicode(filterLines).splitlines()
            for i in range (len(filterLines)):
                jsonData['filter']['filterLines'].append(filterLines[i])
            print filterLines
            filterFileName = self.getFilterFileName()
            if filterFileName:
                tools.writeJson(jsonData, filterFileName)
                self.loadFiltersToSavedFiltersComboBox(form)
                #writeConfigAndLoadGuide(self, filterFileName)

    def loadFilter(self, form):
        if self.savedFiltersComboBox.currentText():
            filterJsonFileName = os.path.join(form.ig.filtersDir, unicode(self.savedFiltersComboBox.currentText()) + '.filter')
            if os.path.isfile(filterJsonFileName):
                print "Current text"
                filterJsonData = tools.readJson(filterJsonFileName)
                self.clearFilterLinesTextEdit()
                for i in range (len(filterJsonData['filter']['filterLines'])):
                    if self.filterLinesTextEdit.toPlainText() == '':
                        self.filterLinesTextEdit.setText(unicode(filterJsonData['filter']['filterLines'][i]))
                    else:
                        self.filterLinesTextEdit.setText(self.filterLinesTextEdit.toPlainText() + '\n' + unicode(filterJsonData['filter']['filterLines'][i]))
        #filterFileName = str(QtGui.QFileDialog.getOpenFileName(self, "Select guide", filter='*.filter', directory=self.curDir))


        #

    def loadFiltersToSavedFiltersComboBox(self, form):
        self.savedFiltersComboBox.clear()
        for file in os.listdir(form.ig.filtersDir):
            if os.path.isfile(os.path.join(form.ig.filtersDir, file)) and (file.endswith('.filter')):
                print os.path.splitext(file)[0]
                self.savedFiltersComboBox.addItem(os.path.splitext(file)[0])
        print ""

    def clearFilterLinesTextEdit(self):
        self.filterLinesTextEdit.clear()
        print ""

    def applyFilter(self, form):
        tableWidgetFilters.resetFilter(form)
        tableWidgetFilters.applyFilter(form, unicode(self.filterLinesTextEdit.toPlainText()).splitlines())
        #UIMainLayout.tableWidgetContentsAutoSize(form)











