def computeLsp(pat,lsp,n):
    len = 0
    i = 1

    while i < n:
        if pat[i] == pat[len]:
            len +=1
            lsp[i] = len
            i +=1
        else:
            if len !=0:
                len = lsp[len -1]
            else:
                lsp[i] = 0
                i +=1



s = input()
n = len(s)
lsp = [0]*n
computeLsp(s,lsp,n)
print(lsp)