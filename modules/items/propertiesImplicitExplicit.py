# -*- coding: utf-8 -*-

def setItemPropertiesImplicitExplicit(form, itemIndex):
    propertiesImplicitExplicitLines = ''
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
