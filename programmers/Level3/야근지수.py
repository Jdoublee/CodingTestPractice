import heapq

def solution(n, works):
    h = [-x for x in works]
    
    heapq.heapify(h)
    
    for _ in range(n):
        tmp = heapq.heappop(h)
        if tmp == 0:
            return 0
        heapq.heappush(h, tmp+1)
            
    return sum([x**2 for x in h])