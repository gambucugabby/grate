#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------
import os
import subprocess
import filecmp
import sys
import time
import shutil
import Erlog

def ProcFiles(filename):
    sortaDb = []
    i=0
    with open(filename) as f:
        for line in f:
            if ',' in line:
                lines = line.split(',')
            elif '|' in line:
                lines = line.split('|')
            elif ' ' in line:
                lines = line.split(' ')
            else:
                ErrLogging (0, 'Invalid separator for line: ' + line)
            sortaDb.insert(i,lines)
            i=i+1
    print sortaDb
    print sorted(sortaDb, key=lambda l:l[0])
