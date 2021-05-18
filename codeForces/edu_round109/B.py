def sorts(a,l,r):
    for i in range(l,r):
        for j in range(i,r):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i] 
    return a

def process(a,n):
    cnt = 0

    left = 0
    right = 1

    while right<=n-1:
        if a[left] > a[right]:
            while right <= n-1 and a[left] > a[right]:
                right +=1
            print(sorts(a,left,right))
            
            cnt +=1
            left = right
            right += 1 

        else:
            left +=1
            right +=1

    return cnt







t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    print(process(a,n))

    t -=1