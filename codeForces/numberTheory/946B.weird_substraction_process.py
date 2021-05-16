def process(a,b):
    while a> 0 and b>0:
        if a>= 2*b:
            a = a - 2*b
        elif b >= 2*a:
            b = b - 2 * a
        else:
            return a,b
    return a,b


a,b = map(int, input().split())
while(a != 0 and b != 0 and (a >= 2*b or b >= 2*a)):

    if(a >= 2*b):

        a %= (2*b)
        
    elif(b >= 2*a):
        
        b %= (2*a)
print(a,b)