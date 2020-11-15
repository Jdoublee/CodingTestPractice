# 완탐 - 문제에서 말하고자 하는 것을 먼저 이해하기
def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow+1): # 1줄부터 시작, yellow 개수만큼(+1) 비교
        if yellow % i != 0:
            continue
        now = yellow/i # i * now = yellow

        if brown == now*2 + i*2 + 4:
            row = 2 + i 
            col = 2+ now
            answer = [row, col]    
            if row < col:
                answer = [col,row]
            break

    return answer