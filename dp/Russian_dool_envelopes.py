class dool:
    def __init__(self,h,w):
        self.h = h
        self.w = w
    
    def compare(self,o):
        return self.w - o.w


def envelop(m,n):
    table = [0]*n
    table[0] = [1]

    for i in range(1,n):
        for j in range(0,i):
            if m[i].compare(m[j]):
                table[i] +=1
    print(table)
    

n = int(input())
m = [0]*n

for i in range(n):
    w,h = map(int,input().split())
    m[i] = dool(h,w)
