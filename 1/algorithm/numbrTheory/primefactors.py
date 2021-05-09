import math
def primeFactor(n):
    while n % 2 == 0:
        print(2, end=" ")
        n = n/2
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i ==0:
            print(i, end=" ")
            n = n / i
    if n > 2:
        print(n)


n = 315
primeFactor(n)
