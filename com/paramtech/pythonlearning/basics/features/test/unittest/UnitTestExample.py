'''
Created on May 2, 2015

@author: bisdallas
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        print "setup is completed"


    def tearDown(self):
        print "tearDown is completed"

    def testName(self):
        assert "checking.."

    def testName2(self):
        assert "checking.."

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()