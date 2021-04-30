#!/bin/python3

import math
import os
import random
import re
import sys


def getWays(n, c):
    numways = [1]+ [0]*n
    for coin in c:
        for i in range(coin,n+1):
            numways[i] += numways[i-coin]

    print(numways)
    return numways[n]

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    
