def extendedGCD(a,b):
    if b == 0:
        return a,1,0
    
    g, x1, y1 = extendedGCD(b,a%b)

    x = y1
    y = x1 - (a//b)*y1

    return g,x,y


a, b = 35,15
g, x, y = extendedGCD(a, b)
print(x,y, g)