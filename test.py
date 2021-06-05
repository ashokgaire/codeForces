def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


if __name__ == "__main__":
    t = int(input())

    while t >0:
        n = int(input())
        a = [int(x) for x in input().split()]
        if n > 2:
            a[0], a[n-2] = a[n-2], a[0]
        print(a)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if gcd(a[i], 2*a[j]) > 1:
                    ans +=1
        print(ans)


        t -=1
