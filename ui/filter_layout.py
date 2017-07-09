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
        print "rewrklwekrlewk;l"




