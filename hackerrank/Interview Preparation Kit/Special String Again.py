#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    res = len(s)
    
    for i in range(n):
        ss = s[i]
        for j in range(i+1, n):
            ss += s[j]
            first = ss[0]
            if ss.count(first) == len(ss):
                print(ss)
                res += 1
            elif ss.count(first) == len(ss) - 1 and ss[len(ss)//2] != first and len(ss) % 2 == 1:
                print(ss)
                res += 1
            elif ss.count(first) < len(ss) - 1:
                break
                     
    return res
                
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
