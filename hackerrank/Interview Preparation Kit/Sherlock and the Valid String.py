#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    dic = {}
    
    for x in s:
        if x in dic.keys():
            dic[x] += 1
        else:
            dic[x] = 1
    
    comp = list(dic.values())[0]

    if list(dic.values()).count(comp) == len(list(dic.values())):
        return 'YES'
    elif list(dic.values()).count(comp) == len(list(dic.values())) - 1 and list(dic.values()).count(comp+1) == 1:
        return 'YES'
    elif list(dic.values()).count(comp) == len(list(dic.values())) - 1 and list(dic.values()).count(1) == 1:
        return 'YES' 
    else:
        return 'NO'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
