

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

class sumTree:
    def __init__(self,n):
        self.size = 1
        while self.size < n:
            self.size *=2
        self.sumarray = [0] * (2* self.size)

    def buildSum(self, a, x , lx, rx):
        if rx - lx == 1:
            if lx < len(a):
                self.sumarray[x] = a[lx]
            return
        m = (lx+rx)//2
        self.buildSum(a,2*x+1, lx, m)
        self.buildSum(a,2*x+2, m , rx)
        self.sumarray[x] = self.sumarray[2*x+1] + self.sumarray[2*x+2]

    def build(self,a):
        self.buildSum(a, 0, 0, self.size)
    

    def set2(self,i,v,x,lx,rx):
        if rx - lx == 1:
            self.sumarray[x] = v
            return
        m = (lx+rx)//2

        if i < m:
            self.set2(i,v,2*x+1, lx,m)
        else:
            self.set2(i,v,2*x+2, m, rx)
        self.sumarray[x] = self.sumarray[2*x+1] + self.sumarray[2*x+2]



    
    def set(self,i,v):
        self.set2(i,v,0,0,self.size)

    def setGcd2(self,i,v,x,lx,rx):
        if rx - lx == 1:
            if self.sumarray[x] > 0:
                self.sumarray[x] = gcd(self.sumarray[x], v)
            return
        m = (lx + rx) //2
        if i < m:
            self.setGcd2(i,v,2*x+1,lx,m)
        else:
            self.setGcd2(i,v,2*x+2, m, rx)
        self.sumarray[x] = self.sumarray[2*x+1] + self.sumarray[2*x+2]

    def setGcd(self,i,v):
        self.setGcd2(i,v,0,0,self.size)
    def queryHelper(self,l,r,x,lx,rx):
        if l >= rx or lx >= r : return 0
        if lx >= l and rx <= r: return self.sumarray[x]
        m = (lx+rx) // 2
        m1 = self.queryHelper(l,r,2*x+1, lx,m)
        m2 = self.queryHelper(l,r,2*x+2,m , rx)
        return m1+m2


    def query(self,l,r):
        return self.queryHelper(l,r,0,0,self.size)




class maxTree:
    def __init__(self,n):
        self.size = 1
        while self.size < n:
            self.size *=2
        self.maxarray= [0] * (2* self.size)

    def buildMax(self, a, x , lx, rx):
        if rx - lx == 1:
            if lx < len(a):
                self.maxarray[x] = a[lx]
            return
        m = (lx+rx)//2
        self.buildMax(a,2*x+1, lx, m)
        self.buildMax(a,2*x+2, m , rx)
        self.maxarray[x] = max(self.maxarray[2*x+1] , self.maxarray[2*x+2])

    def build(self,a):
        self.buildMax(a, 0, 0, self.size)
    


    def set2(self,i,v,x,lx,rx):
        if rx - lx == 1:
            self.maxarray[x] = v
            return
        m = (lx+rx)//2

        if i < m:
            self.set2(i,v,2*x+1, lx,m)
        else:
            self.set2(i,v,2*x+2, m, rx)
        self.maxarray[x] = max(self.maxarray[2*x+1] , self.maxarray[2*x+2])



    
    def set(self,i,v):
        self.set2(i,v,0,0,self.size)

    def setGcd2(self,i,v,x,lx,rx):
        if rx - lx == 1:

            if self.maxarray[x] > 0:
                self.maxarray[x] = gcd(self.maxarray[x], v)
            return
        m = (lx + rx) //2
        if i < m:
            self.setGcd2(i,v,2*x+1,lx,m)
        else:
            self.setGcd2(i,v,2*x+2, m, rx)
        self.maxarray[x] = max(self.maxarray[2*x+1] , self.maxarray[2*x+2])

    def setGcd(self,i,v):
        self.setGcd2(i,v,0,0,self.size)
    def queryHelper(self,l,r,x,lx,rx):
        if l >= rx or lx >= r : return 0
        if lx >= l and rx <= r: return self.maxarray[x]
        m = (lx+rx) // 2
        m1 = self.queryHelper(l,r,2*x+1, lx,m)
        m2 = self.queryHelper(l,r,2*x+2,m , rx)
        return max(m1,m2)


    def query(self,l,r):
        return self.queryHelper(l,r,0,0,self.size)

n,q = map(int, input().split())
a = list(map(int, input().split()))
stSum =sumTree(n)
stMax = maxTree(n) 
stSum.build(a)
stMax.build(a)
while q > 0:
    query = list(map(int, input().split()))

    if query[0] == 3:
        
        print(stMax.query(query[1]-1, query[2]-1))
    elif query[0] == 4:
        
        print(stSum.query(query[1]-1, query[2]))
    
    elif query[0] == 1:
        l = query[1]-1
        r = query[2]
        v = query[3]

        for i in range(l,r):
            stSum.set(i,v)
        for i in range(l,r-1):
            stMax.set(i,v)
    else:

        l = query[1]-1
        r = query[2]
        v = query[3]
        

        for i in range(l,r-1):
            stMax.setGcd(i,v)
        for i in range(l,r):

            stSum.setGcd(i,v)


    q -=1
