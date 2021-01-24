from itertools import combinations # 조합 완전 꿀
from math import sqrt

def solution(nums):
    answer = 0
        
    li = list(combinations(nums, 3))
    
    for l in li:
        num = sum(l)
        
        flag = False

        for i in range(2, int(sqrt(num)) + 1): # 제곱근까지 소수판별. 에라토스테네스의 체는 바로 기억이 안나네ㅠ
            if num % i == 0:
                flag = True
                break
        if not flag:
            answer += 1
    
    return answer