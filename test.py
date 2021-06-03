import math

def findMex(c,n):
    mex = 0
    while mex in c:
        mex +=1
        
    return mex

def process(n,c,k):
    while k > 0:
        ma = max(c)
        mex = findMex(c,n)
        a = math.ceil((ma+mex)/2)
        if mex > ma or mex == a:
            return n+k

        elif a in c:
            break 
        else:
            c.add(a)
        k -=1
    return len(c)

t = int(input())

while t > 0:
    n,k = map(int, input().split())
    c = set(map(int, input().split()))

    print(process(n,c,k))
    t -=1
