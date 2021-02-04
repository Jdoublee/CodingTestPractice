#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    stack = deque() # 덱으로 스택 구현
    brackets = {'{':'}', '[':']', '(':')'}

    for x in s:
        if x in ['{', '[', '(']:
            stack.append(x)
        elif stack: # 스택 빈 경우 고려
            comp = stack.pop()
            if comp in brackets.keys() and brackets[comp] == x:
                continue
            else:
                return 'NO'
        else:
            return 'NO'
                
    if stack:
        return 'NO'
        
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
