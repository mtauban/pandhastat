import os
dir = os.path.dirname(__file__)

def setStatus(st):
    filename = os.path.join(dir,'dat/status.dat')
    f = open(filename,'w')
    f.write(st)
    f.close()

def getStatus():
    filename = os.path.join(dir,'dat/status.dat')
    f = open(filename,'r')
    a=f.read()
    f.close()
    return float(a)

