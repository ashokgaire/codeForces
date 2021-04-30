#!/bin/python3

import math
import os
import random
import re
import sys
from math import ceil, log2;

def getMid(s,e):
    return s + (e-s) // 2

def getSumUtil(st, ss, se, qs, qe, si):
    if(qs <= qs and qe >=se):
        return st[si]
    
    if( se < qs or ss > qe):
        return 0
    
    mid = getMid(ss, se)
    return getSumUtil(st, ss, mid, qs, qe, 2*si+1) + getSumUtil(st, mid+1, se, qs, qe, 2*si+2)

def getSum(st, n, qs, qe):
    if(qs < 0 or qe > n -1 or qs > qe):
        return -1
    return getSumUtil(st, 0 , n-1, qs, qe, 0)

def constructSTUtil(arr, ss, se, st, si):
    if(ss == se):
        st[si] = arr[ss]
        return arr[ss]

    mid = getMid(ss, se)

    st[si] = constructSTUtil(arr, ss, mid, st, si*2 + 1) + constructSTUtil(arr, mid+1, se, st, si*2+2)
    return st[si]

def constructST(arr, n):
    x = (int) (ceil(log2(n)))

    max_size = 2 * (int) (2**x) -1

    st = [0] * max_size

    constructSTUtil(arr, 0 , n-1, st, 0)

    return st



if __name__ == '__main__':
   
    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    n = len(numbers)
    st = constructST(numbers, n)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    getSum(st,n,1,3)

   
