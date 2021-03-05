def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    
    l = 1
    r = distance
    
    while l <= r:
        m = (l+r)//2
        
        before = 0 # 이전 바위 위치
        cnt = 0 # 제거할 바위 개수
        d_min = 1e9
        
        for rock in rocks:
            # 현재 바위와 이전 바위 사이의 거리가 m보다 작다면 현재 바위 제거, cnt++
            if rock - before < m:
                cnt += 1
            else:
                d_min = min(d_min, rock-before) # 아니면 거리 최솟값 업데이트
                before = rock # 현재 바위 이전 바위에 저장
        # 제거한 바위 개수가 주어진 n보다 크면 범위 좁혀서 탐색(최솟값에 가깝게)
        if cnt > n:
            r = m - 1
        # 범위 넓혀서(크게) 탐색
        else:
            l = m + 1
            answer = d_min
        
    return answer