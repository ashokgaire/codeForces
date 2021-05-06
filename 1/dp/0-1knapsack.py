def knapSack(val, wt, w, n):
    table = [[0 for _ in range (w+1)] for _ in range (n+1)]

    for i in range(n+1):
        for w in range(w+1):
            if i == 0 or w == 0:
                table[i][w]  = 0
            
            elif wt[i-1] <= w:
                table[i][w] = max(val[i-1]+ table[i-1][w-wt[i-1]], table[i-1][w])
            
            else:
                table[i][w] = table[i-1][w]

    print(table)
    return table[n][w]


val = [60,100,120]
wt = [10,20,30]
w = 50
n = len(val)

print(knapSack(val,wt,w,n))