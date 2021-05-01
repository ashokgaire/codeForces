#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    i = 0
    print(max(arr))

    while(k):
        if(i > len(arr)-1):
            break
        b = max(arr[i:])
        si = i
        for j in range(i,len(arr)):
            if b == arr[j]:
                si = j
        arr[i],arr[si] = arr[si], arr[i]

        i +=1

        k -=1
    


    return arr 
    

if __name__ == '__main__':
    fptr = open('a.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()