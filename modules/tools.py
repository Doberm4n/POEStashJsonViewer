# -*- coding: utf-8 -*-
from json import load
from json import loads
import json

def readJson(json_file):
        if json_file:
            #try:
                with open(json_file) as data_file:
                    return load(data_file)
            #except Exception, e:
                 #print "Error: " + str(e)

def writeJson(dump, json_file):
    if json_file:
        try:
            #print ""
            with open(json_file, 'w') as outfile:
                    json.dump(dump, outfile)
        except Exception, e:
             print "Error: " + str(e)