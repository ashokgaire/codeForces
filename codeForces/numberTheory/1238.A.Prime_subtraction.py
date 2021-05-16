t = int(input())

while t > 0:
    a,b = map(int , input().split())
    if a- b>1:
        print("YES")
    else:
        print("NO")
    t -=1

