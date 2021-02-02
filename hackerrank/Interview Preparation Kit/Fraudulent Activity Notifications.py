#!/bin/python3

import math
import os
import random
import re
import sys
# import statistics # 내장 함수 median 사용 가능 

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    def findMedian(arr):
        cnt = 0
        m = 0 
        flag = False

        if d % 2 == 0:
            for i in range(len(counter)):
                cnt += counter[i]
                
                if not flag and cnt >= d//2:
                    m = i
                    flag = True
                if cnt >= d//2 + 1:
                    m += i
                    break 
            m /= 2

        else:
            for i in range(len(counter)):
                cnt += counter[i]
                if cnt > d//2:
                    m = i
                    break
                        
        return m # 오 타 조 심 
                    
    res = 0
    counter = [0] * 201
    # 계수 정렬 (counting sort) 안 썼더니 TLE 발생 -> 시간복잡도 O(n)!!!
    for i in range(d):
        counter[expenditure[i]] += 1
    
    for i in range(d, len(expenditure)):
        last = expenditure[i-d]
        new = expenditure[i]
        
        m = findMedian(counter)
        
        if new >= m*2:
            res += 1
        
        counter[last] -= 1
        counter[new] += 1
   
    return res        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
