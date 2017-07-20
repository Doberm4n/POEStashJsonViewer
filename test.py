# -*- coding: utf-8 -*-
from __future__ import division
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtCore import QUrl
from PyQt4.QtCore import QEvent
from PyQt4.QtCore import QObject
#import res.res
import sys
import re
import os
from json import load
from json import loads
import json
import operator
#from fastnumbers import isfloat

sub1 = "python string!"
sub2 = "an arg"

a = "i %s am a %s" % (sub1, sub2)

a = '    2 '
a = [1]
b = [2.1, 5.1]
#print float(a)
#print int(float(a))
#a = sub1.split(' ')
#a = a[0].split('!')
#a = 2
#b = 7
if a:
    print sum(a)
print sub1
#print sum(a)
print sum(b)

if ('p' in sub1) and not('z' in sub1) and ('t' in sub1):
    print 'find'

a = 1
b = a / 2
if a:
    print a
#print a.find('')
if not a:
    print "find"
b = 'find'
print b.split('f')[1].split('d')[0]

a = [0]*5

print a[1]
print a[2]

a = {'valuedwe': 5, 'valuerwerwe': 2}
b = list(a.values())
bb = list(a.keys())


print bb[b.index(max(b))]

print a[max(a, key=a.get)]

a = [0, 5, 2, 1, 7]

print max(a)

a = ['']*5

print a[1]
#print max(enumerate(a['value']))

listOne = ["hello","world"]
listOne = ['-'.join(i) for i in listOne]

print listOne

a = ['1']
#a.append('fjdkfjkld')
if a[0]:
    a[0] += ' fjdskfjkldshfdsh'
print a

a = []

print len(a)

a = {'fdjskfjdslk': ['fjsdklfjds'], 'fjdsk': []}

for value in a.values():
    if value:
        print value

print len(filter(None, a))
#print a.count('')

print len(a)

a = [[1],[]]

if a[1]:
    print len(a[0])

print a[0][0]

a = []
a.append([])
print a
a[0].append('fjkdsfjlksd')
a.append([])
a[1].append('jfkdsljlfk')

print a[0][0]

print len(filter(None, a))

a = [[1], [0], [], [], [], []]

#a = [[]]*5

#print len(filter(None, a))

#print len(a)

bb = filter(None, a)

print bb

a[1][0] = 'lfkdkwrw'
print a

a = [0, 0]
a[0] = 'fdsfklds' + 'kldsfjkdsl'

print a

a=[0]*5
b = a
print b



if b[0] == 0:
    print b[0]

b[0] = 'fdskfjkldsfdsfd'

print len(b[0])

b =1

a = ("'fwdf'sdfdsd '" + str(b) + "' dfsdfsdfs'")

print a

a = []
print a
for i in range(7):
    a.append([])
#a[0].append(0)
a[0].append('eqwe')
a[0].append(1)
b = 'Thousand Ribbons Tempest Stinger•fwwrweMjölnerSimple Robe'
#a[2] = 'flds'
#a[1].append(["'fdsj'"])
print a
#files = unicode(QtGui.QFileDialog.getOpenFileNames(None, "Select .json files", filter='*.json', directory=os.getcwd()))
#if ewqeqw:
    #print
#print files

a = ['', 'fdsfds', '2', '', 'fdfs']
a = []
print '2' in a
#print a.isfloat()


# patternStringFire = 'Adds\s\d+\s+to\s\d+\s+Fire Damage'
# pattern = re.compile(pattern)

#print a    # "i am a python string!"
