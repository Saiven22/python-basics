'''
Created on May 1, 2015

@author: bisdallas
'''
from submodule import FirstModule

def demoSubModuleFunction():
    increment2 = FirstModule.getLambada(2)
    print increment2(95)
    
    
if __name__ == "__main__":
    demoSubModuleFunction()
    
