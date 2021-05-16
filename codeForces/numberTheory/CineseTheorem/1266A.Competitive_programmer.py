from functools import reduce
def process(n):
    s = list(map(int, n))
    s = reduce(lambda a,b:int(a)+int(b),n)    
    flag = False

    cnt = 0
    zero = 0
    for i in n:
        if i == '0':
            zero +=1
        if int(i) % 2 == 0:
            cnt +=1
    if zero and cnt >=2 and s % 3 == 0:
        flag = True
    else:
        flag = False
    
    print("red" if flag else "cyan")
    

        






t = int(input())

while t > 0:
    n = str(input())
    process(n)

    t -=1