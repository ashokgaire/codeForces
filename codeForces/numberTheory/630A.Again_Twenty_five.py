def binpow(a,b,m):
    a %= m

    res = 1
    while b:
        if b % 2 == 0:
            res = (res*a ) % m
        a = (a*a) % m
        b -=1
    return res


n= int(input())

print(str(binpow(5,n,100))[-2:])

