l = [[0 for i in range(30)] for  j in range(30)]

def initliaze():
    l[0][0] = 1

    for i in range(1,30):
        l[i][0] = 1
        for j in range(1,i+1):
            l[i][j] = (l[i-1][j-1] + l[i-1][j])

def nCr(n,r):
    return l[n][r]

initliaze()

n = 2
r = 1
print(nCr(n,r))