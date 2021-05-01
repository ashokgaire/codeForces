#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#
from collections import Counter
def beautifulPairs(A, B):
    ac = Counter(A)
    bc = Counter(B)
    pairs = 0

    for a in ac:
        if a in bc:
            pairs +=min(ac[a], bc[a])

    if pairs == len(A):
        return pairs -1
    else:
        return pairs + 1
    return pairs


if __name__ == '__main__':

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)
    print(result)

