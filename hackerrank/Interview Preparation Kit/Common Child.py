#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the commonChild function below.
# 5, 9, 10, 11, 12, 13 TLE -> cpp은 모두 통과
def commonChild(s1, s2):
    N = len(s1) + 1
    arr = [[0] * N for _ in range(N)]
    
    for i in range(1, N):
        for j in range(1, N):
            if s1[i-1] == s2[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1  
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    
    return arr[-1][-1]
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
