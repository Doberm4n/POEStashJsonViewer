# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1092, 825)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.guideLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.guideLineEdit.setEnabled(False)
        self.guideLineEdit.setObjectName(_fromUtf8("guideLineEdit"))
        self.verticalLayout_2.addWidget(self.guideLineEdit)
        self.savedFiltersComboBox = QtGui.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        self.savedFiltersComboBox.setFont(font)
        self.savedFiltersComboBox.setObjectName(_fromUtf8("savedFiltersComboBox"))
        self.verticalLayout_2.addWidget(self.savedFiltersComboBox)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOpen = QtGui.QMenu(self.menubar)
        self.menuOpen.setObjectName(_fromUtf8("menuOpen"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuExport_to = QtGui.QMenu(self.menuTools)
        self.menuExport_to.setObjectName(_fromUtf8("menuExport_to"))
        self.menuExport_view_to = QtGui.QMenu(self.menuTools)
        self.menuExport_view_to.setObjectName(_fromUtf8("menuExport_view_to"))
        self.menuFilter = QtGui.QMenu(self.menubar)
        self.menuFilter.setObjectName(_fromUtf8("menuFilter"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenJson = QtGui.QAction(MainWindow)
        self.actionOpenJson.setObjectName(_fromUtf8("actionOpenJson"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionEdit_filter = QtGui.QAction(MainWindow)
        self.actionEdit_filter.setObjectName(_fromUtf8("actionEdit_filter"))
        self.actionSelect_columns = QtGui.QAction(MainWindow)
        self.actionSelect_columns.setObjectName(_fromUtf8("actionSelect_columns"))
        self.actionReset_filter = QtGui.QAction(MainWindow)
        self.actionReset_filter.setObjectName(_fromUtf8("actionReset_filter"))
        self.actionExportAllToCsv = QtGui.QAction(MainWindow)
        self.actionExportAllToCsv.setObjectName(_fromUtf8("actionExportAllToCsv"))
        self.actionExportAllToSingleJson = QtGui.QAction(MainWindow)
        self.actionExportAllToSingleJson.setObjectName(_fromUtf8("actionExportAllToSingleJson"))
        self.actionOpenSingleJson = QtGui.QAction(MainWindow)
        self.actionOpenSingleJson.setObjectName(_fromUtf8("actionOpenSingleJson"))
        self.actionExportViewToCsv = QtGui.QAction(MainWindow)
        self.actionExportViewToCsv.setObjectName(_fromUtf8("actionExportViewToCsv"))
        self.actionExportAllToSQLiteDatabase = QtGui.QAction(MainWindow)
        self.actionExportAllToSQLiteDatabase.setObjectName(_fromUtf8("actionExportAllToSQLiteDatabase"))
        self.actionAutosizeColumns = QtGui.QAction(MainWindow)
        self.actionAutosizeColumns.setObjectName(_fromUtf8("actionAutosizeColumns"))
        self.menuOpen.addAction(self.actionOpenJson)
        self.menuOpen.addAction(self.actionOpenSingleJson)
        self.menuHelp.addAction(self.actionAbout)
        self.menuExport_to.addAction(self.actionExportAllToCsv)
        self.menuExport_to.addAction(self.actionExportAllToSingleJson)
        self.menuExport_to.addAction(self.actionExportAllToSQLiteDatabase)
        self.menuExport_view_to.addAction(self.actionExportViewToCsv)
        self.menuTools.addAction(self.menuExport_to.menuAction())
        self.menuTools.addAction(self.menuExport_view_to.menuAction())
        self.menuFilter.addAction(self.actionEdit_filter)
        self.menuFilter.addAction(self.actionReset_filter)
        self.menuView.addAction(self.actionSelect_columns)
        self.menuView.addAction(self.actionAutosizeColumns)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Stash Json Viewer for PoE", None))
        self.menuOpen.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuExport_to.setTitle(_translate("MainWindow", "Export all to", None))
        self.menuExport_view_to.setTitle(_translate("MainWindow", "Export view to", None))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionOpenJson.setText(_translate("MainWindow", "Open json(s)", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionEdit_filter.setText(_translate("MainWindow", "Edit filter", None))
        self.actionSelect_columns.setText(_translate("MainWindow", "Select columns", None))
        self.actionReset_filter.setText(_translate("MainWindow", "Reset filter", None))
        self.actionExportAllToCsv.setText(_translate("MainWindow", "csv", None))
        self.actionExportAllToSingleJson.setText(_translate("MainWindow", "single json", None))
        self.actionOpenSingleJson.setText(_translate("MainWindow", "Open single json", None))
        self.actionExportViewToCsv.setText(_translate("MainWindow", "csv", None))
        self.actionExportAllToSQLiteDatabase.setText(_translate("MainWindow", "SQLite Database", None))
        self.actionAutosizeColumns.setText(_translate("MainWindow", "Autosize columns", None))

