def gcd(a,b):
    if b== 0:
        return a
    else: return gcd(b,a%b)

def build(arr,n):
    table = [[0 for x in range(n+1)] for x in range(n+1)]

    for i in range(n):
        table[i][0] = arr[i]

    j = 1

    while (1 << j) < n:
        for i in range(n):
            table[i][j] = gcd(table[i][j-1],table[(i + ( 1 << j-1)) %n][j-1])

        j +=1
    return table

def Query(table, x):
    pass

    









a = int(input())

arr = list(map(int, input().split()))
table = build(arr, a)
print(table)

print(final(table,a))
t = int(input())

while t > 0:
    b = int(input())
    t -=1