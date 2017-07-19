# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
sys.path.insert(0,os.path.dirname(parentdir))
from PyQt4 import QtSql
import modules.tools as tools

def exportToSQLiteDatabase(form, driverType):
    fileName = tools.getMySQLDatabaseFileName()
    if fileName:
        form.tableWidget.setEnabled(False)
        if os.path.isfile(fileName):
            os.remove(unicode(fileName))
        db = QtSql.QSqlDatabase.addDatabase(driverType)
        db.setDatabaseName(fileName)
        dataDatabaseKeysAndType = ''
        if not db.open():
            form.statusbar.showMessage('Database not open: ' +  db.lastError().text())
            return
        dataDatabaseKeys = ''
        l = len(form.ig.columnsHeaders)
        for i in range(l):
            if form.ig.columnsHeaders[i]['type'] == 'String': dataType = ' VARCHAR(1700)'
            elif form.ig.columnsHeaders[i]['type'] == 'Integer': dataType = ' SMALLINT'
            elif form.ig.columnsHeaders[i]['type'] == 'Float': dataType = ' NUMERIC(7, 2)'
            if i < (l-1):
                dataDatabaseKeysAndType = dataDatabaseKeysAndType + "'" + form.ig.columnsHeaders[i]['columnHeader'] + "'" + dataType + ', '
                dataDatabaseKeys = dataDatabaseKeys + "'" + form.ig.columnsHeaders[i]['columnHeader'] + "', "
            else:
                dataDatabaseKeysAndType = dataDatabaseKeysAndType + "'" + form.ig.columnsHeaders[i]['columnHeader'] + "'" + dataType
                dataDatabaseKeys = dataDatabaseKeys + "'" + form.ig.columnsHeaders[i]['columnHeader'] + "'"
        query = QtSql.QSqlQuery()
        dataCreateTableQuery = 'create table stash (id INT AUTO_INCREMENT PRIMARY KEY, ' + dataDatabaseKeysAndType + ')'
        query.exec_(dataCreateTableQuery)
        dataBindSubst = '?'*l
        dataBindSubst = ' ,'.join(dataBindSubst)
        rowCount = form.tableWidget.rowCount()
        dataDatabaseValuesSectionBind = []
        for i in range(l):
            dataDatabaseValuesSectionBind.append([])
        query.prepare('INSERT INTO stash (' + dataDatabaseKeys + ') VALUES ' + '(' + dataBindSubst + ')')
        for i in range(l):
            form.statusbar.showMessage('Processing column: ' +  str(i) + ' of ' + str(l-1))
            for j in range(rowCount):
                dataValue = form.tableWidget.item(j, i)
                if not dataValue:
                    dataValue = None
                else:
                    dataValue = dataValue.text()
                    dataValue.replace("'", "''")
                dataDatabaseValuesSectionBind[i].append(dataValue)
            query.addBindValue(dataDatabaseValuesSectionBind[i])
        form.statusbar.showMessage('Executing query to SQLite Database...')
        query.execBatch()
        db.removeDatabase(driverType)
        db.close()
        form.tableWidget.setEnabled(True)
        form.statusbar.showMessage('Export to SQLite Database complete')
