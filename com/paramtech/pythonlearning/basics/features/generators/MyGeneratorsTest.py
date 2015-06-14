'''
Created on May 2, 2015

@author: bisdallas
'''

def myRange(n):
    while n != 0:
        yield n
        n -= 1
    
def showLambda(iterable, key=lambda x: x):
     seen = set()
     for elem, ekey in ((e, key(e)) for e in iterable):
        if ekey not in seen:
            yield elem
            seen.add(ekey)
    
def showLambda2(iterable):
     seen = set()
     for elem  in iterable:
        if elem not in seen:
            yield elem
            seen.add(elem)
        
def showGeneratorExamples():
    squares = (x * x for x in range(3))
    print squares
    for x in squares:
        print x
    set = {x * x for x in range(3)}
    print set
    list = [x * x for x in range(3)]
    print list
def showLambaExamples():    
    '''
    Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, 
    using a construct called "lambda".
    '''
    uniquvalues=showLambda(("aaa","bbb","ccc","aaa"))
    for uniqvalue in uniquvalues:
        print uniqvalue
    
    gen10 = myRange(3)
    for num in gen10:
        print num
    
if __name__ == "__main__":
    showGeneratorExamples()
    showLambaExamples()
    
