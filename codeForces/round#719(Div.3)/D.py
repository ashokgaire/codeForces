

def process(a,n):
    ans = 0

    for i in range(n-1):
        for j in range(i+1,n):
            if a[j]-a[i] == j -i:
                ans +=1

    return ans



t = int(input())

while(t>0):
    n = int(input())
    a = list(map(int, input().split()))
    print(process(a,n))
    t -=1