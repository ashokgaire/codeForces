
def computeLsp(lsp,pat,M):
    len = 0
    i = 1

    while i < M:
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



def kmp(txt,pat):
    N = len(txt)
    M = len(pat)
    i = 0
    j = 0
    lsp = [0]* M
    computeLsp(lsp,pat, M)
    cnt = 0
    
    while i < N:
        if txt[i] == pat[j] or txt[i] == "?":
            i +=1
            j +=1
        
        if j == M:
            cnt +=1
            j = lsp[j-1]
        elif i < N and txt[i] != '?' and txt[i] != pat[j]:            
            if j != 0:
                j = lsp[j-1]
            else:
                i +=1
    return cnt


s = input()
t = input()
print(kmp(s,t))