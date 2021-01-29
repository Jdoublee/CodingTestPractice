#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dic = {}
    
    for mgz in magazine:
        if mgz in dic.keys():
            dic[mgz] += 1
        else:
            dic[mgz] = 1
    
    for n in note:
        if n in dic.keys() and dic[n] > 0:
            dic[n] -= 1
        else:
            print('No')
            return
    
    print('Yes')

    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
