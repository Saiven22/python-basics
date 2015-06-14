'''
Created on Apr 30, 2015

@author: bisdallas
'''
import string


def helloWorld():
    print "this is hello world python program"
    
def showDifferentQuotes():
    print 'this is single quote'
    print "this is double quotes"
    print """this is for multiline\n
statemenst we can right what ever we wanted
this is 3rd line
    """
def showPrintTypes():    
    myname = "bbb aaa"
    print "aaa ", "bbb"
    print "aaa " + "bbb"
    print "Strings--> Name is %s number %%f is %.08f " % (myname, 6.12345)
    mymap = {'name':'aaa', 'place':'dallas'}
    print ("map--> is %(name)s from %(place)s " % mymap)
    mystring="template-->this is $name from $place "
    template=string.Template(mystring)
    print template.substitute(mymap)
    
    mytuple = ('aaa', 'dallas')
    print "tuple--> Name is %s from  %s" % mytuple
    mylist = ['aaa', 'dallas']
    try:
        print "list-->My Name is %s from  %s" % mylist
    except Exception as e:
        print str(e)
        print 'list will not work '
        print "list-->My Name is %s from  %s" % (mylist[0],mylist[1])

def showMultiLineExample():
    item_one = 1
    item_two = 2
    item_three = 3
    item_four = 4
    
    total = item_one + \
            item_two + \
            item_three + \
            item_four
            
    print total

if __name__ == "__main__":
    helloWorld()
    showMultiLineExample()
    showDifferentQuotes()
    showPrintTypes()
