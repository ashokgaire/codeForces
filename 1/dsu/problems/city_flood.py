def init(a,size,n):
    for i in range(1,n+1):
        a[i] = i
        size[i] = 1

def root(arr,i):
    while arr[i] != i:
        arr[i] = arr[arr[i]]
        i = arr[i]
    return i

def find(arr,a,b):
    return root(arr,a) == root(arr,b)

def union(arr,size,a,b):
    rootA = root(arr,a)
    rootB = root(arr,b)
    if rootA == rootB:
        return 

    if size[rootA] < size[rootB]:
        arr[rootA] = arr[rootB]
        size[rootB] += size[rootA]
    else:
        arr[rootB] = arr[rootA]
        size[rootA] += size[rootB]
n = int(input())
a = [None] * (n+1)
size = [None] * (n+1)
init(a,size,n)
t = int(input())
while t >0:
    x,y = map(int,input().split())
    
    union(a,size,x,y)
    t -=1
ans  = 0
for i in range(1,n+1):
    if root(a,a[i]) == i:
        ans +=1

print(ans)