'''
Created on May 2, 2015

@author: bisdallas
'''

class MyException(Exception):
    '''
    classdocs
    '''


    def __init__(self, message):
        '''
        Constructor
        '''
        super(MyException, self).__init__(message)
        self.message=message
        