from math import sqrt

def solution(n):
    
    res = []
    for i in range(1, int(sqrt(n))+1): # 제곱근까지
        if n % i == 0:
            res.append(i)
            res.append(n//i)
    
    return (sum(list(set(res)))) # 5*5 = 25 같은 경우 존재 -> set으로 중복 제거
