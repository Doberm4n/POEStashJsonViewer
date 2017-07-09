# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PyQt4 import QtGui
from PyQt4 import QtCore
import generated.form_filter as GUIFilter

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
        self.applyFilterPushButton.clicked.connect(lambda: self.applyFilter(form, unicode(self.filterLinesTextEdit.toPlainText()).splitlines()))

        self.prepareGui(form)




        #print form.tableWidget.horizontalHeaderItem(0).text()
        #print unicode(form.tableWidget.item(0, 0).text())

    def prepareGui(self, form):
        self.loadColumnsToFilterComboBox(form)

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
        print self.filterLinesTextEdit.toPlainText()
        if self.filterLinesTextEdit.toPlainText() == '':
            self.filterLinesTextEdit.setText(self.columnsHeadersComboBox.currentText() + ' [' + self.operandsComboBox.currentText() + '] ' + self.valueLineEdit.text())
        else:
            self.filterLinesTextEdit.setText(self.filterLinesTextEdit.toPlainText() + '\n' + self.columnsHeadersComboBox.currentText() + ' [' + self.operandsComboBox.currentText() + '] ' + self.valueLineEdit.text())
        print "rewrklwekrlewk;l"

    def applyFilter(self, form, filterLines):
        print filterLines
        if filterLines != '':
            self.filters = {}
            self.filters.update({'filters' : []})

            #self.filterLines = filterLines
            print 'Length: ' + str(len(filterLines))
            for i in range (len(filterLines)):
                self.filters['filters'].append({'columnHeader' : None, 'operand' : None, 'filterValue' : None, 'filterType' : None})

                temp = filterLines[i].split(' [')
                self.filters['filters'][i]['columnHeader'] = temp[0]
                self.filters['filters'][i]['operand'] = temp[1].split('] ')[0]

                if (self.filters['filters'][i]['operand'].find('contains') >= 0) or (self.filters['filters'][i]['operand'].find('match') >=0):
                    filterLines[i] =filterLines[i].replace('[match]', '[=]')
                    self.filters['filters'][i]['filterType'] = 'String'
                else:
                    self.filters['filters'][i]['filterType'] = 'Integer'

                self.filters['filters'][i]['filterValue'] = temp[1].split('] ')[1]

            print self.filters['filters']








