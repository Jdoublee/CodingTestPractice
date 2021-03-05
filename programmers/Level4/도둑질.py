def solution(money):
    # 일열로 나열된 집이 아니라 동그랗게 배치되어 있으므로 첫 집과 마지막 집 동시에 못 터는 것 생각해줘야 함
    # 1) 첫번째 집 털 경우
    fdp = [0] * len(money)
    # 2) 첫번째 집 안 털 경우(마지막 집 털 경우)
    ldp = [0] * len(money)
    
    fdp[0] = money[0]
    fdp[1] = max(fdp[0], money[1])
    
    for i in range(2, len(money)-1): # 마지막 집 범위 제외
        fdp[i] = max(fdp[i-1], fdp[i-2]+money[i])
    
    ldp[0] = 0
    ldp[1] = money[1]
    
    for i in range(2, len(money)): # 마지막 집 범위 포함
        ldp[i] = max(ldp[i-1], ldp[i-2]+money[i])
    
    return max(max(fdp), max(ldp)) # 두 경우 중 최대인 값 반환