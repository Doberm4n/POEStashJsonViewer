# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import *
import generated.form_columns_select as GUIColumnsSelect
import modules.tools as tools
import ui.main_layout as UIMainLayout


class columnsSelectDialog(QtGui.QDialog, GUIColumnsSelect.Ui_Dialog):
    def __init__(self, form):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.columnsSelectListWidget.clicked.connect(self.setCheckBox)
        self.savePushButton.clicked.connect(lambda: self.saveColumnsSelection(form))
        self.selectAllColumnsPushButton.clicked.connect(self.selectAllColumns)
        self.unselectAllColumnsPushButton.clicked.connect(self.unselectAllColumns)
        self.prepareGui(form)

    def setCheckBox(self, index):
        if self.columnsSelectListWidget.itemFromIndex(index).checkState() == Qt.Unchecked:
            self.columnsSelectListWidget.itemFromIndex(index).setCheckState(2)
        else:
            self.columnsSelectListWidget.itemFromIndex(index).setCheckState(0)

    def prepareGui(self, form):
        self.configView = form.ig.jsonConfig['view']['columns']
        self.loadColumnsToColumnsListWidget(form)

    def loadColumnsToColumnsListWidget(self, form):
        self.columnsSelectListWidget.clear()
        for i in range (len(self.configView)):
            item = QtGui.QListWidgetItem()
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setText(form.ig.columnsHeaders[i]['columnHeader'])
            if self.configView[i]['isHidden'] == False:
                item.setCheckState(2)
            else:
                item.setCheckState(0)
            self.columnsSelectListWidget.addItem(item)

    def saveColumnsSelection(self, form):
        for i in range (self.columnsSelectListWidget.count()):
            if self.columnsSelectListWidget.item(i).checkState() == Qt.Checked and form.tableWidget.isColumnHidden(i):
                form.tableWidget.showColumn(i)
                form.ig.jsonConfig['view']['columns'][i]['isHidden'] = False
            elif self.columnsSelectListWidget.item(i).checkState() == Qt.Unchecked and not form.tableWidget.isColumnHidden(i):
                form.tableWidget.hideColumn(i)
                form.ig.jsonConfig['view']['columns'][i]['isHidden'] = True
        tools.writeJson(form.ig.jsonConfig, 'Configs\config.json')
        UIMainLayout.tableWidgetContentsAutoSize(form)
        self.close()

    def selectAllColumns(self):
        for i in range (self.columnsSelectListWidget.count()):
            self.columnsSelectListWidget.item(i).setCheckState(2)

    def unselectAllColumns(self):
        for i in range (self.columnsSelectListWidget.count()):
            self.columnsSelectListWidget.item(i).setCheckState(0)








