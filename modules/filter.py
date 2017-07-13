# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import operator
import ui.main_layout

#import modules.tools as tools

def applyFilter(form, filterLines):
        print filterLines
        if filterLines != '':
            filters = {}
            filters.update({'filters' : []})

            #filterLines = filterLines
            print 'Length: ' + str(len(filterLines))
            for i in range (len(filterLines)):
                filters['filters'].append({'columnHeader' : None, 'operand' : None, 'filterValue' : None, 'filterType' : None})

                temp = filterLines[i].split(' [')
                filters['filters'][i]['columnHeader'] = temp[0]
                filters['filters'][i]['operand'] = temp[1].split('] ')[0]

                filters['filters'][i]['filterType'] = form.ig.columnsHeaders[form.ig.columnNameToIndex[temp[0]]]['type']

                # if (filters['filters'][i]['operand'].find('contains') >= 0) or (filters['filters'][i]['operand'].find('match') >=0):
                #     filters['filters'][i]['operand'] = filters['filters'][i]['operand'].replace('match', '=')
                #     filters['filters'][i]['filterType'] = 'String'
                # else:
                #     filters['filters'][i]['filterType'] = 'Integer'

                if filters['filters'][i]['filterType'] == 'String':
                    filters['filters'][i]['operand'] = filters['filters'][i]['operand'].replace('match', '=')

                filters['filters'][i]['filterValue'] = temp[1].split('] ')[1]

                filters['filters'][i]['operand'] = form.ig.operandsChars[filters['filters'][i]['operand']]

            print filters['filters']
            filterTable(form, filters)

def filterTable(form, filters):
    for i in range (len(filters['filters'])):
        columnHeader = filters['filters'][i]['columnHeader']
        filterType = filters['filters'][i]['filterType']
        filterValue = filters['filters'][i]['filterValue']

        operand = filters['filters'][i]['operand']

        #print unicode(form.tableWidget.item(0, form.ig.columnNameToIndex[columnHeader]).text())
        print columnHeader
        print filterType
        print filterValue
        print operand
        for j in range (form.tableWidget.rowCount()):
            if form.tableWidget.isRowHidden(j) == True:
                continue
            if form.tableWidget.item(j, form.ig.columnNameToIndex[columnHeader]):
                itemValue = form.tableWidget.item(j, form.ig.columnNameToIndex[columnHeader]).text()
            else:
                itemValue = ''
            #if not itemValue:
            if (filterType == 'String') and (filters['filters'][i]['operand'] == operator.contains):
                if (not operand(unicode(itemValue).lower(), filterValue.lower())):
                    form.tableWidget.hideRow(j)
            elif (filterType == 'String'):
                    if (not operand(unicode(itemValue), filterValue)):
                        form.tableWidget.hideRow(j)
            else:
                if not itemValue:
                    form.tableWidget.hideRow(j)
                else:
                    filterValue = float(filterValue)
                    if (not operand(float(itemValue), filterValue)):
                        form.tableWidget.hideRow(j)
    ui.main_layout.tableWidgetContentsAutoSize(form)
    print "Applied"

    def resetFilter(form):
        for i in range (len(form.tableWidget.rowCount())):
            if form.tableWidget.row(i).isRowHidden():
                form.tableWidget.showRow(i)

