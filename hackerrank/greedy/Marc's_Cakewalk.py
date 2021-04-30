#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    result = 0
    calorie.sort(reverse=True)

    for i in range(len(calorie)):
        result += 2**i*calorie[i]
        print(result)
    return result


if __name__ == '__main__':

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)
    print(result)
