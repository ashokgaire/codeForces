def process(a,b):
     one = [a*x for x in range(1,20)]
     two = [a*b*x for x in range(1,20)]
     three = []

     for i in range(19):
         if one[i] not in three:
             three.append(one[i])
         if two[i] not in three:
             three.append(two[i])

     ans = False
     for j in range(len(three)):
         for i in range(j+1,len(three)):
             for k in range(i+1,len(three)):
                 x = three[j]
                 y = three[i]
                 z = three[k]

                 if ((x % (a*b) == 0) or (y %(a*b) == 0) or (z%(a*b)==0)) and x+y == z:
                     print("YES")
                     print(x,y,z)
                     ans = True
                     break
                 if ans:
                     break
             if ans:
                break
         if ans:
            break
     if not ans:
         print("NO")







t = int(input())

while t > 0:
    a,b = map(int, input().split())
    process(a,b)
    t -=1