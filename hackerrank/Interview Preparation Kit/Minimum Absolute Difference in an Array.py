#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    res = 2000000001 # -10^9 ~ 10^9
    for i in range(len(arr)-1):
        if res == 0:
            break
        dif = arr[i+1] - arr[i]
        res = min(res, abs(dif))
            
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
