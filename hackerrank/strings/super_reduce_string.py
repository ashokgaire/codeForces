def process(n):

    if n == 0:return -1

    a = list(map(int,str(n)))
    org = int(n)
    su = sum(a)

    if su % 2 == 0 and org % 2 != 0:
        return org
    
    else:
        newsu = 0
        while 



    



t = int(input())

while t > 0:
    n = int(input())
    s = int(input())

    print(process(s))


    t -=1