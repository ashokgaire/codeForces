import math


def binpow(a,b):
    if b == 0:
        return 1
    temp = binpow(a,int(b/2))
    if b%2 == 0:
        return  (temp* temp)
    else:
        return  (temp*temp*a)
def fib(n):
    a = binpow((1+math.sqrt(5))/2,n) % 1000000007
    b = binpow((1-math.sqrt(5))/2,n) % 1000000007

    return int((a - b)/math.sqrt(5) %  1000000007)




n = int(input())

print(fib(n))