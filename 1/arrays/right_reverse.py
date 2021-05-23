def rotate(arr,start,end):

    while start < end :

        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1


def rightRotate(arr,k,n):
    d = k % n
    rotate(arr,0,d-1)
    rotate(arr,d,n-1)
    
    rotate(arr,0,n-1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
k = 3

rightRotate(arr, k, n)
print(arr)