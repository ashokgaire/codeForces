a = ['a','b','c','aa','d','b']
b = [1,2,3,4,5,6]

first = 1
last = 5
d = 'caaab'

# class Tier

class Tier:
    sid = None
    isEOF = False
    failState = 0
    value = None
    outputset = None
    tranList = None
    def __init__(self,index,val):
        self.sid = index
        self.value = val
        self.outputset = set()
        self.tranList = {}
        self.failState = 0

    def goto(self,key):
        if key in self.tranList:
            return self.tranList[k]

 
#class Adhoc

class Adhoc:
    root = None
    sid = 0
    table = {}

    def __init__(self):
        self.root = Tier(0,None)
        self.table[0] = self.root

    def addKeyword(self,keyword):
        current = self.root

        for key in keyword:
            if key not in current.tranList:
                self.sid = self.sid + 1
                current.tranList[key] = Tier(self.sid,key)
                self.table[self.sid] = current.tranList[key]

        current = current.tranList[key]
        current.isFinal = True
        current.outputset.add(keyword)
        print(current.tranList)




if __name__ == '__main__':
    x = Adhoc()
    for i in a:
        x.addKeyword(i)

