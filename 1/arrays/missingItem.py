def getMissingNo(A):
    n = len(A)
    xor1 = A[0]
    xor2 = 1

    for i in range(1,n):
        xor1 = xor1 ^ A[i]

    for i in range(2, n+2):
        xor2 = xor2 ^ i

    return xor1 ^ xor2




A = [1, 2, 4, 5, 6]
miss = getMissingNo(A)
print(miss)