def getZarr(string,z):
    n = len(string)

    l,r,k = 0,0,0

    for i in range(1,n):
        if i > r:
            l,r = i,i

            while r<n and string[r-l] == string[r]:
                r +=1
            z[i] = r -l
            r -=1
        
        else:
            k = i-l

            if z[k] < r-i+1:
                z[i] = z[k]

            else:
                l = i
                while r < n and string[r-l] == string[r]:
                    r +=1
                z[i] = r-l
                r -=1
    



def search(txt,pat):
    concat = pat + "$" + text
    l = len(concat)

    z = [0] * l
    getZarr(concat , z)

    for i in range(l):
        if z[i] == len(pat):
            print(i - len(pat) -1)



text = "oxy is oxy"
pattern = "oxy"
search(text, pattern)