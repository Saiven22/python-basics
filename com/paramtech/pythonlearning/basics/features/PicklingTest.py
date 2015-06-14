'''
Created on May 4, 2015

@author: bisdallas
'''
import pickle
def dump():
    my_list = ["abc", "def", "ghi"]
    pickle.dump(my_list, open("my_list.txt", "wb"))

def undemp():
    my_list = pickle.load(open("my_list.txt", "rb"))
    for item in my_list:
        print item

if __name__ == '__main__':
    dump()
    undemp()
