# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
from PyQt4 import QtGui
import modules.calc.dpsCalc as dpsCalc


def setItemDpsPdpsEdpsFdpsLdpsCdpsChDps(form, itemIndex, dataPropertiesImplicitExplicit):

    dataQuality = form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Quality']).text()
    if dataQuality:
        dataQuality = 'Quality: +' + dataQuality + '\n'
    data = dataQuality + unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['PropertiesImplicitExplicit']).text())

    # unicodeData = unicode(self.POEWeaponDataTextEdit.toPlainText())
 #        if self.POEDPSCalc.Calc(unicodeData):
 #            self.populateData()
 #        else:
 #            self.POEWeaponDataTextEdit.setPlainText('Wrong data')
 #            self.resetData()
    if unicode(form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Type']).text()).find('H Weapon)') >= 0:
        _dpsCalc = dpsCalc.dpsCalc()
        if _dpsCalc.Calc(data):
            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['pDPS'], QtGui.QTableWidgetItem(str(_dpsCalc.valuePhysical)))
        # self.eDPSLabel.setText("eDPS: " + str(self.POEDPSCalc.valueElemental))
        # self.cDPSLabel.setText("cDPS: " + str(self.POEDPSCalc.valueChaos))
        # self.fireDPSLabel.setText(str(self.POEDPSCalc.valueFire))
        # self.lightningDPSLabel.setText(str(self.POEDPSCalc.valueLightning))
        # self.coldDPSLabel.setText(str(self.POEDPSCalc.valueCold))
        # self.totalDPSLabel.setText(str(self.POEDPSCalc.totalDPS))
        else:

            form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['pDPS'], QtGui.QTableWidgetItem('Wrong data'))
        #set for not None value
    else: form.tableWidget.setItem(itemIndex, form.ig.columnNameToIndex['pDPS'], QtGui.QTableWidgetItem(''))



    #dataExplicitModifiers = []
    #dataProperties.update({'propertiesLines' : []})
    # propertiesImplicitExplicitLines = ''
    # #dataProperties['propertiesLines'].append({'key': '', 'keyNext': ''})
    # #dataProperties['fdsfds'] = 'frdsfs'
    # #print dataProperties
    # #dataProperties.append([])
    # a = form.tableWidget.item(0,0).text()
    # print unicode(a)

    # properties = form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Properties']).text()
    # implicitModifiers = form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Implicit Modifiers']).text()
    # explicitModifiers = form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Explicit Modifiers']).text()

    # if properties and (implicitModifiers or explicitModifiers):
    #     properties = properties + '\n\n'
    # if implicitModifiers and explicitModifiers:
    #     implicitModifiers = implicitModifiers + '\n\n'
    # if explicitModifiers:
    #     explicitModifiers = explicitModifiers


    # propertiesImplicitExplicitLines =  properties + implicitModifiers + explicitModifiers

    # return propertiesImplicitExplicitLines
    # print ""