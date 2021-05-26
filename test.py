def process(a,s,q):
    n = len(a)
    ans = 0

    for i in range(n):
        if s == 0:
            if a[i] >= q:
                ans +=1
        else:
            if a[i] > q:
                ans +=1
    return ans



    
n = int(input())
a = list(map(int, input().split()))
a.sort()
t = int(input())
while t >0:
    s,q = map(int,input().split())    
    ans = process(a,s,q)
    print(ans)

    t -=1
