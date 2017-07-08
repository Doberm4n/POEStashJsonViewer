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





        # dataName = unicode(self.stashJson[0]['items'][itemIndex]['name'])
        # dataName = self.cleanString(dataName, '>')
        # typeLine = unicode(self.stashJson[0]['items'][itemIndex]['typeLine'])
        # typeLine = self.cleanString(typeLine, '>')
        # if typeLine:
        #     dataName = dataName + '\n' + typeLine
        # return dataName