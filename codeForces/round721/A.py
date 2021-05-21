def process(n):
    if n == 0:
        return 
    if n == 1:
        return 0
    
    j = 1
    k =1

    while (1 << j) < n:
        if k +  (1<< j) < n:
            k += (1 << j)

        j +=1
    return k 

def test(n):
    sum = n
    k  = n-1
    while sum != 0:
        sum &= k
        k -=1
    return k+1
t = int(input())
while t > 0:

    n = int(input())
    print(process(n))
    t -=1