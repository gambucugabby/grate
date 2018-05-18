#-------------------------------------------------------------------------------
#Step 1 - Guaranteed Rate "HomeWork"
#
#Takes 3 types of files (comma, space and pipe delimited)
#in python list (theoretically unlimited) and merges them into
#a list for sorting in 3 orders:
#type 1 = gender (females first), and then last name
#type 2 = birthdate ascending
#type 3 = last name descending
#-------------------------------------------------------------------------------
import Erlog
import time
import operator
import filecmp

def ProcFiles(filename, sortTyp):
    sortaDbs = []
    i=0
    for flnm in filename:
        with open(flnm) as f:
            for line in f:
                try:
                    lines = line.rstrip('\n')
                    if ',' in lines:
                        lines = lines.split(',')
                    elif '|' in lines:
                        lines = lines.split('|')
                    elif ' ' in lines:
                        lines = lines.split(' ')
                except:
                    ErrLogging (0, 'Invalid separator for line: ' + line)
                sortaDbs.insert(i,lines)
                i=i+1

    #stick it in a file b/c I'll need it for the REST API
    filename = 'DaSotraDb'
    f=open(filename, 'a')
    for dLn in sortaDbs:
        f.write(str(dLn) + '\n')
    f.close()

    f=open(filename, 'r')
    DaSotraDbAll = []
    j=0
    for rLn in f:
        rLn = rLn.rstrip('\n')
        rLn = rLn.replace('[','')
        rLn = rLn.replace(']','')
        rLn = rLn.replace("'",'')
        rLn = rLn.split(',')
        print rLn
        DaSotraDbAll.insert(j, rLn)
        j=j+1
    f.close()


    if sortTyp == 1:
        #This is the sort type of gender (females before males) then last name ascending
        return sorted(DaSotraDbAll, key=operator.itemgetter(2,1))
    elif sortTyp == 2:
        #This is the sort type of birthdate, ascending
        return sorted(DaSotraDbAll, key=lambda x: (x[4].split('/')[::-1], x[-1]))
    elif sortTyp == 3:
        #This is the sort type of lastname, descending
        return sorted(DaSotraDbAll, key=lambda l:l[0], reverse=True)
    elif sortTyp == 4:
        #This is the sort type of lastname for RESTAPI
        return sorted(DaSotraDbAll, key=lambda l:l[0])
    #else:
        #erlog.ErrLogging (0, 'Invalid return type or ecord added via RESTAPI')
