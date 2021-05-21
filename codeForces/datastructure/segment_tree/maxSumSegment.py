class item:
    def __init__(self,seg,pref,suf,sum):
        self.seg = seg
        self.pref = pref
        self.suf = suf
        self.sum = sum

class Segment:
    size = 1
    arr = []
    def __init__(self,n):
        self.n = n
        while self.size <= n:
            self.size *=2
        self.arr = [self.NEUTRAL_ELEMENT]*(2*self.size)
        
    
    
    NEUTRAL_ELEMENT = item(0,0,0,0)

    def single(self,v):
        if v > 0:
            return item(v,v,v,v)
        else:
            return item(0,0,0,v)
    def merge(self,a,b):
        return item(
            max(a.seg, max(b.seg, a.suf+b.pref)),
            max(a.pref, a.sum+b.pref),
            max(b.suf, b.sum + a.suf),
            a.sum + b.sum
        )

    
   
    def build2(self,a,x,lx,rx):
        if rx - lx ==1:
            if lx < len(a):
                self.arr[x] = self.single(a[lx])
            return
        
        m = (lx + rx) // 2
        self.build2(a,2*x+1, lx, m)
        self.build2(a,2*x+2,m,rx)
        
        
        self.arr[x] = self.merge(self.arr[2*x+1], self.arr[2*x+2])
    def build(self,arr):
        self.build2(arr,0,0,self.size)

    
    def set2(self,i,v,x,lx,rx):
        if rx - lx == 1:
            self.arr[x] = self.single(v)
            return

        m = (lx + rx) // 2

        if i < m:
            self.set2(i,v,2*x+1, lx,m)
        else:
            self.set2(i,v,2*x+2,m,rx)

        self.arr[x]  = self.merge(self.arr[2*x+1], self.arr[2*x+2])

    
    def calc2(self,l,r,x,lx,rx):
        if lx >= r or l >= rx: return self.NEUTRAL_ELEMENT
        if lx >= l or r <= rx: return self.arr[x]

        m1 = self.calc2(l,r,2*x+1,lx,m)
        m2 = self.calc2(l,r,2*x+2, m,rx)

        return self.merge(m1,m2)
        


    def calc(self,l,r):
        return self.calc2(l,r,0,0,self.size)

    def set(self,i,v):
        return self.set2(i,v,0,0,self.size)







n , m= map(int, input().split())
a = list(map(int, input().split()))

st = Segment(n)
st.build(a)

print(st.calc(0,n).seg)

while m > 0:
    i , v = map(int, input().split())
    st.set(i,v)
    print(st.calc(0,n).seg)
    m -=1