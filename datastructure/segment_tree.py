

class segment:
    size = 1
    sums = []
    def __init__(self,n):
        self.n = n

        while self.size < n:
            self.size *=2
        self.sums = [0]*(2*self.size)
    
    def set2(self,i,v,x,lx,rx):
        if rx - lx == 1:
            self.sums[x] = v
            return
        
        m = (lx+rx) // 2

        if i < m:
            self.set2(i,v,2*x+1, lx, m)
        else:
            self.set2(i,v,2*x+2,m,rx)
        self.sums[x] = self.sums[2*x+1] + self.sums[2*x+2]

    
    def set(self,i,v):
        self.set2(i,v,0,0,self.size)

    def sum2(self,l,r,x,lx,rx):
        if lx >= r or l >=rx: return 0

        if lx >=l and rx <=r : return self.sums[x]

        m = (lx + rx) / 2

        s1 = self.sum2(l,r,2*x+1,lx,m)
        s2 = self.sum2(l,r,2*x+2,m,rx)

        return s1+s2

    def sum(self,l,r):
        return self.sum2(l,r,0,0,self.size)












if __name__ == "__main__":
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    st = segment(n)
    for i in range(n):
        st.set(i,arr[i])

    while m > 0:
        op,i,v = map(int, input().split())

        if op == 1:
            st.set(i,v)
        else:
            print(st.sum(i,v))
        m -=1





