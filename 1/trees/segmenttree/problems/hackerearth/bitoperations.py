class sTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.arr = [0] * (2*self.size)
        self.xor = [0] * (2*self.size)


    def setXor(self,i,v,x,lx,rx):
        if rx - lx == 1:
            self.arr[x]= self.arr[x]^v
            self.xor[x] = self.xor[x]^v
            return 
        m = (lx+rx)//2
        if i < m:
            self.setXor(i,v,2*x+1,lx,m)
        else:
            self.setXor(i,v,2*x+2, m , rx)
        self.arr[x] = self.arr[2*x+1] + self.arr[2*x+2]
        self.xor[x] = self.xor[2*x+1] ^ self.xor[2*x+2]

    def setAnd(self,i,v,x,lx,rx):
        if rx - lx == 1:
            self.arr[x] = self.arr[x]&v
            self.xor[x] = self.xor[x]&v
            return 
        m = (lx+rx)//2
        if i < m:
            self.setAnd(i,v,2*x+1,lx,m)
        else:
            self.setAnd(i,v,2*x+2, m , rx)
        self.arr[x] = self.arr[2*x+1] + self.arr[2*x+2]

        self.xor[x] = self.xor[2*x+1] ^ self.xor[2*x+2]

    def setOr(self,i,v,x,lx,rx):
        if rx - lx == 1:
            self.arr[x] = self.arr[x]|v
            self.xor[x] = self.xor[x]|v
            return 
        m = (lx+rx)//2
        if i < m:
            self.setOr(i,v,2*x+1,lx,m)
        else:
            self.setOr(i,v,2*x+2, m , rx)
        self.arr[x] = self.arr[2*x+1] + self.arr[2*x+2]

        self.xor[x] = self.xor[2*x+1] ^ self.xor[2*x+2]

    def setHelper(self,typ, l, r, v):
        for i in range(l,r):
            if typ == 1:
                self.setOr(i,v,0,0,self.size)
            elif typ == 2:
                self.setAnd(i,v,0,0,self.size)
            else:
                self.setXor(i,v,0,0,self.size)
    
    def xorQuery(self,l,r,x,lx,rx):
        if l >= rx or lx >= r: return 0
        if lx >= l and rx <=r: return self.xor[x]

        m = (lx+rx)// 2
        m1 = self.xorQuery(l,r,2*x+1,lx,m)
        m2 = self.xorQuery(l,r,2*x+2,m,rx)
        return m1^m2
    def sumQuery(self,l,r,x,lx,rx):
        if l >= rx or lx >= r: return 0
        if lx >= l and rx <=r: return self.arr[x]

        m = (lx+rx)// 2
        m1 = self.sumQuery(l,r,2*x+1,lx,m)
        m2 = self.sumQuery(l,r,2*x+2,m,rx)
        return m1+m2

    def query(self,typ, l, r):
        if typ == 4:
            return self.sumQuery(l,r,0,0,self.size)
        else:
            return self.xorQuery(l,r,0,0,self.size)


n , m = map(int, input().split())
st = sTree(n)

while m > 0:
    query = list(map(int , input().split()))
    if query[0] == 1:
        st.setHelper(1, query[1]-1, query[2], query[3])
    elif query[0] == 2:
        st.setHelper(2, query[1]-1, query[2], query[3])
    elif query[0] == 3:
        st.setHelper(3, query[1]-1, query[2], query[3])
    elif query[0] == 4:
        
        print(st.query(4,query[1]-1, query[2]))
    else:
        print(st.query(5, query[1]-1, query[2]))

    m -=1
