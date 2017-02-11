import os
dirr= os.path.dirname(__file__)

def getUser():
    filename = os.path.join(dirr, 'dat/user.dat') 
    f = open(filename,'r')
    a=f.read() 
    f.close() 
    return float(a) 
   
if __name__ == '__main__':
    print getUser() 
