'''
Created on May 1, 2015

@author: bisdallas
'''

def showOperations():
    print '5/2= ' + str(5 / 2)  # in Python 3 it will be 2.5
    print '5//2= ' + str(5 // 2)  # // omits fraction
    print '5./2= ' + str(5. / 2)
    print '5.//2= ' + str(5. // 2)  # if one of them is decimal result will be decimal
    
    print '5%2=' + str(5 % 2)
    print '5**2=' + str(5 ** 2)
    
    pass

if __name__ == "__main__":
    showOperations()
