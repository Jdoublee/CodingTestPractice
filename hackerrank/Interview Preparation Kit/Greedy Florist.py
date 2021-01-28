#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    res = 0
    
    c.sort(reverse=True)

    kcnt = k
    mul = 1

    for x in c:
        if kcnt == 0:
            kcnt = k
            mul += 1

        res += mul * x

        kcnt -= 1

    return res
             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
