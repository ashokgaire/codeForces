import math

def solve(n):
    a = []

    if n <= 2:
        return [0]
    while n % 2 == 0:
        a.append(2)
        n = n // 2

    i = 3
    
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            a.append(i)
            n = n // i
            i -=1
        i +=1
    
    if n > 1:
        a.append(n)   
    return ''.join(str(x) for x in a)
    


n = int(input())
m = str(n)
sum1 = 0
for x in m:
    sum1 +=int(x)

b = solve(n)
sum2 = 0
for x in b:
    sum2 += int(x)

if sum1 == sum2:
    print(1)
else:
    print(0)

