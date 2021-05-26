import random
def quickSort(arr,l,h):
    if l < h:

        pi = partition(arr,l,h)
        quickSort(arr,l,pi-1)
        quickSort(arr, pi+1,h)

def partition(arr,l,h):
    pivot = arr[h]
    i = l-1

    for j in range(l,h):
        if arr[j] < pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i +1




a = [5,8,1,2,9,3,4,0,6]
n = len(a)
quickSort(a,0,n-1)
print(a)
