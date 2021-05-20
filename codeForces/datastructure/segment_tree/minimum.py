import sys


class item:
    def __init__(self,m,c):
        self.m = m
        self.c = c

class segment:
    size = 1
    mins = []

    def merge(self,a,b):
        if a.m < b.m:
            return a
        if a.m > b.m:
            return b
        return item(a.m,a.c + b.c)
    
    def single(self,v):
        return item(v,1)
    NEUTRAL_ELEMENT = item(sys.maxsize, 0)

    def __init__(self,n):
        while self.size <= n:
            self.size *=2
        self.mins = [item(0,0)]*(2*self.size)
        
    

    def build2(self,a,x,lx,rx):
        if rx - lx ==1:
            if lx < len(a):
                self.mins[x] = self.single(a[lx])
            return
        
        m = (lx + rx) // 2
        self.build2(a,2*x+1, lx, m)
        self.build2(a,2*x+2,m,rx)
        
        
        self.mins[x] = self.merge(self.mins[2*x+1], self.mins[2*x+2])
    
    def build(self,a):
        self.build2(a,0,0,self.size)

    
    
    def set2(self,i,v,x,lx,rx):
        if rx - lx == 1:
            self.mins[x] = self.single(v)
            return 
        
        m = (rx+lx) // 2

        if i < m:
            self.set2(i,v,2*x+1,lx,m)
        else:
            self.set2(i,v,2*x+2, m,rx)
        self.mins[x] = self.merge(self.mins[2*x+1], self.mins[2*x+2])

    def set(self,i,v):
        return self.set2(i,v,0,0,self.size)
    
    def min2(self,l,r,x,lx,rx):
        if lx >= r or l >= rx: return self.NEUTRAL_ELEMENT
        if lx >= l and rx <= r: return self.mins[x]

        m = (rx+lx)//2

        m1 = self.min2(l,r,2*x+1, lx, m)
        m2 = self.min2(l,r,2*x+2,m,rx)

        return self.merge(m1,m2)



    def min(self,l,r):
        return self.min2(l,r,0,0,self.size)


if __name__ == "__main__":
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    st = segment(n)
    st.build(arr)

    while m > 0:
        op,i,v = map(int, input().split())

        if op == 1:
            st.set(i,v)
        else:
            res = st.min(i,v)
            print(res.m, res.c)
        m -=1