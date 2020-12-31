from math import sqrt

def solution(n):
    answer = -1
    
    if int(sqrt(n)) == sqrt(n):
        answer = (int(sqrt(n)) + 1) ** 2
    
    return answer