'''
Created on May 4, 2015

@author: bisdallas
'''
import timeit


def swap():
    a=1
    b=2
    print a, b
    a,b=b,b+a
    b=a-b
    print a, b
    

def reverseString(originalString):
    len1 = len(originalString)
    print len1
    startindex = 0
    reversed = ""
    while True:
        reversed += (originalString[len1 - 1])
        print reversed
        len1 -= 1
        if len1 == 0:
            break
        
    print reversed
    
def reverseString3(originalString):
    print min(timeit.repeat("''.join(reversed('world'))"))
# 2.2613844704083021
    print min(timeit.repeat("'world'[::-1]"))
# 0.28049658041891234
    print min(timeit.repeat("start=stop=None; step=-1; 'world'[start:stop:step]"))
# 0.37622163503510819
    print min(timeit.repeat("start=stop=None; step=-1; reverse_slice = slice(start, stop, step); 'world'[reverse_slice]"))
# 0.54768217598029878

def reverseString2(originalString):
    print "".join(reversed(originalString))
        
    
if __name__ == '__main__':
    reverseString2("Texas")
    reverseString3("abcdef")
    swap()
