# create min heap and delete item and heapify 

def Heapify(arr,n, i):
    largest = i
    l = 2*i +1
    r = 2*i +2

    if l < n and arr[l] > arr[largest]:
        largest = l
    
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != arr[i]:
        arr[i], arr[largest] = arr[largest], arr[i]
        Heapify(arr,n,largest)

def HeapSort(arr):
    n = len(arr)
    mid = n//2
    for i in range(mid-1,-1,-1):
        Heapify(arr,n,i)
    
    print(arr)
    
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)





# Driver code to test above
arr = [12,11,13,5,6,7]
HeapSort(arr)
print(arr)