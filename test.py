# -*- coding: utf-8 -*-
#from __future__ import division
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

if ('p' in sub1) and ('z' in sub1) and ('t' in sub1):
    print 'find'

# patternStringFire = 'Adds\s\d+\s+to\s\d+\s+Fire Damage'
# pattern = re.compile(pattern)

#print a    # "i am a python string!"
