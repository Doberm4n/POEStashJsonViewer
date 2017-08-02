# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtCore import QUrl
from PyQt4.QtCore import QEvent
from PyQt4.QtCore import QObject
import sys
import os
from json import load
import json
import gc
import time
import res.res
import global_values
import modules.tools as tools
import modules.items.items as items
from modules.items.propertiesImplicitExplicit import setItemPropertiesImplicitExplicit
from modules.items.dpsPdpsEdpsFdpsLdpsCdpsChDps import setItemDpsPdpsEdpsFdpsLdpsCdpsChDps
from modules.items.apsCsch import setItemApsCsch
from modules.items.allResistances import setItemResistances
from modules.items.allAttributesLifeMana import setItemAttributesLifeMana
from modules.items.armEvEsChtbGcscGcsmCscfsCspSpdQty import setItemArmEvEsChtbGcscGcsmCscfsCspSpdQty
from modules.items.allRequirements import setItemRequirements
from modules.items.allSockets import setItemSockets
from modules.items.mTier import setItemMapTier
from modules.filter import resetFilter
import modules.export.exportToCsv as exportToCsv
import modules.export.exportToSingleJson as exportToSingleJson
import modules.export.exportToSQLiteDatabase as exportToSQLiteDataBase
import modules.openSingleJson as openSingleJson
from modules.classes.custom.QTableWidgetItem import QCustomTableWidgetItem as QCI
import generated.form_main as GUIMain
import generated.form_about as GUIAbout
import ui.main_layout as UIMainLayout
import ui.filter_layout as UIFilterLayout
import ui.columns_select_layout as UIColumnsSelectLayout
import ctypes
from time import time

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# form = None
# formAbout = None
# formFilter = None
version = '0.9.0_alpha(260717_2)'
link = '<a href="https://github.com/Doberm4n/POEStashJsonViewer">GitHub</a>'


class POEStashTabViewerApp(QtGui.QMainWindow, GUIMain.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.prepareGui()
        self.actionOpenJson.triggered.connect(self.browseGuide)
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionAutosizeColumns.triggered.connect(lambda: UIMainLayout.tableWidgetContentsAutoSize(self))
        self.loadConfig()
        #self.tableWidget.horizontalHeader().sortIndicatorChanged.connect(lambda: UIMainLayout.tableWidgetContentsAutoSize(self))
        self.actionEdit_filter.triggered.connect(self.showFilter)
        self.actionSelect_columns.triggered.connect(self.showColumnsSelect)
        self.actionReset_filter.triggered.connect(self.resetFilter)
        self.actionExportAllToCsv.triggered.connect(lambda: exportToCsv.exportAllToCsv(self))
        self.actionExportViewToCsv.triggered.connect(lambda: exportToCsv.exportViewToCsv(self))
        self.actionExportAllToSingleJson.triggered.connect(lambda: exportToSingleJson.exportToSingleJson(self))
        self.actionExportAllToSQLiteDatabase.triggered.connect(lambda: exportToSQLiteDataBase.exportToSQLiteDatabase(self, 'QSQLITE'))
        self.actionOpenSingleJson.triggered.connect(lambda: openSingleJson.openSingleJson(self))

    def resetFilter(self):
        resetFilter(self)
        self.savedFiltersComboBox.setCurrentIndex(0)
        UIMainLayout.tableWidgetContentsAutoSize(self)

    #close filter form when main closed
    def closeEvent(self, evnt):
        if self.formFilter:
            self.formFilter.close()

    def onQApplicationStarted(self):
        self.statusbar.showMessage('Please wait...')
        UIMainLayout.tableWidgetSetResizeMode(self)
        UIMainLayout.tableWidgetSetColumnsSelected(self)
        UIMainLayout.loadFiltersToSavedFiltersComboBox(self)
        self.statusbar.showMessage('Loaded')

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
                with open(json_file, 'w') as outfile:
                        json.dump(dump, outfile)
            except Exception, e:
                print "Error: " + str(e)

    def loadConfig(self):
        #try:
            self.ig = global_values.globalValues()
            self.formFilter = None
            self.formColumnsSelect = None
            UIMainLayout.applyLayout(self)

            if self.ig.jsonConfig['curGuide']:
                self.curGuide = self.ig.jsonConfig["curGuide"]
                self.curDir = os.path.dirname(self.curGuide)
            else:
                self.curDir = ""
                self.curGuide = ""
        #except Exception, e:
             #print "Error in loading config: " + str(e)


    def showAllColumns(self):
        for i in range (self.tableWidget.columnCount()):
            self.tableWidget.showColumn(i)

    def browseGuide(self):
        self.curJsonFiles = QtGui.QFileDialog.getOpenFileNames(self, "Select .json files", filter='*.json', directory=self.curDir)
        if self.curJsonFiles:
            self.ig.jsonConfig['curGuide'] = unicode(self.curJsonFiles[0])
            self.writeJson(self.ig.jsonConfig, 'Configs\config.json')
            l = len(self.curJsonFiles)
            if l == 1:
                self.guideLineEdit.setText(os.path.basename(unicode(self.curJsonFiles[0])))
            else:
                self.guideLineEdit.setText(str(l) + ' json files')
            UIMainLayout.tableWidgetBeforeLoad(self)
            if self.loadJson(self.curJsonFiles):
                UIMainLayout.tableWidgetAfterLoad(self)

    def prepareGui(self):

        self.tabWidget.hide()
        self.actionOpenJson.setShortcut("Ctrl+O")
        self.actionEdit_filter.setShortcut("F3")
        self.actionSelect_columns.setShortcut("F2")
        self.actionReset_filter.setShortcut("F7")
        self.actionAutosizeColumns.setShortcut("F5")

    def setItem(self, itemIndex):

            #Name ('name' + 'typeLine')
            #start = time()
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Name'], QtGui.QTableWidgetItem(items.setItemNameAndTypeLine(self, itemIndex)))
            #print 'Name ' + str(tools.printTime(start))

            #Type
            #start = time()
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Type'], QtGui.QTableWidgetItem(items.setItemType(self, itemIndex)))
            #print 'Type ' + str(tools.printTime(start))

            #Location
            #start = time()
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Location'], QtGui.QTableWidgetItem(items.setItemLocation(self, itemIndex)))
            #print 'Location ' + str(tools.printTime(start))

            #iLvl
            #start = time()
            value = items.setIlvl(self, itemIndex)
            if value:
                self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['iLvl'], QCI(value))
            #print 'iLvl ' + str(tools.printTime(start))

            #Rarity
            #start = time()
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Rarity'], QtGui.QTableWidgetItem(items.setItemRarity(self, itemIndex)))
            #print 'Rarity ' + str(tools.printTime(start))

            #Quality
            #start = time()
            value = items.setItemQuality(self, itemIndex)
            if value:
                self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Quality'], QCI(value))
            #print 'Quality ' + str(tools.printTime(start))

            #Requirements
            #start = time()
            setItemRequirements(self, itemIndex)
            #print 'Requirements ' + str(tools.printTime(start))

            #Properties
            #start = time()
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Properties'], QtGui.QTableWidgetItem(items.setItemProperties(self, itemIndex)))
            #print 'Properties ' + str(tools.printTime(start))

            #Implicit modifiers
            #start = time()
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Implicit Modifiers'], QtGui.QTableWidgetItem(items.setItemImplicitModifiers(self, itemIndex)))
            #print 'Implicit modifiers ' + str(tools.printTime(start))

            #Explicit modifiers
            #start = time()
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Explicit Modifiers'], QtGui.QTableWidgetItem(items.setItemExplicitModifiers(self, itemIndex)))
            #print 'Explicit modifiers ' + str(tools.printTime(start))

            #PropertiesImplicitExplicit
            #start = time()
            self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['PropertiesImplicitExplicit'], QtGui.QTableWidgetItem(setItemPropertiesImplicitExplicit(self, itemIndex)))
            #print 'PropertiesImplicitExplicit ' + str(tools.printTime(start))

            # Calculated columns
            if self.ig.jsonConfig['common']['calculateSpecifiedColumns']:

                #get required values
                propertiesImplicitExplicitLines = unicode(self.tableWidget.item(itemIndex, self.ig.columnNameToIndex['PropertiesImplicitExplicit']).text())
                propertiesImplicitExplicitLinesList = propertiesImplicitExplicitLines.splitlines()
                typeName = unicode(self.tableWidget.item(itemIndex, self.ig.columnNameToIndex['Type']).text())

                #dpsPdpsEdpsFdpsLdpsCdpsChDps
                #start = time()
                setItemDpsPdpsEdpsFdpsLdpsCdpsChDps(self, itemIndex, propertiesImplicitExplicitLines)
                #print 'dpsPdpsEdpsFdpsLdpsCdpsChDps ' + str(tools.printTime(start))
                #self.tableWidget.setItem(itemIndex, self.ig.columnNameToIndex['Type'], QtGui.QTableWidgetItem(items.setItemType(self, itemIndex)))

                #APS, Critical Strike Chance
                #start = time()
                setItemApsCsch(self, itemIndex, propertiesImplicitExplicitLinesList)
                #print 'APS, Critical Strike Chance ' + str(tools.printTime(start))

                #all Resistances (resTotal, resAll, resF, resL, resC, resCh), values for Fire, Lightning, Cold resistances includes value from '% to all elemental resistances' modifier
                #start = time()
                setItemResistances(self, itemIndex, propertiesImplicitExplicitLines, propertiesImplicitExplicitLinesList, typeName)
                #print 'all Resistances ' + str(tools.printTime(start))

                #all Attributes (toAttrTotal, toStr, toDex, toInt), values for Str, Dex, Int attributes includes value from 'to all Attributes' modifier
                #start = time()
                setItemAttributesLifeMana(self, itemIndex, propertiesImplicitExplicitLinesList, typeName)
                #print 'all Attributes ' + str(tools.printTime(start))

                #Armour, Evasion, Energy Shield, Chance to Block, Global Critical Strike Chance, Global Critical Strike Multiplier, Critical Strike Chance for Spells, Cast Speed, Spell Damage
                #start = time()
                setItemArmEvEsChtbGcscGcsmCscfsCspSpdQty(self, itemIndex, propertiesImplicitExplicitLinesList, typeName)
                #print 'Armour, Evasion, Energy Shield ' + str(tools.printTime(start))

                #all Sockets
                #start = time()
                setItemSockets(self, itemIndex)
                #print 'all Sockets ' + str(tools.printTime(start))

                #MapTier
                #start = time()
                setItemMapTier(self, itemIndex, propertiesImplicitExplicitLinesList, typeName)
                #print 'MapTier ' + str(tools.printTime(start))

    def loadJson(self, jsonFileNames):
        #try:
            self.ig.leagues = []
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabsStash), 'Stash')
            self.stashJson = {}
            jsonFilesCount = len(jsonFileNames)
            for jsonFiles in range(jsonFilesCount):
                self.statusbar.showMessage('Processing ' + os.path.basename(unicode(jsonFileNames[jsonFiles])))
                self.stashTabJson = self.readJson(unicode(jsonFileNames[jsonFiles]))
                if not self.stashTabJson.has_key('items'):
                    self.statusbar.showMessage('Wrong json file: ' + unicode(jsonFileNames[jsonFiles]))
                    return False
                itemsCount = len(self.stashTabJson['items'])

                #add rows, number equal to items count in json
                for itemIndex in range(itemsCount):
                    self.statusbar.showMessage('Processing ' + os.path.basename(unicode(jsonFileNames[jsonFiles])) + ' (item ' + str(itemIndex+1) + ' of ' + str(itemsCount) + ')')
                    self.tableWidget.insertRow(itemIndex)
                    self.setItem(itemIndex)
            if self.ig.leagues:
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabsStash), unicode(self.tabWidget.tabText(self.tabWidget.indexOf(self.tabsStash)) + ' ' + unicode('[%s]' % ', '.join(map(str, self.ig.leagues))) + ' '))
            self.statusbar.showMessage('Load complete')
            return True

    def showAbout(self):
        self.formAbout = aboutDialog()
        self.formAbout.show()

    def showFilter(self):
        if not self.formFilter:
            self.formFilter = UIFilterLayout.filterDialog(self)
            self.formFilter.show()
        else:
            self.formFilter.show()
            self.formFilter.activateWindow()
            self.formFilter.prepareGui(self)

    def showColumnsSelect(self):
        if not self.formColumnsSelect:
            self.formColumnsSelect = UIColumnsSelectLayout.columnsSelectDialog(self)
            self.formColumnsSelect.show()
        else:
            self.formColumnsSelect.show()
            self.formColumnsSelect.activateWindow()
            self.formColumnsSelect.prepareGui(self)


class aboutDialog(QtGui.QDialog, GUIAbout.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.linkLabel.linkActivated.connect(self.openURL)
        self.versionLabel.setText("v." + version)
        self.linkLabel.setText(link)
        pic = self.picLabel
        pic.setPixmap(QtGui.QPixmap(":database-icon32.png"))

    def openURL(self, linkStr):
        QDesktopServices.openUrl(QUrl(linkStr))


def main():
    app = QtGui.QApplication(sys.argv)
    appIco = QtGui.QIcon()
    appIco.addFile(':database-icon16.png', QtCore.QSize(16,16))
    appIco.addFile(':database-icon32.png', QtCore.QSize(32,32))
    app.setWindowIcon(appIco)
    form = POEStashTabViewerApp()
    form.showMaximized()

    #timer check for form load complete
    t = QtCore.QTimer()
    t.singleShot(0,form.onQApplicationStarted)
    app.exec_()


if __name__ == '__main__':
    main()
