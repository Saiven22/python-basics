'''
Created on May 3, 2015

@author: bisdallas
'''

def showNestedFunct():
    myName = "aaa"
    
    def mylen(stringline):
        x = 0;
        for a in stringline:
            x += 1 
        return x 
    print mylen(myName)
    
    
if __name__ == '__main__':
    showNestedFunct()
