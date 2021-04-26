def solution(stones, k):
    res = 0

    l = 1
    r = max(stones)
    
    if len(stones) == 1: # tc1 - 디딤돌 하나면 해당 숫자 반환
        return stones[0]
    
    # 이분탐색
    while l <= r:
        m = (l+r)//2
        
        suc = 0 # 숫자 0인 디딤돌 연달아 세줌 
        sucs = [] # 연속되는 0인 디딤돌 개수 저장

        for s in stones:
            if s < m:
                suc += 1
            else:
                sucs.append(suc)
                suc = 0

        sucs.append(suc)
        
        if max(sucs) < k: # 숫자 0인 연속되는 디딤돌 개수가 한 번에 뛰어넘을 수 있는 k개보다 작으면 오른쪽 범위 확인
            res = m # res update
            l = m+1
        else: # k보다 크면 왼쪽 범위 확인
            r = m-1    
    
    return res