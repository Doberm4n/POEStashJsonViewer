# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
sys.path.insert(0,os.path.dirname(parentdir))
from PyQt4 import QtSql
#import json
import modules.tools as tools
import sqlite3
from time import time


def exportToSQLiteDatabase(form, driverType):
    fileName = tools.getMySQLDatabaseFileName()
    if fileName:
        form.tableWidget.setEnabled(False)
        start = time()

        if os.path.isfile(fileName):
            os.remove(unicode(fileName))

        #db = QtSql.QSqlDatabase.addDatabase(driverType)

        #db.setDatabaseName(fileName)

        conn = sqlite3.connect(unicode(fileName))

        c = conn.cursor()


        #dataTableCreateQuery = "create table sportsmen(id int primary key, ""firstname varchar(20), lastname varchar(20))"
        dataDatabaseKeysAndType = ''

        # if not db.open():
        #     form.statusbar.showMessage('Database not open: ' +  db.lastError().text())
        #     return

        l = len(form.ig.columnsHeaders)
        for i in range(l):
            if form.ig.columnsHeaders[i]['type'] == 'String': dataType = ' VARCHAR(1700)'
            elif form.ig.columnsHeaders[i]['type'] == 'Integer': dataType = ' SMALLINT'
            elif form.ig.columnsHeaders[i]['type'] == 'Float': dataType = ' NUMERIC(7, 2)'

            if i < (l-1):
                dataDatabaseKeysAndType = dataDatabaseKeysAndType + "'" + form.ig.columnsHeaders[i]['columnHeader'] + "'" + dataType + ', '
            else:
                dataDatabaseKeysAndType = dataDatabaseKeysAndType + "'" + form.ig.columnsHeaders[i]['columnHeader'] + "'" + dataType
        print dataDatabaseKeysAndType

        #query = QtSql.QSqlQuery()

        c.execute('create table allStash (id INTEGER PRIMARY KEY AUTOINCREMENT, ' + dataDatabaseKeysAndType + ')')

        #query.exec_(dataCreateTableQuery)
        rowCount = form.tableWidget.rowCount()
        for i in range(rowCount):
            form.statusbar.showMessage('Processing ' + os.path.basename(unicode(fileName))  + ' (item ' + str(i+1) + ' of ' + str(rowCount) + ')')
            #print 'Processing row: ' +  str(i+1) + ' of ' + str(rowCount)

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

            #print dataDatabaseKeys
            #print unicode(dataDatabaseValues)

            c.execute('INSERT INTO allStash (' + unicode(dataDatabaseKeys) + ') VALUES (' + unicode(dataDatabaseValues) + ')')

            #print unicode(dataInsertValuesQuery)

                # query.prepare('UPDATE "%s" SET value=:val WHERE property=:var' % tbl)
                # query.bindValue(':val', val)
                # query.bindValue(':var', var)

            #query.exec_(dataInsertValuesQuery)
                # query.bindValue(":id", 1001);
                # query.bindValue(":forename", "Bart");
                # query.bindValue(":surname", "Simpson");
                # query.exec()

                # query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
        #db.removeDatabase(driverType)
        #db.close()
        conn.commit()
        conn.close()
        form.statusbar.showMessage('Export to SQLite Database complete')
        form.tableWidget.setEnabled(True)
        print str(tools.printTime(start))


        # temp = json.dumps(data)
        # jsonData = json.loads(temp)




        # #with open(unicode(fileName), 'wb') as stream:

        # jsonData['common']['singleJsonVersion'] = form.ig.jsonConfig['common']['configVersion']

        # for i in range(form.tableWidget.rowCount()):
        #         #jsonItemValues = []
        #         jsonData['rows'].append([])
        #         for j in range(form.tableWidget.columnCount()):
        #             itemValue = form.tableWidget.item(i, j)
        #             if itemValue:
        #                 jsonData['rows'][i].append(unicode(itemValue.text()))
        #             else:
        #                 jsonData['rows'][i].append('')
        # tools.writeJson(jsonData, unicode(fileName))