# -*- coding: utf-8 -*-
#from PyQt4 import QtGui

def setItemPropertiesImplicitExplicit(form, itemIndex):
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