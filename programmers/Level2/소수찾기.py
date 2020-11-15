# 순열 사용법이 문제였다
from math import sqrt
from itertools import permutations # 이 라이브러리 알아두기이

def isprime(n):
    if n<2:
        return False
    for i in range(2, int(sqrt(n))+1):
    	if n%i==0:
    		return False
    return True

def solution(numbers):
    answer = 0
    li = []

    for k in range(1, len(numbers)+1): # 1개부터 총개수 만큼 뽑아야 함
        pm = list(map(''.join, permutations(numbers, k))) # 순열 함수 사용. 이 구문 알아두기***
        pm = list(set(list(map(int, pm))))
        for n in pm:
            # print(n)
            if isprime(n):
                print(n)
                li.append(n)
    
    answer = len(set(li)) # 위에서 set해줬는데도 중복이 남아있는 경우 있어서 마지막으로 set으로 중복 제거
    return answer