def lcs(x,y,n,m):
    table = [[None]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j ==0:
                table[i][j] = 0
            elif x[i-1] == y[j-1]:
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])
    
    return table[n][m]




X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X,Y, len(X), len(Y)))