#!/bin/python3

import math
import os
import random
import re
import sys

t_mod = 1000000007

def multiply(mat1, mat2):
    return [((mat1[0]*mat2[0])+(mat1[1]*mat2[2])) % t_mod, ((mat1[0]*mat2[1])+(mat1[1]*mat2[3])) % t_mod,
            ((mat1[2]*mat2[0])+(mat1[3]*mat2[2])) % t_mod, ((mat1[2]*mat2[1])+(mat1[3]*mat2[3])) % t_mod]

def solve(mat, n):
    i_m = [1,1,1,0]
    while n:
        if n & 1:
            i_m = multiply(i_m,mat)
        mat = multiply(mat, mat)
        n >>= 1
    return i_m
if __name__ == '__main__':
 

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        n = int(first_multiple_input[2])
        mat = [1,1,1,0]

        result = solve(mat,n-1)
        print((result[2]*b + result[3]*a) % t_mod)
