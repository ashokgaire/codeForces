def catalan(n):
    if n <= 1:
        return 1
    
    cat = [0]*(n+1)
    cat[0] = 1
    cat[1] = 1

    for i in range(2,n+1):
        for j in range(i):
            cat[i] += cat[j]* cat[i-j-1]
    return cat[n]


for i in range(10):
    print(catalan(i), end = " ")