#!/bin/python3

import math
import os
import random
import re
import sys



def binpow(a,b,m):
    a = a%m
    res = 1
    while b:
        if b % 2 == 0:
            res = (res*a)%m
        a = (a * a) %m
        b >>= 1 
    return (res%m)

def solve(A, M):
    if A == 0:
        print('YES')
    elif pow(A, (M - 1) // 2, M) == 1:
        print('YES')
    else:
        print('NO')

    
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(a, m)
