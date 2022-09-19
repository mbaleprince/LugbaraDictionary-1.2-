import time
import os.path

def findfile():
    file = os.path.exists("time.txt")
    if file == True:
        getDetails()
    else:
        timeline()    

def timeline():
    t = time.localtime(time.time())
    f = open('time.txt','w')
    out = t[2]
    f.write(str(out))
    f.close()   

def getDetails():
    T = time.localtime(time.time())
    O = str(T[2])
    file = open('time.txt','r')
    content = file.readline()
    file.close()
    if O == content:
        return True
    else:
        return False
