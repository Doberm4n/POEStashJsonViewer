# -*- coding: utf-8 -*-
import operator
# from PyQt4 import QtGui
# from PyQt4 import QtCore
# from PyQt4.QtGui import QDesktopServices
# from PyQt4.QtCore import QUrl
# from PyQt4.QtCore import QEvent
# from PyQt4.QtCore import QObject
# #import res.res
# import sys
# import re
# import os
# from json import load
# from json import loads
# import json

sub = {"python string!", "an arg"}
sub1 = "python string!"
sub2 = "an arg"



a = "i %s am a %s" % (sub1, sub2)
#a = "i %s am a %s" % (*sub)
tu = ['15', '12']
a = "{0} retretre".format(*tu)
print a

test = sub1.split()[0]
if sub1 > sub2:
	print "Yes"

print test
print sub1
print

#a = "i am a " % (sub1, sub2)

#print a    # "i am a python string!"
