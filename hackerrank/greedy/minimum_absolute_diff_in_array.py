#!/bin/python3

import math
import os
import random
import re
import sys



def minimumAbsoluteDifference(arr):
    arr.sort()
    print(arr)
    mini = 10**10

    for i in range(len(arr)-1):
        mini = min(mini, abs(arr[i]-arr[i+1]))

    return mini


if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)
