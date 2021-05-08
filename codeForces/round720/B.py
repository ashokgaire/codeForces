def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def process(a,n):
    count = 0
    arr = []
    t = 2
    while t > 0:

        for i in range(1,n):
            if gcd(a[i-1],a[i]) !=1:
                count +=1
                if a[i-1] % 2 == 0:
                    temp = a[i-1]
                    a[i-1] +=1
                    a[n-1] = min(temp, a[i-1])
                    arr.append(i)
                    arr.append(n)
                    arr.append(a[i-1])
                    arr.append(a[n-1])
                else:
                    temp = a[i-1]
                    a[i-1] += 2
                    a[n-1] = min(temp, a[i-1])
                    arr.append(i)
                    arr.append(n)
                    arr.append(a[i - 1])
                    arr.append(a[n - 1])
        t -=1
    print(count)
    if count > 0:
        i = 3
        while i <= len(arr):
            print(arr[i-3], arr[i-2], arr[i-1], arr[i])
            i += 4



t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    process(a,n)
    t -=1

