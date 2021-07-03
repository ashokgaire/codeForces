import random

def quicksort(arr, start, stop):
    if start < stop:
        pivotindex = partitionrand(arr, start, stop)
        quicksort(arr, start, pivotindex -1)
        quicksort(arr, pivotindex+1, stop)

def partitionrand(arr, start, stop):
    randpivot =  random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partition(arr, start, stop):
    pivot = start 
    i = start +1
    for j in range(start+1, stop +1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i+1
    arr[pivot] , arr[i-1] = arr[i-1] , arr[pivot]
    pivot = i-1
    return pivot



n = int(input())
r = n-1
l = -1

a = [int(x) for x in input().split()]

for i in range(1,n):
    if l == -1 and a[i-1] > a[i]:
        l  = i-1
    if l != -1 and r == n-1 and a[i-1] < a[i]:

        r = i-1
if l == -1:
    l = 0
b = sorted(a)
quicksort(a, l, r)
if b== a:
        print("yes")
        print(l+1, r+1)
else:
    print("no")
33333333333333333333333333333