import sys
import time

def ErrLogging(errSev,errDesc):
    logTxt = (str(time.time()) + ',' + (errSev) + ',' + (errDesc))
    errfl = open("log.txt", 'a')
    errfl.write(logTxt+'\n')


def shellquote(s):
    s= "'" + s.replace("'", "'\\''") + "'"
    s = s.replace("|", "")
    s = s.replace("del", "")
    s = s.replace("ls", "")
    s = s.replace("rm", "")
    s = s.replace(":(){:|:&};:", "")
    s = s.replace("command > /dev/sda", "")
    s = s.replace("wget", "")
    return s
