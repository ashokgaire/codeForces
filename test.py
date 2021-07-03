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


def summ(n):
    res = 0

    while n > 0:
        res += n % 10
        n = n//10
    return res
if __name__ == "__main__":
    t = int(input())

    while t:
        n, s= inm()
        ans = 0

        if summ(n) <= s:
            print(0)
            t -=1
            continue
        
        else:
            pw = 1

            for i in range(1,19):
                digit = (n//pw) % 10
                add = pw * ((10 - digit) % 10)

                n += add

                ans += add

                if summ(n) <= s:
                    break
                pw *= 10
        
        print(ans)





            

        t -=1


