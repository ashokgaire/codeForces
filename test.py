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
    n = ini()

    while n > 0:
        m = ini()
        s = ins()
        count = {'T':0, 'M':0}
        for i in range(m):
            if s[i] == 'T':
                count['T'] +=1
            else:
                count['M'] +=1
        
        if count['T']/ count['M'] == 2.0:
            print("YES")
        else:
            print("No")
        n -=1
        
    
    
