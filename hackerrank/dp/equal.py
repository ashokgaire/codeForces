#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    choices = [5,2,1]
    
    n = len(arr)
    step = 0
    while(max(arr) != min(arr)):
        arr.sort()
        a = arr[n-1] - arr[0]
        for i in range(n-2):
            for j in range(len(choices)):
                if a+choices[j] <= arr[n-2]:
                    arr[i] += choices[j]
                    step +=1
                    break
    print(arr)
    return step





if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)
        print(result)
