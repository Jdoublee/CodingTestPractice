import heapq

def solution(n, stations, w):
    answer = 0
    
    area = []
    s = 1
    
    for station in stations:
        if s <= station-w-1:
            heapq.heappush(area,(s,station-w-1))
        s = station + w + 1
    
    if s <= n:
        heapq.heappush(area,(s,n))
    
    while area:
        a, b = heapq.heappop(area)
        
        if b-a+1 > 2*w+1:
            a += 2*w+1
            heapq.heappush(area,(a,b))
        answer += 1

    return answer

# 그냥 for문 돌리면 효율성 0점 -> 구간으로 체크