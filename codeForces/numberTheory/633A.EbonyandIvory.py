def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)


a,b,c = map(int, input().split())

if c % gcd(a,b) == 0:
    k = 0
    while a*k <=c:
        if ((c -a) * k )%b == 0:
            print("YES")
            break
        k +=1
else:
    print("NO")