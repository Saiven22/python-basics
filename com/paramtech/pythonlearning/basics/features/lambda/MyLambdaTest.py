'''
Created on May 2, 2015

@author: bisdallas
'''

def myprint(iterable):
    num = 0;
    while True:
        num += 1
        print num

def showLambda(iterable, key=lambda x: x):
     seen = set()
     num = 0
     myprint = (iterable)
     for elem, ekey, num in ((e, key(e), myprint)for e in iterable):
        if ekey not in seen:
            yield elem
            seen.add(ekey)
    
        

def showLambaExamples():    
    '''
    Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, 
    using a construct called "lambda".
    '''
    double = lambda x: x * 2
    print double(4)
    print double("aaa ")
    names = ["aaaa", "bbbb", "cccc", "aaaa"]
    print names
    uniquvalues = showLambda(names)
    for uniqvalue in uniquvalues:
        print uniqvalue
def showLambdaExample2():
    iseven = lambda x: x % 2 == 0     
    print iseven(5)
    print iseven(2)
    
def showLambdaMap():
    
    c2f = lambda x :((9.0 / 5) * x) + 32
    f2c = lambda x :(5 / 9.0) * (x - 32)
    tvalues = (36, 50.5, -40)
    fvalues = map(c2f, tvalues)
    tvalues2 = map(f2c, fvalues)
    print 'showLambdaMap'
    print tvalues
    print tvalues2
    print fvalues
    

def showLambdreduce():
    max = lambda x, y :x if x > y else y
    min = lambda x, y :x if x < y else y
    
    tvalues = (36, 4, 100, 50.5, 30)
    maxvalue = reduce(max, tvalues)
    minvalue = reduce(min, tvalues)
    print 'showLambdreduce'
    print tvalues
    print maxvalue
    print minvalue


def showLambdfilter():
    iseven = lambda x: x % 2 == 0
    
    tvalues = (2, 4, 6, 7, 8, 912, 34, 567, 34, 6, 7, 9, 23, 456, 89)
    evalues = filter(iseven, tvalues)
    print 'showLambdfilter'
    print tvalues
    print evalues
    
if __name__ == "__main__":
#     showGeneratorExamples()
    showLambaExamples()
    showLambdaExample2()
    showLambdaMap()
    showLambdfilter()
    showLambdreduce()
