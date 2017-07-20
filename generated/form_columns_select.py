# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_columns_select.ui'
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
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(473, 498)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(473, 498))
        Dialog.setMaximumSize(QtCore.QSize(473, 498))
        self.columnsSelectListWidget = QtGui.QListWidget(Dialog)
        self.columnsSelectListWidget.setGeometry(QtCore.QRect(10, 10, 451, 446))
        self.columnsSelectListWidget.setViewMode(QtGui.QListView.ListMode)
        self.columnsSelectListWidget.setObjectName(_fromUtf8("columnsSelectListWidget"))
        self.savePushButton = QtGui.QPushButton(Dialog)
        self.savePushButton.setGeometry(QtCore.QRect(385, 465, 75, 23))
        self.savePushButton.setObjectName(_fromUtf8("savePushButton"))
        self.selectAllColumnsPushButton = QtGui.QPushButton(Dialog)
        self.selectAllColumnsPushButton.setGeometry(QtCore.QRect(10, 465, 75, 23))
        self.selectAllColumnsPushButton.setObjectName(_fromUtf8("selectAllColumnsPushButton"))
        self.unselectAllColumnsPushButton = QtGui.QPushButton(Dialog)
        self.unselectAllColumnsPushButton.setGeometry(QtCore.QRect(90, 465, 75, 23))
        self.unselectAllColumnsPushButton.setObjectName(_fromUtf8("unselectAllColumnsPushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Columns select", None))
        self.savePushButton.setText(_translate("Dialog", "Ok", None))
        self.selectAllColumnsPushButton.setText(_translate("Dialog", "Select all", None))
        self.unselectAllColumnsPushButton.setText(_translate("Dialog", "Unselect all", None))

