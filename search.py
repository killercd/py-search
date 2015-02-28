#!/usr/bin/env python

import sys
import os
import glob

files = []



def usage():
    print "Usage: search.py folder pattern [file_content]"

    
def isInFile(fl, content):
    content = content.lower()
    f = open(fl, 'r')
    for line in f.xreadlines():
        line = line.lower()
        if line.find(content)>-1:
            return True
    

if len(sys.argv)<3:
    usage()
    sys.exit(-1)

folder = sys.argv[1]
pattern = sys.argv[2]
content = ""


if len(sys.argv)>3:
    content = sys.argv[3].strip()

for root, dirnames, filenames in os.walk(folder):
    matches = glob.glob(root + "/"+pattern)
    for fl in matches:
        if len(matches)>0:
            if content!="":
                if isInFile(fl,content):
                    print fl
            else:
                print fl
