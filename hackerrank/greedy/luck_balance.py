#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#


def luckBalance(k, contests):
    n=len(contests)
    important, optional = [], 0

    for x,y in contests:
        if y:
            important.append(x)
        else:
            optional +=x
    important.sort()
    luck = 0
    if(len(important) > k):
        diff = len(important) - k
        luck  += sum(important[diff:]) - sum(important[:diff])
    
    return luck + optional


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)

