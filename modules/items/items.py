# -*- coding: utf-8 -*-

def cleanString(self, data, str):
        temp = data.split(str)
        print len(temp)
        return temp[len(temp)-1]

def setItemNameAndTypeLine(self, itemIndex):
        dataName = unicode(self.stashTabJson['items'][itemIndex]['name'])
        dataName = cleanString(self, dataName, '>')
        typeLine = unicode(self.stashTabJson['items'][itemIndex]['typeLine'])
        typeLine = cleanString(self, typeLine, '>')
        if dataName and typeLine:
            dataName = dataName + '\n' + typeLine
            return dataName
        else:
            dataName = dataName + typeLine
            return dataName

def setItemLocation(self, itemIndex):
    if self.stashTabJson.has_key('tabs'):
        for i in range(len(self.stashTabJson['tabs'])):
            if self.stashTabJson['tabs'][i]['selected']:
                return  unicode(self.stashTabJson['tabs'][i]['n']) + '\n(Stash Tab)'
    elif self.stashTabJson.has_key('character'):
            league = unicode(self.stashTabJson['character']['league'])
            if not league in self.ig.leagues:
                self.ig.leagues.append(league)
            return unicode(self.stashTabJson['character']['name']) + '\n(Character)'

def setItemType(self, itemIndex):
        itemType = "Unknown"
        for i in range (len(self.ig.itemTypes)):
                for j in range (len(self.ig.itemTypes[i]['items'])):
                    compareStr = self.ig.itemTypes[i]['items'][j].lower()
                    print compareStr
                    if (self.stashTabJson['items'][itemIndex]['icon'].lower().find(compareStr) >= 0) or \
                       (self.stashTabJson['items'][itemIndex]['name'].lower().find(compareStr) >= 0) or \
                       (self.stashTabJson['items'][itemIndex]['typeLine'].lower().find(compareStr) >= 0):
                       print self.ig.itemTypes[i]['typeName']
                       return self.ig.itemTypes[i]['typeName']
                    if self.stashTabJson['items'][itemIndex].has_key('properties'):
                        if self.stashTabJson['items'][itemIndex]['properties'][0]['name'].lower().find(compareStr) >= 0:
                            print self.ig.itemTypes[i]['typeName']
                            return self.ig.itemTypes[i]['typeName']
        return itemType

def setIlvl(self, itemIndex):
    return unicode(self.stashTabJson['items'][itemIndex]['ilvl'])

def setItemRarity(self, itemIndex):
    return unicode(self.ig.rarity[self.stashTabJson['items'][itemIndex]['frameType']])

def setItemQuality(self, itemIndex):
    dataQuality = ''
    if self.stashTabJson['items'][itemIndex].has_key('properties'):
        for i in range (len(self.stashTabJson['items'][itemIndex]['properties'])):
            if self.stashTabJson['items'][itemIndex]['properties'][i]['name'] == 'Quality':
                dataQuality = self.stashTabJson['items'][itemIndex]['properties'][i]['values'][0][0]
                dataQuality = dataQuality.replace('%', '')
                dataQuality = dataQuality.replace('+', '')
    return unicode(dataQuality)

def setSockets(self, itemIndex):
    return self.stashTabJson['items'][itemIndex]['frameType']

def setItemProperties(self, itemIndex):
    dataProperties = {}
    dataProperties.update({'propertiesLines' : []})
    propertiesLines = ''
    if self.stashTabJson['items'][itemIndex].has_key('properties'):
        for i in range (len(self.stashTabJson['items'][itemIndex]['properties'])):
                dataProperties['propertiesLines'].append({'name' : '', 'value' : ''})
                print dataProperties['propertiesLines'][0]
                dataProperties['propertiesLines'][i]['name'] = self.stashTabJson['items'][itemIndex]['properties'][i]['name']
                print dataProperties['propertiesLines'][i]['name']
                if dataProperties['propertiesLines'][i]['name'].find('%0') >= 0:
                    substValues = []
                    for subst in range (len(self.stashTabJson['items'][itemIndex]['properties'][i]['values'])):
                        substValues.append(unicode(self.stashTabJson['items'][itemIndex]['properties'][i]['values'][subst][0]))
                    for substIndex in range (len(substValues)):
                        dataProperties['propertiesLines'][i]['name'] = dataProperties['propertiesLines'][i]['name'].replace('%' + str(substIndex), '{' + str(substIndex) + '}')
                        print dataProperties['propertiesLines'][i]['name']
                    dataProperties['propertiesLines'][i]['name'] = dataProperties['propertiesLines'][i]['name'].format(*substValues)
                    print substValues
                    print dataProperties['propertiesLines'][i]['name']
                    dataProperties['propertiesLines'][i]['value'] = ''
                else:
                    print 'i= ' + str(i)
                    if len(self.stashTabJson['items'][itemIndex]['properties'][i]['values']) > 0:
                        dataProperties['propertiesLines'][i]['value'] = ': ' + unicode(self.stashTabJson['items'][itemIndex]['properties'][i]['values'][0][0])
                    else:
                        dataProperties['propertiesLines'][i]['value'] = ''

                if i < (len(self.stashTabJson['items'][itemIndex]['properties']) - 1):
                    propertiesLines = propertiesLines + dataProperties['propertiesLines'][i]['name'] + dataProperties['propertiesLines'][i]['value'] + '\n'
                else:
                    propertiesLines = propertiesLines + dataProperties['propertiesLines'][i]['name'] + dataProperties['propertiesLines'][i]['value']
    print dataProperties['propertiesLines']
    return propertiesLines

def setItemImplicitModifiers(self, itemIndex):
    dataImplicitModifiers = []
    implicitModifiersLines = ''
    if self.stashTabJson['items'][itemIndex].has_key('implicitMods'):
        for i in range (len(self.stashTabJson['items'][itemIndex]['implicitMods'])):
                dataImplicitModifiers.append(unicode(self.stashTabJson['items'][itemIndex]['implicitMods'][i]))
                if i < (len(self.stashTabJson['items'][itemIndex]['implicitMods']) - 1):
                    implicitModifiersLines = implicitModifiersLines + dataImplicitModifiers[i] + '\n'
                else:
                    implicitModifiersLines = implicitModifiersLines + dataImplicitModifiers[i]
    return implicitModifiersLines
    print ""

def setItemExplicitModifiers(self, itemIndex):
    dataExplicitModifiers = []
    explicitModifiersLines = ''
    if self.stashTabJson['items'][itemIndex].has_key('explicitMods'):
        for i in range (len(self.stashTabJson['items'][itemIndex]['explicitMods'])):
                dataExplicitModifiers.append(unicode(self.stashTabJson['items'][itemIndex]['explicitMods'][i]))
                if i < (len(self.stashTabJson['items'][itemIndex]['explicitMods']) - 1):
                    explicitModifiersLines = explicitModifiersLines + dataExplicitModifiers[i] + '\n'
                else:
                    explicitModifiersLines = explicitModifiersLines + dataExplicitModifiers[i]
    return explicitModifiersLines
