import math

def buildSparseTable(arr,table,n):

    for i in range(n):
        table[i][0] = arr[i]

    j = 1

    while (1 << j) < n:
        for i in range(n):
            table[i][j] = min(table[i][j-1],  table[i + ( 1 << (j -1))][j-1])
     
        j +=1

def Search(L,R,table):
    j = int(math.log2(R-L+1))

    if table[L][j] <= table[R - (1 << j) +1][j]:
        return table[L][j]
    else:
        return table[R - (1 << j) + 1][j]






t = int(input())
arr = list(map(int, input().split()))
n = t
table = [[0 for x in range(n+1)] for x in range(n+1)]

buildSparseTable(arr,table,n)


q = int(input())

while q > 0:

    L,R = map(int, input().split())
    print(Search(L,R,table))


    q -=1
