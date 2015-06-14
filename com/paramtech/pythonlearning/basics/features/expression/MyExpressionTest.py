'''
Created on May 3, 2015

@author: bisdallas
'''

def showExpression():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print([x for x in list if x % 2 == 0])
    
if __name__ == '__main__':
    showExpression()
    myname = 'raman'
    print myname[::-1]
    reversed = ''
    index = len(myname)
    while index > 0:
        reversed.append(0, myname[index - 1])
        index -= 1
    print myname,reversed
