

import math
import os
import random
import re
import sys


def fibonacciModified(t1, t2, n):
    newarr = [0]*n
    newarr[0] = t1
    newarr[1] = t2
    for i in range(2,n):
        newarr[i] = newarr[i-2] + newarr[i-1]**2
    
    return newarr[n-1]
        

if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1,t2, n)
    print(result)
