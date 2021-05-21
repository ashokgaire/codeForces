class Segment:
    size = 1
    arr = []

    def __init__(self,n):
        while self.size <=n:
            self.size *=2
        self.arr = [0]*(2*self.size)

    def build2(self,a,x,lx,rx):
        if rx - lx == 1:
            if lx > len(a):
                self.arr[x] = a[lx]
            return
        m =(rx + lx) //2
        self.build2(a,2*x+1,lx,m)
        self.build2(a,2*x+2,m,rx)
        self.arr[x] = self.arr[2*x+1] + self.arr[2*x+2] 

    

    def build(self,a):
        self.build2(a,0,0,0,self.size)

    
    def set2(self,i,v,x,lx,rx):
        if rx -lx == 1:
            self.arr[x] = v
            return
        m = (rx+lx) //2

        self.set2(i,v,2*x+1,lx,m)
        self.set2(i,v,2*x+2,m)

    def set(self,i,v):
        self.set2(i,v,0,0,self.size)
    
    def calc2(self,v,lx,rx):
        pass
    def calc(self,v):
        return self.calc2(v,0,self.size)



n , m= map(int, input().split())
a = list(map(int, input().split()))

st = Segment(n)
st.build(a)


while m > 0:
    i , v = map(int, input().split())

    if i == 1:
        st.set(v,1 - a[v])
    else:
        print(st.calc(i,v))
    m -=1