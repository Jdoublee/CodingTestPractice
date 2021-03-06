# def solution(w,h):
#     answer = 0
    
#     for i in range(1, w):
#         answer += (h * i) // w # 테케 12번 시간초과 남
    
#     return answer * 2

# 동일 코드 C++로 하면 시간 초과따위 안 남^^
# 최대공약수로 어쩌구 저쩌구 풀라는데 내일 해보겠음

import math

def solution(w,h):

    answer = w * h - (w + h - math.gcd(w,h)) # 최대공약수 내장함수도 있다. 최소공배수는 math.lcm
    
    return answer

# 규칙이 왜 이런가

# 최소로 잡히는 직사각형의 너비와 높이는 전체 직사각형의 너비와 높이에 영향을 받는다.
# 그리고 예제에서는 8 * 12 직사각형에서 2 * 3 이 도출되었다.
# 그렇다, GCD(최대공약수)를 통해서 구할 수 있다.

# 직사각형 개수를 구했다면, 직사각형에서 대각선이 통과하는 블럭만 걸러내야 한다.
# 대각선이 통과하는 블럭의 개수는 최단거리 이동에 필요한 블럭 개수와 동일하다.
# 단! 최단거리 이동과 다른점은 시작점까지 더해줘야 하기 때문에 +1이 포함된다.

# 너비와 높이에서 각각 1을 뺀 값들을 서로 더해서 최단거리를 구하고 여기에 1을 더한다.
# (2-1) + (3-1) + 1 = 4 로 대각선을 지나는 블럭의 개수가 구해진다.

# (8 * 12) - ((2-1) + (3-1) + 1) * 4
# = (w * h) - ((w/gcd - 1) + (h/gcd - 1) + 1) * gcd
# = (w * h) - (w + h - gcd)

# 출처 : https://hyeon9mak.github.io/python/Python-프로그래머스-멀쩡한_사각형
# 라고 한다