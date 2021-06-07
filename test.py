import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def ini():
    return(int(input()))
def inl():
    return(list(map(int,input().split())))
def ins():
    s = input()
    return(list(s[:len(s) - 1]))
def inm():
    return(map(int,input().split()))

def p(s):
    print(s)

def pa(s):
    print(" ".join(str(x) for x in s))

def pj(arr):
    print("".join(str(x) for x in  arr))


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
if __name__ == "__main__":

    a = [int(x) for x in input().split()]
    n = len(a)
    table = {}

    for i in range(n):
        for j in range(i+1,n):
            
            table[a[i] + a[j]] = [a[i], a[j]]
    ans = []
    for i in range(n):
        comp = 0 - a[i]
        if comp in table:
            d = sorted([a[i]] + table[comp])
            if d not in ans:
                ans.append(d)
    print(ans)

    
