# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
sys.path.insert(0,os.path.dirname(parentdir))
import modules.tools as tools
import sqlite3
#from time import time

def exportToSQLiteDatabase(form, driverType):
    fileName = tools.getMySQLDatabaseFileName()
    if fileName:
        form.tableWidget.setEnabled(False)
        #start = time()
        if os.path.isfile(fileName):
            os.remove(unicode(fileName))
        conn = sqlite3.connect(unicode(fileName))
        c = conn.cursor()
        dataDatabaseKeysAndType = ''
        l = len(form.ig.columnsHeaders)
        for i in range(l):
            if form.ig.columnsHeaders[i]['type'] == 'String': dataType = ' VARCHAR(1700)'
            elif form.ig.columnsHeaders[i]['type'] == 'Integer': dataType = ' SMALLINT'
            elif form.ig.columnsHeaders[i]['type'] == 'Float': dataType = ' NUMERIC(7, 2)'
            if i < (l-1):
                dataDatabaseKeysAndType = dataDatabaseKeysAndType + "'" + form.ig.columnsHeaders[i]['columnHeader'] + "'" + dataType + ', '
            else:
                dataDatabaseKeysAndType = dataDatabaseKeysAndType + "'" + form.ig.columnsHeaders[i]['columnHeader'] + "'" + dataType
        c.execute('create table allStash (id INTEGER PRIMARY KEY AUTOINCREMENT, ' + dataDatabaseKeysAndType + ')')
        rowCount = form.tableWidget.rowCount()
        for i in range(rowCount):
            form.statusbar.showMessage('Processing ' + os.path.basename(unicode(fileName))  + ' (item ' + str(i+1) + ' of ' + str(rowCount) + ')')
            dataDatabaseValues = ''
            dataDatabaseKeys = ''
            for j in range(l):
                dataValue = form.tableWidget.item(i, j)
                dataType = form.ig.columnsHeaders[j]['type']
                if (not dataValue) and (not dataType == 'String'):
                    dataValue = '0'
                elif (not dataValue.text()) and (not dataType == 'String'):
                    dataValue = '0'
                elif not dataValue.text():
                    dataValue = ''
                else:
                    dataValue = dataValue.text()
                    dataValue.replace("'", "''")
                if j < (l-1):
                    dataDatabaseKeys = dataDatabaseKeys + "'" + form.ig.columnsHeaders[j]['columnHeader'] + "', "
                    dataDatabaseValues = dataDatabaseValues + "'" + dataValue + "', "
                else:
                    dataDatabaseKeys = dataDatabaseKeys + "'" + form.ig.columnsHeaders[j]['columnHeader'] + "'"
                    dataDatabaseValues = dataDatabaseValues + "'" + dataValue + "'"
            c.execute('INSERT INTO allStash (' + unicode(dataDatabaseKeys) + ') VALUES (' + unicode(dataDatabaseValues) + ')')
        conn.commit()
        conn.close()
        form.statusbar.showMessage('Export to SQLite Database complete')
        form.tableWidget.setEnabled(True)
        #print str(tools.printTime(start))
