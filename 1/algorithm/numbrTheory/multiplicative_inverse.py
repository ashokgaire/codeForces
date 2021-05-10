'''
if m is prime we can use Fermats’s little theorem
else use Extended Euclid Algorithm  

first case:
am-1 ≅ 1 (mod m)

If we multiply both sides with a^-1, we get 

a^-1 ≅ a^m-2 (mod m)
'''


def modInverse(a,m):
    g  = gcd(a,m)
    if g !=1:
        return -1
    
    else:
        print(power(a,m-2,m))

# to compute x^y under modulo m
def power(x,y,m):
    if y == 0:
        return 1
    
    p = power(x,y//2,m)%m
    p = (p*p) %m
    if y%2 == 0:
        return p
    else:
        return ((x*p) % m)

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

a = 3
m = 11
 
# Function call
modInverse(a, m)