'''
Created on May 2, 2015

@author: bisdallas

file/module should start with test_
'''
import pytest

@pytest.fixture
def myname(request):
    print "inside myname"
    return "aaa"
    def cleanup_myname():
        print "myname is cleanedup"

def test_is_name(myname):
    print myname
    assert myname is not None
    
def notestis_name2(myname):
    '''
    this method will not be treated as test method as its not start with test
    '''
    print myname
    assert myname is None
    