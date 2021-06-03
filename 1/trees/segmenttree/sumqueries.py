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
        m = (lx+rx) // 2
        self.build2(a,2*x+1,lx, m)
        self.build2(a,2*x+2, m , rx)

        self.arr[x] = self.arr[2*x+1]+ self.arr[2*x+2]

    
    def build(self,a):
        self.build2(a,0,0,self.size)
    
    def set2(self,i,v,x,lx,rx):
        if rx - lx == 1:
            self.arr[x] = v
            return
        
        m = (lx+rx)//2
        if i < m:
            self.set2(i,v,2*x+1,lx,m)
        else:
            self.set2(i,v,2*x+2,m,rx)
        self.arr[x] =self.arr[2*x+1] + self.arr[2*x+2]


    def set(self,i,v):
        self.set2(i,v,0,0,self.size)
    
    def sum(self,l,r,x,lx,rx):
        if lx >= r or l >= rx: return 0
        if lx >= l and rx <= r: return self.arr[x]

        m = (lx+rx) // 2

        s1 = self.sum(l,r,2*x+1, lx, m)
        s2 = self.sum(l,r,2*x+2, m , rx)
        return s1+s2


    
    def query(self, l , r):
        return self.sum(l,r,0,0,self.size)









# Driver Code
if __name__ == "__main__" :
    
        # Max size of tree
    a = [3,2,1,5,6,8,2,3] 

	# n is global
    n = len(a) 
    st = segmentTree(n)	
    print(st.arr)
