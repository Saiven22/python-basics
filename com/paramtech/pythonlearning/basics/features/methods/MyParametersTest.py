

def showDefaultParameter(name="aaa"):
    print name

def showDefaultParameter2(age, name="aaa",):
    print name
def addNames(name, names=[]):
    names.append(name)
    return names
def properAddNames(name, names=None):
    if names is None:
        names = []
    names.append(name)
    return names
if __name__ == "__main__":
    showDefaultParameter2(33, "bbb")
    showDefaultParameter2(33)
    showDefaultParameter("bbb")
    showDefaultParameter()
    print addNames("AAAA")
    print addNames('BBBB')
    print addNames("CCCC", [])
    print properAddNames("AAAA")
    print properAddNames('BBBB')
    print properAddNames("CCCC", [])
