def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def process(n):
    if n == 100:
        return 1
    
    e = n
    w = 100 - e
    g = gcd(e,w)
    if g > 1:
        e = e // g
        w = w //g
    if w % e == 0:
        return w//e+1
    return w+e








t = int(input())

while t > 0:
    a = int(input())
    print(process(a))

    t -=1