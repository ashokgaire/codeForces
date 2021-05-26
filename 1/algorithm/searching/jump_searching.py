'''
Time Complexity : O(√n) 
Auxiliary Space : O(1)'''

import math
def jumpSearch(arr,n,x):
    block = int(math.sqrt(n))

    for i in range(0,n,block):
        if arr[i] == x:
            return i
        if arr[i] > x:
            for j in range(i-1, i-block,-1):
                if arr[j] == x:
                    return j
    return -1


arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
x = 55
n = len(arr)

print(jumpSearch(arr,n,x))