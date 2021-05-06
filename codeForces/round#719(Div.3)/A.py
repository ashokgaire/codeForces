


def process(s,n):
    result = {}
    ans = "YES"

    for i in range(n):
        if s[i] not in result.values():
            result[i] = s[i]
        elif s[i] in result.values() and s[i] != s[i-1]:
            ans = "NO"
    return ans






t = int(input())
while(t>0):
    n = int(input())
    s = input()
    print(process(s,n))
    t -=1

