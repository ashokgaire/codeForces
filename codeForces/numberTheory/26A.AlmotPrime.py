import math
def primeFactors(n):
    a = set()

    while n % 2 == 0:
        a.add(2)
        n = n /2

    for i in range(3, int(math.sqrt(n))+1,2):
        while n % i == 0:
            a.add(int(i))
            n = n / i
    if n > 2:
        a.add(int(n))
    return a


def process(n):
    cnt = 0
    for i in range(1,n+1):
        if len(primeFactors(i)) == 2:
            cnt +=1
    return cnt




n = int(input())
print(process(n))
