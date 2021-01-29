#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    if len(s1) < len(s2): # 사이즈 큰게 s1, 사이즈 작은게 s2
        s1, s2 = s2, s1
    
    for s in s2: # 사이즈 작은 문자열 개수만큼 비교 동작
        if s in s1: 
            return 'YES'
    
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
