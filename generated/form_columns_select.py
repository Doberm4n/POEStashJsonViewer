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
        Dialog.setMinimumSize(QtCore.QSize(370, 167))
        Dialog.setMaximumSize(QtCore.QSize(1370, 1167))
        self.columnsListWidget = QtGui.QListWidget(Dialog)
        self.columnsListWidget.setGeometry(QtCore.QRect(10, 10, 451, 446))
        self.columnsListWidget.setViewMode(QtGui.QListView.ListMode)
        self.columnsListWidget.setObjectName(_fromUtf8("columnsListWidget"))
        self.savePushButton = QtGui.QPushButton(Dialog)
        self.savePushButton.setGeometry(QtCore.QRect(385, 465, 75, 23))
        self.savePushButton.setObjectName(_fromUtf8("savePushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About", None))
        self.savePushButton.setText(_translate("Dialog", "Ok", None))

