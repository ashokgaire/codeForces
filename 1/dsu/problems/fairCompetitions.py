def init(arr,size,n):
    for i in range(1,n+1):
        arr[i] = i
        size[i] = 1

def root(arr, a):

    while arr[a] != a:
        arr[a] = arr[arr[a]]
        a = arr[a]
    return a

def find(arr,a,b):
    return root(arr,a) == root(arr,b)


def union(arr,size,a,b):
    rootA = root(arr,a)
    rootB = root(arr,b)

    if size[rootA] < size[rootB]:
        arr[rootA] = arr[rootB]
        size[rootB] += size[rootA]
        
    else:
        arr[rootB] = arr[rootA]
        size[rootA] += size[rootB]
        







    
t = int(input())
while t >0:
    n,m = map(int,input().split())
    arr = [None]*(n+1)
    size = [None]*(n+1)
    init(arr,size,n)
    while m  > 0:
        a,b = map(int,input().split())
        if not find(arr,a,b):
            union(arr,size,a,b)
        

        m -=1
    
    print(arr)
    t -=1
