import math


t = int(input())

while t > 0:
    
    n = int(input())
    print(n & (n-1)) 
    if (n & (n-1)):
        print("YES")
    else:
        print("NO")
    t -=1
