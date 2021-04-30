#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(v):
    n = len(v)
    l = len(v[0])
    for i in range(n):
        v[i] = sorted(v[i])
   

    
    for i in range(n-1):
        for j in range(l):
            if (v[i][j] > v[i+1][j]):
                return "NO"
    return "YES"


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)
