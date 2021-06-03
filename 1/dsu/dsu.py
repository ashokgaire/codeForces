def init(arr,size, n):
    for i in range(1, n+1):
        arr[i] = i
        size[i] = 1

# finding root of an element
def root(arr, i):
    while(arr[i] != i):
        arr[i] = arr[arr[i]]
        i = arr[i]
    return i

def find(arr,a,b):
    if root(arr,a) == root(arr,b):
        return True
    else:
        return False

def weightedUnion(arr, size, a, b):
    rootA= root(arr,a)
    rootB= root(arr,b)

    if size[rootA] < size[rootB]:
        arr[rootA] = arr[rootB]
        size[rootB] += size[rootA]
        size[rootA] =0
    
    else:
        arr[rootB] = arr[rootA]
        size[rootA] += size[rootB]
        size[rootB] =0


if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = [None]*(n+1)
    size = [None]*(n+1)
    init(arr,size,n)
    while m >0:
        ans = []
        u , v = map(int,input().split())

        if not find(arr,u,v):
            weightedUnion(arr,size,u,v)
        for i in range(1,len(size)):
            if size[i] != 0:
                ans.append(size[i])
        ans.sort()
        print(" ".join(str(x) for x in ans))
        m -=1


