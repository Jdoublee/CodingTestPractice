#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):    
    arr.sort()
    
    res = 2000000001 # 최대 10^9
    
    for i in range(len(arr)-k+1):
        res = min(res, arr[i+k-1] - arr[i]) # 굳이 max, min 연산 또 안해줘도 됨. 정렬되어 있으므로 범위 내 제일 앞 인덱스가 최소, 제일 뒤 인덱스가 최대.
        
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
