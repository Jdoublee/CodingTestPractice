from math import gcd # gcd는 내장함수에 존재한다. lcm은 왜 없을까.

def lcm(a, b):
    return (a * b) // gcd(a, b) # lcm 함수 선언 후 사용

def solution(arr):
    answer = arr[0]
    # 리스트 내 원소들끼리 최소공배수 구해줌
    for a in arr[1:]:
        answer = lcm(answer, a)
    
    return answer