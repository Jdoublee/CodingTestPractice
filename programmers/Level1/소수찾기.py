from math import sqrt
def solution(n):
    answer = 0
    flag = -1
    for i in range(2, n+1) :
        for j in range(2, int(sqrt(i))+1) :
            if i%j == 0 :
                flag = 0
                break
        if flag != 0 :
            answer += 1
        flag = -1
    return answer