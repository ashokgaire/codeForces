
def gcd(a,b, x , y):
    if b == 0:
        x = 1
        y = 0
        return a

    x1 = 0
    y1 = 1
    d = gcd(b,a%b,x1,y1)

    x= y1
    y = int(x1 - y1 * int(a/b))

    return d

def solution(a,b,c):
    x0 = 1
    y0 = 0
    g =gcd(abs(a), abs(b), x0, y0)

    if c % g:
        return "NO"
    else:
        return "YES"

a,b,c = map(int, input().split())
print(solution(a,b,c))