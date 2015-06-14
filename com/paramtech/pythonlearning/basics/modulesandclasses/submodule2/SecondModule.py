'''
Created on May 1, 2015

@author: bisdallas
'''
class Customer:
    def __init__(self,name,age,state):
        self.name=name
        self.age=age
        self.state=state
    
    def show(self):
        print self.name
        print self.age
        print self.state
        