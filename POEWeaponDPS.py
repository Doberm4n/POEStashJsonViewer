# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtCore import QUrl
import res.res
import sys
import re
import os
import modules.DPSCalc as DPSCalcModule
import generated.main as GUIMain
import generated.about as GUIAbout
from Tkinter import Tk
import ctypes

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

form = None
formAbout = None
version = '0.9.1'
link = '<a href="https://github.com/Doberm4n/POEWeaponDPSCalculator">GitHub</a>'

class POEWeaponDPSApp(QtGui.QMainWindow, GUIMain.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pasteButton.clicked.connect(self.pasteFromClipboard)
        self.actionAbout.triggered.connect(self.showAbout)


    def pasteFromClipboard(self):
        temp = Tk()
        try:
            clipboardData = temp.selection_get(selection = "CLIPBOARD")
            self.POEWeaponDataTextEdit.setPlainText(clipboardData)
        except:
            pass
        self.calcDPS()


    def calcDPS(self):
        self.POEDPSCalc = DPSCalcModule.DPSCalc()
        unicodeData = unicode(self.POEWeaponDataTextEdit.toPlainText())
        if self.POEDPSCalc.Calc(unicodeData):
            self.populateData()
        else:
            self.POEWeaponDataTextEdit.setPlainText('Wrong data')
            self.resetData()


    def populateData(self):
        self.pDPSLabel.setText("pDPS: " + str(self.POEDPSCalc.valuePhysical))
        self.eDPSLabel.setText("eDPS: " + str(self.POEDPSCalc.valueElemental))
        self.cDPSLabel.setText("cDPS: " + str(self.POEDPSCalc.valueChaos))
        self.fireDPSLabel.setText(str(self.POEDPSCalc.valueFire))
        self.lightningDPSLabel.setText(str(self.POEDPSCalc.valueLightning))
        self.coldDPSLabel.setText(str(self.POEDPSCalc.valueCold))
        self.totalDPSLabel.setText(str(self.POEDPSCalc.totalDPS))


    def resetData(self):
        self.pDPSLabel.setText("pDPS: 0")
        self.eDPSLabel.setText("eDPS: 0")
        self.cDPSLabel.setText("cDPS: 0")
        self.fireDPSLabel.setText("0")
        self.lightningDPSLabel.setText("0")
        self.coldDPSLabel.setText("0")
        self.totalDPSLabel.setText("0")


    def showAbout(self):
        global formAbout
        formAbout = aboutDialog()
        formAbout.show()


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
        pic.setPixmap(QtGui.QPixmap(":Device-blockdevice-cubes-icon32.png"))


    def openURL(self, linkStr):
        QDesktopServices.openUrl(QUrl(linkStr))


def main():
    app = QtGui.QApplication(sys.argv)
    appIco = QtGui.QIcon()
    appIco.addFile(':Device-blockdevice-cubes-icon16.png', QtCore.QSize(16,16))
    appIco.addFile(':Device-blockdevice-cubes-icon32.png', QtCore.QSize(32,32))
    app.setWindowIcon(appIco)
    form = POEWeaponDPSApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()




