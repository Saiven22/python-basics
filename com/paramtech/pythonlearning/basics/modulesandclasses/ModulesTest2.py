'''
Created on May 1, 2015

@author: bisdallas
'''
import sysconfig

from submodule import FirstModule

def demoSubModuleFunction(n=1):
    incrementFun = FirstModule.getLambada(n)
    print 'increase 95 by ' + str(n) +' value is '+ str(incrementFun(95))
    
    
if __name__ == "__main__":
    n = 0
    print sysconfig.sys.argv.__len__()
    print sysconfig.sys.argv
    if sysconfig.sys.argv.__len__() == 2:
        n = sysconfig.sys.argv[1]
        
    print n
        
    demoSubModuleFunction(int(n))
        
