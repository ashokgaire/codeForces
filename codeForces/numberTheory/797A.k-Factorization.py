import math

def process(n,k):
    c = n
    d = k
    a = []
    while n % 2 == 0 and k > 1:
        a.append(2)
        n = n//2
        k -=1
    for i in range(3,int(math.sqrt(n))+1, 2):
        while n % i == 0:
            if k > 1:
                a.append(i)
                n = n // i
                k -=1
            else:
                break
    if k and n > 1:
        a.append(n)
    ans = 1
    print(a)

  
    for i in a:
        ans *= i
    if ans == c and len(a) == d:
        print(" ".join(str(x) for x in a))
    else:
        print(-1)
        




n, k = map(int, input().split())
process(n,k)