def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def process(a,n):
    i = 1
    cnt = 0
    aa = []
    while i < n:
        if gcd(a[i], a[i-1]) != 1:
            cnt +=1
            temp = a[i-1]
            if a[i-1] % 2 == 0:
                a[i-1] +=1
                a[n-1] = temp
                aa.append([i,n,a[i-1],a[n-1]])
            else:
                a[i-1] += 2
                a[n-1] = temp
                aa.append([i,n,a[i-1], a[n-1]]) 
        i +=1
    print(cnt)
    if cnt > 0:
        for i in range(len(aa)):
            print(" ".join(str(x) for x in aa[i]))
    
t  = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    process(a,n)


    t -=1