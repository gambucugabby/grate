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


    if sortTyp == 1:
        #This is the sort type of gender (females before males) then last name ascending
        print sorted(sortaDbs, key=operator.itemgetter(2,1))
    elif sortTyp == 2:
        #This is the sort type of birthdate, ascending
        print sorted(sortaDbs, key=lambda x: (x[4].split('/')[::-1], x[-1]))
    elif sortTyp == 3:
        #This is the sort type of lastname, descending
        print sorted(sortaDbs, key=lambda l:l[0], reverse=True)
    else:
        ErrLogging (0, 'Invalid Sort Type')
