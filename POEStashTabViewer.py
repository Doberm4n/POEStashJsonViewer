# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtCore import QUrl
from PyQt4.QtCore import QEvent
from PyQt4.QtCore import QObject
#import res.res
import sys
import re
import os
from json import load
from json import loads
import json
import gc
import time
import res.res
import global_values
import modules.items as items
#import modules.DPSCalc as DPSCalcModule
import generated.form_main as GUIMain
import generated.form_about as GUIAbout
import ui.main_layout as UIMainLayout
import ui.filter_layout as UIFilterLayout
#import generated.about as GUIAbout
from Tkinter import Tk
import ctypes
import export


myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

form = None
formAbout = None
formFilter = None
version = '0.9.0'
link = '<a href="https://github.com/Doberm4n/PoEStashTabViewer">GitHub</a>'


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class POEStashTabViewerApp(QtGui.QMainWindow, GUIMain.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.prepareGui()

        self.openGuidePushButton.clicked.connect(self.browseGuide)
        self.actionReset_All.triggered.connect(self.menuActionResetAll)
        self.actionComplete_All.triggered.connect(self.menuActionCompleteAll)
        self.menuActionOpen.triggered.connect(self.browseGuide)
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionCreate_empty_guide_file.triggered.connect(lambda: export.createGuideAndImportText(self))

        self.pushButton.clicked.connect(self.tableWidgetContentsAutoSize)



        self.loadConfig()

        self.tableWidget.horizontalHeader().sortIndicatorChanged.connect(self.tableWidgetContentsAutoSize)

        self.actionEdit_filter.triggered.connect(self.showFilter)

    #close filter form when main closed
    def closeEvent(self, evnt):
        if self.formFilter:
            self.formFilter.close()

    def onQApplicationStarted(self):
        #self.tableWidget.setVisible(False)
        # vporig = QtCore.QRect
        # vporig = self.tableWidget.viewport().geometry()
        # vpnew = QtCore.QRect
        # vpnew = vporig
        # #vpnew.setWidth(std::numeric_limits<int>::max());
        # vpnew.setWidth(1);
        # self.tableWidget.viewport().setGeometry(vpnew);
        # #self.tableWidget.resizeColumnsToContents();
        # self.tableWidget.resizeRowsToContents();
        # self.tableWidget.viewport().setGeometry(vporig);
        #self.setWindowState(QtCore.Qt.WindowMaximized)

        self.tableWidgetSetResizeMode()
        #self.setFixedColumnsWidth()

        print ""
        #self.tableWidget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)
        #self.tableWidgetContentsAutoSize()
        # self.tableWidget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        # self.tableWidget.verticalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setResizeMode(7, QtGui.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setResizeMode(8, QtGui.QHeaderView.ResizeToContents)
        #self.tableWidget.setVisible(True)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(1000)
        # sizePolicy.setVerticalStretch(1000)
        #sizePolicy.setHeightForWidth(True)
        #self.setSizePolicy(sizePolicy)
        #self.setWindowState(QtCore.Qt.WindowMaximized)


    def setFixedColumnsWidth(self):
        for i in range (self.tableWidget.columnCount()):
            # if self.ig.columnsHeaders[i]['columnHeader'] == 'iLvl' or \
            # self.ig.columnsHeaders[i]['columnHeader'] == 'Rarity':
            self.tableWidget.setColumnWidth(i, 125)
            #      self.tableWidget.item(0,2).setTextAlignment(QtCore.Qt.AlignCenter)
            #      continue


        #     self.tableWidget.horizontalHeader().setResizeMode(i, QtGui.QHeaderView.ResizeToContents)
        # for j in range (self.tableWidget.rowCount()):
        # #print ""
        #     self.tableWidget.verticalHeader().setResizeMode(j, QtGui.QHeaderView.ResizeToContents)
        # print ""

    def tableWidgetSetResizeMode(self):

        for i in range (self.tableWidget.columnCount()):
            # if self.ig.columnsHeaders[i]['columnHeader'] == 'iLvl' or \
            # self.ig.columnsHeaders[i]['columnHeader'] == 'Rarity':
            #      self.tableWidget.setColumnWidth(i, 27)
            #      self.tableWidget.item(0,2).setTextAlignment(QtCore.Qt.AlignCenter)
            #      continue
            print unicode(self.tableWidget.item(0,0).text())

            self.tableWidget.horizontalHeader().setResizeMode(i, QtGui.QHeaderView.ResizeToContents)
        for j in range (self.tableWidget.rowCount()):
        #print ""
            self.tableWidget.verticalHeader().setResizeMode(j, QtGui.QHeaderView.ResizeToContents)

        #self.tableWidget.horizontalHeader().setDefaultSectionSize(20)



    def tableWidgetContentsAutoSize(self):
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        #self.formFilter.applyFilter(self, ['Name [contains] test'])
        #self.tableWidget.setColumnWidth(2, 27)
        print ""

    def buttonsTextClick(self, tab, index):
        #print str(tab) + " " + str(index)
        if self.buttonsText[tab, index].isEnabled():
            self.buttonsText[tab, index].setEnabled(False)
            guideJson = self.readJson(self.curGuide)
            guideJson['guide']['tabs'][tab]['text'][index]['isCompleted'] = True
            self.writeJson(guideJson, self.curGuide)

    def buttonsCompleteClick(self, tab, index):
        #print str(tab) + " " + str(index)
        if not self.buttonsText[tab, index].isEnabled():
            self.buttonsText[tab, index].setEnabled(True)
            self.buttonsText[tab, index].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)
            guideJson = self.readJson(self.curGuide)
            guideJson['guide']['tabs'][tab]['text'][index]['isCompleted'] = False
            self.writeJson(guideJson, self.curGuide)

    def menuActionResetClick(self, tab, count):
        guideJson = self.readJson(self.curGuide)
        if self.dialogYesNo('Reset', 'Reset ' + guideJson['guide']['tabs'][tab]['name'] + '\n\nAre you sure?'):
            #print str(tab) + str(count)
            for i in range (count + 1):
                if not self.buttonsText[tab, i].isEnabled():
                    self.buttonsText[tab, i].setEnabled(True)
                    self.buttonsText[tab, i].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)
                    guideJson['guide']['tabs'][tab]['text'][i]['isCompleted'] = False
            self.writeJson(guideJson, self.curGuide)

    def menuActionResetAll(self):
        if self.dialogYesNo('Reset all', "Reset all\n\nAre you sure?"):
            guideJson = self.readJson(self.curGuide)
            for tabs in range (self.tabWidget.count()):
                    for widget in self.groupBoxes[tabs].children():
                        if isinstance(widget, QtGui.QPushButton):
                            if "guideStringPushButton_" in widget.objectName():
                                if not widget.isEnabled():
                                    widget.setEnabled(True)
                            #print "linedit: %s  - %s" %(widget.objectName(),widget.text())
                    for i in range (len(guideJson['guide']['tabs'][tabs]['text'])):
                        if guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted']:
                            guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted'] = False
            self.writeJson(guideJson, self.curGuide)

    def menuActionCompleteClick(self, tab, count):
        guideJson = self.readJson(self.curGuide)
        if self.dialogYesNo('Complete', 'Complete ' + guideJson['guide']['tabs'][tab]['name'] + '\n\nAre you sure?'):
            #print str(tab) + str(count)
            for i in range (count + 1):
                if  self.buttonsText[tab, i].isEnabled():
                    self.buttonsText[tab, i].setEnabled(False)
                    self.buttonsText[tab, i].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)
                    guideJson['guide']['tabs'][tab]['text'][i]['isCompleted'] = True
            self.writeJson(guideJson, self.curGuide)

    def menuActionCompleteAll(self):
        if self.dialogYesNo('Complete all', "Complete all\n\nAre you sure?"):
            #print "curGuide: " + self.curGuide
            guideJson = self.readJson(self.curGuide)
            for tabs in range (self.tabWidget.count()):
                    for widget in self.groupBoxes[tabs].children():
                        if isinstance(widget, QtGui.QPushButton):
                            if "guideStringPushButton_" in widget.objectName():
                                if  widget.isEnabled():
                                    widget.setEnabled(False)
                            #print "linedit: %s  - %s" %(widget.objectName(),widget.text())
                    for i in range (len(guideJson['guide']['tabs'][tabs]['text'])):
                        if not guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted']:
                            guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted'] = True
            self.writeJson(guideJson, self.curGuide)

    def dialogYesNo(self, title, question):
        result = QtGui.QMessageBox.question(self, title, question, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            return True
        else:
            return False

    def readJson(self, json_file):
        if json_file:
            try:
                with open(json_file) as data_file:
                    return load(data_file)
            except Exception, e:
                 print "Error: " + str(e)

    def writeJson(self, dump, json_file):
        if json_file:
            try:
                #print ""
                with open(json_file, 'w') as outfile:
                        json.dump(dump, outfile)
            except Exception, e:
                 print "Error: " + str(e)

    def loadConfig(self):
        #try:
            self.ig = global_values.globalValues()
            UIMainLayout.applyLayout(self)

            self.formFilter = UIFilterLayout.filterDialog(self)

            guideJson = self.readJson('Configs\config.json')
            if guideJson['curGuide']:
                #print "Yes"
                self.curGuide = guideJson["curGuide"]
                curGuideFilename = os.path.basename(self.curGuide)
                self.guideLineEdit.setText(curGuideFilename)
                self.curDir = os.path.dirname(self.curGuide)
                self.loadGuide(self.curGuide)
                # self.tabWidget.update()
                # self.tableWidget.resizeColumnsToContents()
                # self.tableWidget.resizeRowsToContents()
                # self.tabWidget.update()
            else:
                self.curDir = ""
                self.curGuide = ""
                #print "No"
        #except Exception, e:
             #print "Error in loading config: " + str(e)

    def browseGuide(self):
        self.curGuide = str(QtGui.QFileDialog.getOpenFileName(self, "Select guide", filter='*.json', directory=self.curDir))
        if self.curGuide:
            guideJson = self.readJson('Configs\config.json')
            guideJson['curGuide'] = self.curGuide
            self.writeJson(guideJson, 'Configs\config.json')
            self.guideLineEdit.setText(os.path.basename(self.curGuide))
            #self.clearGuide()
            self.loadGuide(self.curGuide)

    def prepareGui(self):

        self.tabWidget.hide()
        self.completedStylesheet = "QPushButton:!enabled {font-family: Verdana; font-size: 8pt; color: green; text-align: left;  padding: 5;}"
        self.uncompletedStylesheet = "QPushButton:enabled {font-family: Verdana; font-size: 8pt; text-align: left; border: 1px solid grey; background-color: white; padding: 5; font-weight: 1bold } QPushButton:hover {background-color: rgb(187, 255, 177);}"
        self.disabledtabsylesheet = ""
        self.actionsReset = [self.actionAct_1, self.actionAct_2, self.actionAct_3, self.actionAct_4, self.actionAct_5, self.actionAct_6, self.actionAct_7, self.actionAct_8, self.actionAct_9, self.actionAct_10, self.actionReset_All]
        self.menuActionResets = {}
        self.menuActionProgress = {}
        self.windowTitle = 'PoE Leveling Guide'
        self.tabWidget.setStyleSheet(self.disabledtabsylesheet)

        self.actionEdit_filter.setShortcut("F3")

    # def clearButtons(self):
    #     for tabs in range (10):
    #             for widget in self.groupBoxes_original[tabs].children():
    #                 if isinstance(widget, QtGui.QPushButton):
    #                     widget.deleteLater()

    def clearTabs(self):
        tabs_count = self.tabWidget.count()
        #print "tabs_count = " + str(tabs_count)
        for i in range (tabs_count -1, -1, -1):
            self.tabWidget.widget(i).close()
            self.tabWidget.widget(i).deleteLater()
            self.tabWidget.removeTab(i)
        gc.collect()

    def clearMenuActionReset(self):
        if self.menuActionResets:
            #print "self.menuReset_progress.widget.count()"
            for value in self.menuActionResets.values():
                self.menuReset_progress.removeAction(value)
            self.menuActionResets = {}

    def clearMenuActionProgress(self):
        if self.menuActionProgress:
            #print "self.menuReset_progress.widget.count()"
            for value in self.menuActionProgress.values():
                self.menuComplete_progress.removeAction(value)
            self.menuActionProgress = {}

    def eventFilter(self, obj, event):
        if obj and not obj.isEnabled() and event.type() == QEvent.Wheel:
            newEvent = QtGui.QWheelEvent(obj.mapToParent(event.pos()), event.globalPos(),
                                   event.delta(), event.buttons(),
                                   event.modifiers(), event.orientation())
            QtGui.QApplication.instance().postEvent(obj.parent(), newEvent)
            return True
        return QObject.eventFilter(self, obj, event)


    def setItem(self, itemIndex):
        #if self.ig.columnsHeaders[columnHeader]:
            #print self.ig.columnsHeaders[columnHeader].values()[1]
            #self.setNameAndTypeLine(itemIndex)
            #print dataName[6]
            #result = self.processData()
            #data = "Tempest Stinger•fwwrweMjölner"
            #data = data.decode('utf-8')
            #data = unicode(data)

            #Name ('name' + 'typeLine')
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Name'], QtGui.QTableWidgetItem(items.setItemNameAndTypeLine(self, itemIndex)))

            #Type
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Type'], QtGui.QTableWidgetItem(items.setItemType(self, itemIndex)))

            #iLvl
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['iLvl'], QtGui.QTableWidgetItem(items.setIlvl(self, itemIndex)))

            #Rarity
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Rarity'], QtGui.QTableWidgetItem(items.setItemRarity(self, itemIndex)))

            #Quality
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Quality'], QtGui.QTableWidgetItem(items.setItemQuality(self, itemIndex)))

            #Properties
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Properties'], QtGui.QTableWidgetItem(items.setItemProperties(self, itemIndex)))

            #Implicit modifiers
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Implicit Modifiers'], QtGui.QTableWidgetItem(items.setItemImplicitModifiers(self, itemIndex)))

            #Type
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Explicit Modifiers'], QtGui.QTableWidgetItem(items.setItemExplicitModifiers(self, itemIndex)))

            #Properties
            #self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['iLvl'], QtGui.QTableWidgetItem(items.setItemProperties(self, itemIndex)))


            #print data
            #return data




    def processData(self, data):
        print ""

    def loadGuide(self, guide):
        #try:
            self.stashJson = {}
            characterJson = {}

            self.stashTabJson = self.readJson(guide)

            #for stashTabs in range (len(self.stashTabJson)):

                #self.stashJson[1000000000] = self.readJson(guide)
            text = []

                ######################################################## self.clearTabs()
                ######################################################## self.clearMenuActionReset()
                ######################################################## self.clearMenuActionProgress()

            #self.tableWidget.setVisible(False)

                #add defined columns
            textLength = len(self.stashTabJson['items'])
            # for columns in range (len(self.ig.columnsHeaders)):
            #     self.tableWidget.insertColumn(columns)
            for i in range (11):
            #add rows, number equal to items count in json
                for rows in range (textLength):
                    self.tableWidget.insertRow(rows)
                    self.setItem(rows)
                #for columns in range (len(self.ig.columnsHeaders)):
                    #fill rows with data
                    #print rows, columns, item
                    #self.tableWidget.setItem(rows, columns, QtGui.QTableWidgetItem(item))
            #self.tableWidget.repaint()
            # self.tabWidget.update()
            # self.tableWidget.resizeColumnsToContents()
            # self.tableWidget.resizeRowsToContents()




            #self.tableWidget.setColumnHidden()
            #self.tableWidget.setRowHidden(1, True)
            #self.tableWidgetContentsAutoSize()





            # if (not self.firstTab) and (textLength > 0):
            #       self.tabWidget.setCurrentIndex(tabs)
            #       self.firstTab = True
            # if textLength > 0:
            #     self.menuActionResets[tabs] = QtGui.QAction(self)
            #     self.menuActionResets[tabs].setObjectName(_fromUtf8("actionReset_" + str(tabs)))
            #     self.menuReset_progress.addAction(self.menuActionResets[tabs])
            #     self.menuActionResets[tabs].setText(_translate("MainWindow", "Reset " + guideJson['guide']['tabs'][tabs]['name'], None))
            #     self.menuActionProgress[tabs] = QtGui.QAction(self)
            #     self.menuActionProgress[tabs].setObjectName(_fromUtf8("actionProgress_" + str(tabs)))
            #     self.menuComplete_progress.addAction(self.menuActionProgress[tabs])
            #     self.menuActionProgress[tabs].setText(_translate("MainWindow", "Complete " + guideJson['guide']['tabs'][tabs]['name'], None))
            i = 0
            #################if textLength == 0:
                #print "Length = 0"
                #############################self.tabWidget.setTabEnabled(tabs, False)
                #self.tabWidget.widget(0).hide()
                #tabs_count = self.tabWidget.count()
                #print "tabs_count = " + str(tabs_count)
            #print "Length " + str(tabs) + " " + str(textLength)



            # for i in range (textLength):
            #     self.buttonsText[tabs, i] = QtGui.QPushButton(self.groupBoxes[tabs])
            #     self.buttonsComplete[tabs, i] = QtGui.QPushButton(self.groupBoxes[tabs])
            #     self.buttonsText[tabs, i].setObjectName(_fromUtf8("guideStringPushButton_" + str(i)))
            #     self.buttonsComplete[tabs, i].setObjectName(_fromUtf8("resetPushButton_" + str(i)))
            #     self.buttonsText[tabs, i].setText(_translate("MainWindow", "guideStringPushButton", None))
            #     self.buttonsComplete[tabs, i].setText(_translate("MainWindow", "resetPushButton", None))
            #     self.buttonsText[tabs, i].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)
            #     self.gridLayouts[tabs].addWidget(self.buttonsText[tabs, i], i, 0, 1, 1)
            #     self.gridLayouts[tabs].addWidget(self.buttonsComplete[tabs, i], i, 1, 1, 1)
            #     tempString = guideJson['guide']['tabs'][tabs]['text'][i]['string']
            #     if  tempString.find(u'\u25e6') >= 0:
            #         tempString = "     " + tempString
            #     self.buttonsText[tabs, i].setText(tempString)
            #     self.buttonsText[tabs, i].setEnabled(not guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted'])
            #     self.buttonsText[tabs, i].installEventFilter(self)
            #     self.buttonsComplete[tabs, i].setText("Reset")
            #     self.buttonsText[tabs, i].clicked.connect(lambda clicked, tabs=tabs, i=i: self.buttonsTextClick(tabs, i))
            #     self.buttonsComplete[tabs, i].clicked.connect(lambda clicked, tabs=tabs, i=i: self.buttonsCompleteClick(tabs, i))

            # if textLength > 0:
            #     if self.menuActionResets[tabs].triggered:
            #         self.menuActionResets[tabs].triggered.disconnect()
            #     self.menuActionResets[tabs].triggered.connect(lambda clicked, tabs=tabs, i=i: self.menuActionResetClick(tabs, i))

            #     if self.menuActionProgress[tabs].triggered:
            #         self.menuActionProgress[tabs].triggered.disconnect()
            #     self.menuActionProgress[tabs].triggered.connect(lambda clicked, tabs=tabs, i=i: self.menuActionCompleteClick(tabs, i))
            # if not self.firstTab:
            #     self.tabWidget.hide()
            # self.setWindowTitle(self.windowTitle + " - " + os.path.basename(guide) + ' (' + os.path.dirname(guide) + ')')
            # guideInfo = guideJson['common']['info']
            # self.guideLineEdit.setText(guideInfo['name'] + "" + guideInfo['version'] + "(" + guideInfo['date'] + " " + guideInfo['time'] + ")" + guideInfo['author'] + "" + guideInfo['notes'] + "")
            # self.statusbar.clearMessage()
        # except Exception, e:
        #     self.tabWidget.hide()
        #     self.statusbar.showMessage("Error in loading guide: " + str(e))

    def showAbout(self):
        #global formAbout
        self.formAbout = aboutDialog()
        self.formAbout.show()

    def showFilter(self):
        #global formFilter

        self.formFilter.show()


class aboutDialog(QtGui.QDialog, GUIAbout.Ui_Dialog):
    def __init__(self):
        global version
        global link
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.linkLabel.linkActivated.connect(self.openURL)
        self.versionLabel.setText("v." + version)
        self.linkLabel.setText(link)
        pic = self.picLabel
        pic.setPixmap(QtGui.QPixmap(":todo-icon32.png"))

    def openURL(self, linkStr):
        QDesktopServices.openUrl(QUrl(linkStr))


def main():
    app = QtGui.QApplication(sys.argv)
    appIco = QtGui.QIcon()
    appIco.addFile(':todo-icon16.png', QtCore.QSize(16,16))
    appIco.addFile(':todo-icon32.png', QtCore.QSize(32,32))
    app.setWindowIcon(appIco)
    form = POEStashTabViewerApp()
    form.showMaximized()
    #form.setWindowState(QtCore.Qt.WindowMaximized)
    #timer check for autosize tableWidget rows and columns to contents when form load complete
    t = QtCore.QTimer()
    t.singleShot(0,form.onQApplicationStarted)
    app.exec_()


if __name__ == '__main__':
    main()




