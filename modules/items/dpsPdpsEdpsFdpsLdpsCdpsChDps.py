# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import calc.dpsCalc as dpsCalc


def setItemPropertiesImplicitExplicit(form, itemIndex):





	# unicodeData = unicode(self.POEWeaponDataTextEdit.toPlainText())
 #        if self.POEDPSCalc.Calc(unicodeData):
 #            self.populateData()
 #        else:
 #            self.POEWeaponDataTextEdit.setPlainText('Wrong data')
 #            self.resetData()


    #dataExplicitModifiers = []
    #dataProperties.update({'propertiesLines' : []})
    propertiesImplicitExplicitLines = ''
    #dataProperties['propertiesLines'].append({'key': '', 'keyNext': ''})
    #dataProperties['fdsfds'] = 'frdsfs'
    #print dataProperties
    #dataProperties.append([])
    a = form.tableWidget.item(0,0).text()
    print unicode(a)

    properties = form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Properties']).text()
    implicitModifiers = form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Implicit Modifiers']).text()
    explicitModifiers = form.tableWidget.item(itemIndex, form.ig.columnNameToIndex['Explicit Modifiers']).text()

    if properties and (implicitModifiers or explicitModifiers):
        properties = properties + '\n\n'
    if implicitModifiers and explicitModifiers:
        implicitModifiers = implicitModifiers + '\n\n'
    if explicitModifiers:
        explicitModifiers = explicitModifiers


    propertiesImplicitExplicitLines =  properties + implicitModifiers + explicitModifiers

    return propertiesImplicitExplicitLines
    print ""