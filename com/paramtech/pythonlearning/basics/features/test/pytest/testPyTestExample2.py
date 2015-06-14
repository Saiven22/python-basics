'''
Created on May 2, 2015

@author: bisdallas
this classs is not consider as its not started with test_
'''
import pytest

@pytest.fixture
def myname(request):
    print "inside myname"
    return "aaaa"
    def cleanup_myname():
        print "myname is cleanedup"

def notest_is_name(myname):
#     pytest.skip("skipping this method")
    print myname
    assert myname is not None
    