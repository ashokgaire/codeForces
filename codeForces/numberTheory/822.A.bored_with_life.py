n , m = map(int, input().split())

ans = 1
for i in range(1, min(n,m)+1):
    ans *= i
print(ans)
