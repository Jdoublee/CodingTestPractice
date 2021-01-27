#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    
    impc = [c[0] for c in contests if c[1] == 1]
    unimpc = [c[0] for c in contests if c[1] == 0]
    
    impc.sort(reverse=True)
    
    res = sum(impc[:k]) - sum(impc[k:])
    res += sum(unimpc)
    
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
