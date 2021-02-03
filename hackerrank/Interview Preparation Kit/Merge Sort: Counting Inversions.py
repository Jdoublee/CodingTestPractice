# 11, 12, 13 TLE -> pypy3 모두 통과

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    class Context: # countInversions 내에 cnt 선언하면 할당 안됐다고 에러남
        cnt = 0
    
    def merge(arr, l, m, r):
        i = l
        j = m+1
        sortedarr = []
        
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                sortedarr.append(arr[i])
                i += 1
            else:
                sortedarr.append(arr[j])
                j += 1
                Context.cnt += m - i + 1
        
        while i <= m:
            sortedarr.append(arr[i])
            i += 1
        
        while j <= r:
            sortedarr.append(arr[j])
            j += 1
        
        for idx in range(l, r+1):
            arr[idx] = sortedarr[idx-l]
    

    def mergesort(arr, l, r):
        if l < r :
            m = (l + r) // 2
            mergesort(arr, l , m)
            mergesort(arr, m+1, r)
            merge(arr, l, m, r)
            
    mergesort(arr, 0, len(arr)-1)
    
    return Context.cnt
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
