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

def setItemType(self, itemIndex):
        itemType = "Unknown"
        for i in range (len(self.ig.itemTypes)):
            #if itemType is not 'Unknown':
                for j in range (len(self.ig.itemTypes[i]['items'])):
                    compareStr = self.ig.itemTypes[i]['items'][j].lower()
                    print compareStr
                    #stashTabJsonItem =
                    if (self.stashTabJson['items'][itemIndex]['icon'].lower().find(compareStr) >= 0) or \
                       (self.stashTabJson['items'][itemIndex]['name'].lower().find(compareStr) >= 0) or \
                       (self.stashTabJson['items'][itemIndex]['typeLine'].lower().find(compareStr) >= 0):
                       print self.ig.itemTypes[i]['typeName']
                       #return
                       return self.ig.itemTypes[i]['typeName']
                       #break
                    if self.stashTabJson['items'][itemIndex].has_key('properties'):
                        if self.stashTabJson['items'][itemIndex]['properties'][0]['name'].lower().find(compareStr) >= 0:
                            print self.ig.itemTypes[i]['typeName']
                            #return
                            return self.ig.itemTypes[i]['typeName']
                            #break
        #print self.ig.itemTypes[i]['typeName']
        #return
        return itemType

def setIlvl(self, itemIndex):
    return unicode(self.stashTabJson['items'][itemIndex]['ilvl'])
    #print ""

def setItemRarity(self, itemIndex):
    return unicode(self.ig.rarity[self.stashTabJson['items'][itemIndex]['frameType']])
    #print ""

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
    print ""

def setItemProperties(self, itemIndex):
    dataProperties = {}
    dataProperties.update({'propertiesLines' : []})
    propertiesLines = ''
    #dataProperties['propertiesLines'].append({'key': '', 'keyNext': ''})
    #dataProperties['fdsfds'] = 'frdsfs'
    #print dataProperties
    #dataProperties.append([])
    if self.stashTabJson['items'][itemIndex].has_key('properties'):
        for i in range (len(self.stashTabJson['items'][itemIndex]['properties'])):
            #for j in range (len(self.stashTabJson['items'][itemIndex]['properties'][i]['values'])):

                dataProperties['propertiesLines'].append({'name' : '', 'value' : ''})
                print dataProperties['propertiesLines'][0]
                #dataProperties[i]['name'] = " "
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
    #             if self.stashTabJson['items'][itemIndex]['properties'][i]['name'] == 'Quality':
    #                 dataQuality = self.stashTabJson['items'][itemIndex]['properties'][i]['values'][0][0]
    #                 dataQuality = dataQuality.replace('%', '')
    #                 dataQuality = dataQuality.replace('+', '')
    return propertiesLines
    #print ""

def setItemImplicitModifiers(self, itemIndex):
    dataImplicitModifiers = []
    #dataProperties.update({'propertiesLines' : []})
    implicitModifiersLines = ''
    #dataProperties['propertiesLines'].append({'key': '', 'keyNext': ''})
    #dataProperties['fdsfds'] = 'frdsfs'
    #print dataProperties
    #dataProperties.append([])
    if self.stashTabJson['items'][itemIndex].has_key('implicitMods'):
        for i in range (len(self.stashTabJson['items'][itemIndex]['implicitMods'])):
            #for j in range (len(self.stashTabJson['items'][itemIndex]['properties'][i]['values'])):

                dataImplicitModifiers.append(unicode(self.stashTabJson['items'][itemIndex]['implicitMods'][i]))


                if i < (len(self.stashTabJson['items'][itemIndex]['implicitMods']) - 1):
                    implicitModifiersLines = implicitModifiersLines + dataImplicitModifiers[i] + '\n'
                else:
                    implicitModifiersLines = implicitModifiersLines + dataImplicitModifiers[i]
    #print dataProperties['propertiesLines']
    #             if self.stashTabJson['items'][itemIndex]['properties'][i]['name'] == 'Quality':
    #                 dataQuality = self.stashTabJson['items'][itemIndex]['properties'][i]['values'][0][0]
    #                 dataQuality = dataQuality.replace('%', '')
    #                 dataQuality = dataQuality.replace('+', '')
    #return propertiesLines
    return implicitModifiersLines
    print ""

def setItemExplicitModifiers(self, itemIndex):
    dataExplicitModifiers = []
    #dataProperties.update({'propertiesLines' : []})
    explicitModifiersLines = ''
    #dataProperties['propertiesLines'].append({'key': '', 'keyNext': ''})
    #dataProperties['fdsfds'] = 'frdsfs'
    #print dataProperties
    #dataProperties.append([])
    if self.stashTabJson['items'][itemIndex].has_key('explicitMods'):
        for i in range (len(self.stashTabJson['items'][itemIndex]['explicitMods'])):
            #for j in range (len(self.stashTabJson['items'][itemIndex]['properties'][i]['values'])):

                dataExplicitModifiers.append(unicode(self.stashTabJson['items'][itemIndex]['explicitMods'][i]))


                if i < (len(self.stashTabJson['items'][itemIndex]['explicitMods']) - 1):
                    explicitModifiersLines = explicitModifiersLines + dataExplicitModifiers[i] + '\n'
                else:
                    explicitModifiersLines = explicitModifiersLines + dataExplicitModifiers[i]
    #print dataProperties['propertiesLines']
    #             if self.stashTabJson['items'][itemIndex]['properties'][i]['name'] == 'Quality':
    #                 dataQuality = self.stashTabJson['items'][itemIndex]['properties'][i]['values'][0][0]
    #                 dataQuality = dataQuality.replace('%', '')
    #                 dataQuality = dataQuality.replace('+', '')
    #return propertiesLines
    #return implicitModifiersLines
    #print ""
    return explicitModifiersLines
    print ""




        # dataName = unicode(self.stashJson[0]['items'][itemIndex]['name'])
        # dataName = self.cleanString(dataName, '>')
        # typeLine = unicode(self.stashJson[0]['items'][itemIndex]['typeLine'])
        # typeLine = self.cleanString(typeLine, '>')
        # if typeLine:
        #     dataName = dataName + '\n' + typeLine
        # return dataName