import sys

class segmentTree:
    def __init__(self,n):
        self.size = 1

        while self.size < n:
            self.size *=2
        self.arr = [0] * (2*self.size)
    
    def build2(self,a,x,lx,rx):
        if rx - lx == 1:
            if lx < len(a):
                self.arr[x] = a[lx]
            return 
        m = (rx+lx) // 2
        self.build2(a,2*x+1,lx,m)
        self.build2(a,2*x+2,m,rx)
        self.arr[x]= min(self.arr[2*x+1], self.arr[2*x+2])
    
    def build(self,a):
        self.build2(a,0,0,self.size)
    
    def set2(self,i,v,x,lx,rx):
        if rx - lx == 1:
            self.arr[x] = v
            return 
        m = (rx+lx)//2
        if i < m:

            self.set2(i,v,2*x+1, lx,m)
        else:
            self.set2(i,v,2*x+2, m,rx)
        self.arr[x] = min(self.arr[2*x+1], self.arr[2*x+2])

    
    def set(self,i,v):
        self.set2(i,v,0,0,self.size)
    
    def minimum(self,l,r,x,lx,rx):
        
        if lx >= r or l >= rx: return sys.maxsize
        if lx >= l and rx <= r: return self.arr[x]

        m = (lx+rx) // 2

        s1 = self.minimum(l,r,2*x+1, lx, m)
        s2 = self.minimum(l,r,2*x+2, m , rx)
        return min(s1,s2)

    def query(self,l,r):
        return self.minimum(l,r,0,0,self.size)



n,q = map(int,input().split())
arr = list(map(int, input().split()))
st = segmentTree(n)
st.build(arr)

while q >0:
    t,a,b = input().split()

    if t == 'u':
        st.set(int(a)-1, int(b))
    else:
        ans = st.query(int(a)-1, int(b)-1)
        print(ans)
    q -=1
