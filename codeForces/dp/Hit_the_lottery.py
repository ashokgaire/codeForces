
n = int(input())

a = [100,20,10,5,1]

ans = 0
for i in range(5):
    ans += int(n/a[i])
    n = n%a[i]

print(ans)

