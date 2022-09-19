import time
import os.path

def create():
    fileX = os.path.exists("month.txt")
    if fileX == True:
        getDatas()
    else:
        build()

def build():
    tX = time.localtime(time.time())
    fX = open('month.txt','w')
    output = tX[1]
    fX.write(str(output))
    fX.close()

def getDatas():
    TimeX = time.localtime(time.time())
    MonthX = str(TimeX[1])
    file = open('month.txt','r')
    contents = file.readline()
    file.close()
    if MonthX == contents:
        return True
    else:
        return False  
