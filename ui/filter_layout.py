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
        form.tableWidget.setVisible(False)
        #print form.tableWidget.columnsCount()
        #self.linkLabel.linkActivated.connect(self.openURL)
        #self.versionLabel.setText("v." + version)
        #self.linkLabel.setText(link)
        #pic = self.picLabel
        #pic.setPixmap(QtGui.QPixmap(":todo-icon32.png"))