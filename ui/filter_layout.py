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


class filterDialog(QtGui.QDialog, GUIFilter.Ui_Dialog):
    def __init__(self, form):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.closePushButton.clicked.connect(self.close)
        self.columnsHeadersComboBox.currentIndexChanged.connect(lambda: self.loadOperandsText(form))
        self.addFilterStringPushButton.clicked.connect(lambda: self.addFilterLine(form))
        self.applyFilterPushButton.clicked.connect(lambda: self.applyFilter(form))
        self.saveFilterPushButton.clicked.connect(lambda: self.saveFilter(form))
        self.loadFilterPushButton.clicked.connect(lambda: self.loadFilter(form))
        self.clearFilterPushButton.clicked.connect(self.clearFilterLinesTextEdit)
        self.prepareGui(form)

    def prepareGui(self, form):
        self.filterLinesTextEdit.setEnabled(False)
        self.valueLineEdit.setFocus()
        self.loadColumnsToFilterComboBox(form)
        self.loadFiltersToSavedFiltersComboBox(form)

    def loadColumnsToFilterComboBox(self, form):
        for i in range (form.tableWidget.columnCount()):
           self.columnsHeadersComboBox.addItem(form.tableWidget.horizontalHeaderItem(i).text())

    def loadOperandsText(self, form):
        self.operandsComboBox.clear()
        currentText = unicode(self.columnsHeadersComboBox.currentText())
        operandsText = form.ig.operandsText[form.ig.columnsHeaders[form.ig.columnNameToIndex[currentText]]['type']]
        for i in range (len(operandsText)):
            self.operandsComboBox.addItem(operandsText[i])

    def addFilterLine(self, form):
        filterValue = unicode(self.valueLineEdit.text())
        if self.operandsComboBox.currentText() in form.ig.operandsText['Integer']:
            if (not self.isFloat(filterValue)) and (not filterValue.isdigit()):
                return
        if self.filterLinesTextEdit.toPlainText() == '':
            self.filterLinesTextEdit.setText(self.columnsHeadersComboBox.currentText() + ' [' + self.operandsComboBox.currentText() + '] ' + filterValue)
        else:
            self.filterLinesTextEdit.setText(self.filterLinesTextEdit.toPlainText() + '\n' + self.columnsHeadersComboBox.currentText() + ' [' + self.operandsComboBox.currentText() + '] ' + filterValue)

    def isFloat(self, element):
        partition=element.partition('.')
        if (partition[0].isdigit() and partition[1]=='.' and partition[2].isdigit()) or (partition[0]=='' and partition[1]=='.' and partition[2].isdigit()) or (partition[0].isdigit() and partition[1]=='.' and partition[2]==''):
            return True
        else:
            return False

    def getFilterFileName(self):
        newName = QtGui.QFileDialog.getSaveFileName(None, 'Save filter', directory=os.getcwd() + '\\Filters', filter='*.filter')
        return newName

    def saveFilter(self, form):
        filterLines = self.filterLinesTextEdit.toPlainText()
        if filterLines:
            data = {"filter":{"filterLines":[]}}
            temp = json.dumps(data)
            jsonData = loads(temp)
            filterLines = unicode(filterLines).splitlines()
            for i in range (len(filterLines)):
                jsonData['filter']['filterLines'].append(filterLines[i])
            filterFileName = self.getFilterFileName()
            if filterFileName:
                tools.writeJson(jsonData, filterFileName)
                self.loadFiltersToSavedFiltersComboBox(form)
                UIMainLayout.loadFiltersToSavedFiltersComboBox(form)

    def loadFilter(self, form):
        if self.savedFiltersComboBox.currentText():
            filterJsonFileName = os.path.join(form.ig.filtersDir, unicode(self.savedFiltersComboBox.currentText()) + '.filter')
            if os.path.isfile(filterJsonFileName):
                filterJsonData = tools.readJson(filterJsonFileName)
                self.clearFilterLinesTextEdit()
                for i in range (len(filterJsonData['filter']['filterLines'])):
                    if self.filterLinesTextEdit.toPlainText() == '':
                        self.filterLinesTextEdit.setText(unicode(filterJsonData['filter']['filterLines'][i]))
                    else:
                        self.filterLinesTextEdit.setText(self.filterLinesTextEdit.toPlainText() + '\n' + unicode(filterJsonData['filter']['filterLines'][i]))

    def loadFiltersToSavedFiltersComboBox(self, form):
        self.savedFiltersComboBox.clear()
        for file in os.listdir(form.ig.filtersDir):
            if os.path.isfile(os.path.join(form.ig.filtersDir, file)) and (file.endswith('.filter')):
                self.savedFiltersComboBox.addItem(os.path.splitext(file)[0])

    def clearFilterLinesTextEdit(self):
        self.filterLinesTextEdit.clear()

    def applyFilter(self, form):
        form.statusbar.showMessage('Applying filter...')
        UIMainLayout.tableWidgetDisableResizeToContents(form)
        tableWidgetFilters.resetFilter(form)
        tableWidgetFilters.applyFilter(form, unicode(self.filterLinesTextEdit.toPlainText()).splitlines())
        UIMainLayout.tableWidgetContentsAutoSize(form)
        form.statusbar.showMessage('Filter applied' + ' (' + str(form.ig.itemFound) + ' items found)')












