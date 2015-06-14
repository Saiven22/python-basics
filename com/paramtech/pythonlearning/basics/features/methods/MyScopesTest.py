'''
Created on May 3, 2015

@author: bisdallas
'''

myname = ("bbb", "aaa")
def showLocalScopExample():

    myname = ("ccc", "bbb", "aaa")
    print myname
    showMyname()
def showGoblaScopExample():
    global myname
    myname = ("ccc", "bbb", "aaa")
    print myname
    showMyname()
def showGoblaScopExample2(myname2):
    global myname
    myname2 = ("ccc", "bbb", "aaa","mca")
    print myname2
    showMyname()
        
def showMyname():
    print myname
    
if __name__ == '__main__':
    showLocalScopExample()
    showGoblaScopExample()
    showGoblaScopExample2(myname)