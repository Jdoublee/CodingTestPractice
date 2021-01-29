#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    res = 0
    dic = {}
    
    for x in a:
        if x in dic.keys():
            dic[x] += 1
        else:
            dic[x] = 1
    
    for x in b:
        if x in dic.keys():
            dic[x] -= 1
            if dic[x] == 0:
                del dic[x]
        else:
            res += 1
    
    if dic:
        for v in dic.values():
            res += v         
            
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
