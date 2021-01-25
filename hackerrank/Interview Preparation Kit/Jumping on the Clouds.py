#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    res = 0
    idx = 0
    
    while idx < len(c) - 2:            
        if c[idx+1] == 0:
            if c[idx+2] == 0:
                idx += 2
                res += 1
            else:
                idx += 1
                res += 1
        else:
            idx += 2
            res += 1
    
    if idx < len(c) - 1:
        res += 1
    
    return res

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
