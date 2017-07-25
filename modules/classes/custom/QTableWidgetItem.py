# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class QCustomTableWidgetItem (QtGui.QTableWidgetItem):
    def __init__ (self, value):
        super(QCustomTableWidgetItem, self).__init__(QtCore.QString('%s' % value))

    def __lt__ (self, other):
        if (isinstance(other, QCustomTableWidgetItem)):
            selfDataValue  = float(self.data(QtCore.Qt.EditRole).toString())
            otherDataValue = float(other.data(QtCore.Qt.EditRole).toString())
            return selfDataValue < otherDataValue
        else:
            return QtGui.QTableWidgetItem.__lt__(self, other)
