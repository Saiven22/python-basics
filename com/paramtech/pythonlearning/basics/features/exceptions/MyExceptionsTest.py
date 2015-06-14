'''
Created on May 2, 2015

@author: bisdallas
'''
from MyException import MyException
def demoExceptionScenario():
    try:
        int("aaa")
    except ValueError as ve:
        print str(ve)
        raise MyException("this is error")
    except TypeError as te:
        print str(te)
    except :
        print "error"
    finally:
        print "in finally block"
if __name__ == '__main__':
    try:
        demoExceptionScenario()
    except MyException as me:
        print me