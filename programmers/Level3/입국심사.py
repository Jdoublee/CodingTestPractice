def solution(n, times):    
    l = 1 # 최소치.
    r = max(times) * n # 최대치. 가장 오래걸리는 심사시간 * 사람 수
    
    # 이분탐색 수행
    while l <= r:
        m = (l+r)//2
        
        # 시간 m 동안 각 입국 심사대가 처리할 수 있는 인원 수가 n보다 작으면 
        if sum([m//time for time in times]) < n:
            l = m + 1 # 범위 늘려서 확인 (값 더 커짐)
        else: # n보다 크거나 같으면
            r = m - 1 # 범위 좁혀서 확인 (최소치에 더 가깝게)    
    
    return l