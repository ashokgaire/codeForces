def binomialCoefficient(n,k, memo = {}):

    if k > n:
        return 0
    if k == 0 or  k == n:
        return 1
    
    key = str(n) + "," + str(k)

    if key in memo:
        return memo[key]
    
    memo[key] = binomialCoefficient(n-1, k-1) + binomialCoefficient(n-1,k)

    return memo[key]


n = 5
k = 2

print(binomialCoefficient(n,k))

    