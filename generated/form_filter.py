# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_filter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(497, 409)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(800, 600))
        self.filterGroupBox = QtGui.QGroupBox(Dialog)
        self.filterGroupBox.setGeometry(QtCore.QRect(5, 75, 486, 286))
        self.filterGroupBox.setObjectName(_fromUtf8("filterGroupBox"))
        self.filterLinesTextEdit = QtGui.QTextEdit(self.filterGroupBox)
        self.filterLinesTextEdit.setGeometry(QtCore.QRect(10, 50, 466, 226))
        self.filterLinesTextEdit.setObjectName(_fromUtf8("filterLinesTextEdit"))
        self.valueLineEdit = QtGui.QLineEdit(self.filterGroupBox)
        self.valueLineEdit.setGeometry(QtCore.QRect(290, 20, 121, 22))
        self.valueLineEdit.setObjectName(_fromUtf8("valueLineEdit"))
        self.operandComboBox = QtGui.QComboBox(self.filterGroupBox)
        self.operandComboBox.setGeometry(QtCore.QRect(210, 20, 69, 22))
        self.operandComboBox.setObjectName(_fromUtf8("operandComboBox"))
        self.columnsHeadersComboBox = QtGui.QComboBox(self.filterGroupBox)
        self.columnsHeadersComboBox.setGeometry(QtCore.QRect(10, 20, 191, 22))
        self.columnsHeadersComboBox.setObjectName(_fromUtf8("columnsHeadersComboBox"))
        self.addFilterStringPushButton = QtGui.QPushButton(self.filterGroupBox)
        self.addFilterStringPushButton.setGeometry(QtCore.QRect(419, 20, 56, 22))
        self.addFilterStringPushButton.setObjectName(_fromUtf8("addFilterStringPushButton"))
        self.applyFilterPushButton = QtGui.QPushButton(Dialog)
        self.applyFilterPushButton.setGeometry(QtCore.QRect(245, 375, 75, 23))
        self.applyFilterPushButton.setObjectName(_fromUtf8("applyFilterPushButton"))
        self.closePushButton = QtGui.QPushButton(Dialog)
        self.closePushButton.setGeometry(QtCore.QRect(415, 375, 75, 23))
        self.closePushButton.setObjectName(_fromUtf8("closePushButton"))
        self.savedFiltersGroupBox = QtGui.QGroupBox(Dialog)
        self.savedFiltersGroupBox.setGeometry(QtCore.QRect(5, 10, 486, 56))
        self.savedFiltersGroupBox.setObjectName(_fromUtf8("savedFiltersGroupBox"))
        self.savedFiltersComboBox = QtGui.QComboBox(self.savedFiltersGroupBox)
        self.savedFiltersComboBox.setGeometry(QtCore.QRect(10, 20, 376, 22))
        self.savedFiltersComboBox.setObjectName(_fromUtf8("savedFiltersComboBox"))
        self.loadFilterPushButton = QtGui.QPushButton(self.savedFiltersGroupBox)
        self.loadFilterPushButton.setGeometry(QtCore.QRect(400, 20, 75, 23))
        self.loadFilterPushButton.setObjectName(_fromUtf8("loadFilterPushButton"))
        self.saveFilterPushButton = QtGui.QPushButton(Dialog)
        self.saveFilterPushButton.setGeometry(QtCore.QRect(330, 375, 75, 23))
        self.saveFilterPushButton.setObjectName(_fromUtf8("saveFilterPushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About", None))
        self.filterGroupBox.setTitle(_translate("Dialog", "Edit filters", None))
        self.addFilterStringPushButton.setText(_translate("Dialog", "Add", None))
        self.applyFilterPushButton.setText(_translate("Dialog", "Apply filter", None))
        self.closePushButton.setText(_translate("Dialog", "Close", None))
        self.savedFiltersGroupBox.setTitle(_translate("Dialog", "Filters", None))
        self.loadFilterPushButton.setText(_translate("Dialog", "Load filter", None))
        self.saveFilterPushButton.setText(_translate("Dialog", "Save", None))

