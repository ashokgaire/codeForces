import math 

def buildSparseTable(arr, n, lookup):
    for i in range(0,n):
        lookup[i][0]  = arr[i]
    
    j = 1

    while 2**j < n:
        i = 0

        while (i + (1 << j) -1) < n:

            if lookup[i][j-1] < lookup[i + (2**(j-1))][j-1]:
                lookup[i][j] = lookup[i][j-1]
            else:
                lookup[i][j] = lookup[i + (2 **(j-1))][j-1]
            i +=1
        j +=1


def query(L,R):
    j = int(math.log2(R-L + 1))

    if lookup[L][j] <= lookup[R - 2**j + 1][j]:
        return lookup[L][j]
    else:
        return lookup[R - (2**j ) + 1][j]
a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(a)
MAX = n
     
    # lookup[i][j] is going to store minimum
    # value in arr[i..j]. Ideally lookup table
    # size should not be fixed and should be
    # determined using n Log n. It is kept
    # constant to keep code simple.
lookup = [[0 for i in range(MAX)]
                 for j in range(MAX)]
buildSparseTable(a,n,lookup)

print(lookup)

print(query(0, 4))
print(query(4, 7))
print(query(7, 8))