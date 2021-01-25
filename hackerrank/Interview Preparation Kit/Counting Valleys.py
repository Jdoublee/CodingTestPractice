#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    res = 0
    now = 0
    status = 0 # -1:valley, 0:sea, 1:mountain
    for p in path:
        if p == 'D':
           now -= 1
        else:
            now += 1
        
        if now < 0 and status >= 0 :
            res += 1
            status = -1
        elif now == 0 and status != 0:
            status = 0
        elif now > 0 and status <= 0:
            status = 1
            
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
