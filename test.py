

def mergeSort(arr,n):
    temparr = [0]* n
    return _mergeSort(arr, temparr, 0 , n-1)

def _mergeSort(arr, temparr, left, right):
    invcount = 0
    if left < right:
        mid = (left+right) // 2

        invcount += _mergeSort(arr, temparr, left, mid)
        invcount += _mergeSort(arr, temparr, mid+1, right)
        invcount += merge(arr, temparr, left, mid, right)

    return invcount

def merge(arr, temparr, left, mid, right):
    i = left
    j = mid+1
    k = left
    invcount = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temparr[k] = arr[i]
            i +=1
            k +=1
        
        else:
            temparr[k] = arr[j]
            invcount += mid -i +1
            k +=1
            j +=1
    
    while i <= mid:
        temparr[k] =arr[i]
        k +=1
        i +=1
    
    while j <= right:
        temparr[k] = arr[j]
        j +=1
        k +=1
    
    for loop_var in range(left, right+1):
        arr[loop_var] = temparr[loop_var]
    
    return invcount

        


n = int(input())

a = list(map(int, input().split()))


    
print(mergeSort(a,n))
print(a)