'''
Created on May 1, 2015

@author: bisdallas
'''

def showDataTypes():
    age=10
    name="helloWorld"
    salary=6587.89
    contact_numbers=(12345,6789,24689)
    roles=['admin','employee','executive']
    tax_paid={2016:10000,2015:6777}
    
    print name
    print age
    print salary
    print contact_numbers[:2]
    print roles[1]
    print tax_paid[2015]
    



if __name__== "__main__":
    showDataTypes()