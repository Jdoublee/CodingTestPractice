import heapq

def solution(scoville, K):
    
    h = [] # heapq 저장
    # h.heapify(scoville) 로 아래 포문 구현 가능. 히피파이~~
    for s in scoville:
        heapq.heappush(h, s)
    
    cnt = 0
    while True:
        if len(h) < 2: # 원소 하나 남으면 더이상 연산 불가
            return -1
        
        res = heapq.heappop(h) + heapq.heappop(h) * 2
        heapq.heappush(h, res)
        cnt += 1

        if h[0] >= K: # 문제 조건 만족하면 리턴
            return cnt
            
        # 다음과 같은 풀이도 가능
        # s = heapq.heappop(scoville)
        # f = heapq.heappushpop(scoville, f + s + s) # push 후 pop 동작. 시간 더 짧게 걸린다고.
