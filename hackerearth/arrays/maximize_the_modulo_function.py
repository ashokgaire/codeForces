def binpower(a,b,m):
    a %=m
    res = 1
    while b > 0:
        if b & 1:
            res = res*a % m
        a = a*a % m
        b >>= 1
    return res

def solve(s,m,k):
    mod_val = 0
    for i in range(m):
        digit = int(s[i])
        mod_val = (mod_val + (digit*binpower(10,m-i-1,k)%k))%k
    

    prev = 0
    ans = mod_val

    for i in range(m):
        digit = int(s[i])
        mod_val = (mod_val - (digit*binpower(10, m - i - 1,k))%k + k) % k
        ans = max(ans, (prev + mod_val)%k)
        prev = (prev + (digit*binpower(10,m-i-2,k))%k)%k
    return ans


t = int(input())

while t > 0:
    m , k = map(int, input().split())
    s = input()
    print(solve(s,m,k))
    t -=1