import heapq
    
def solution(jobs):
    answer = 0
    div = len(jobs)
    heapq.heapify(jobs)
    
    def queue(p): # 현재 시간(now) 기준 작업 가능한(도착한) 애들 큐에 넣기
        res = []
        while jobs:
            s, e = heapq.heappop(jobs)
            if s <= p:
                res.append([s, e])
            else:
                heapq.heappush(jobs, [s, e])
                return res
        return res
    
    now = 0
    q = []
    
    while True:
        q.extend(queue(now)) # 새로운 후보 작업들 큐에 추가
        if not q and not jobs: # 후보 없고 jobs 도 없다 -> 다 봤다 -> 종료
            break
        elif not q: # 현재 후보 없으면 시간 + 1 후 다시 후보 찾으러
            now += 1
            continue
        q.sort(key=lambda x:(x[1], x[0]), reverse=True) # 후보 작업들 중 가장 짧은 작업 먼저 처리 위해 정렬. 소요 시간 같다면 제일 최근에(늦게) 도착한 작업 선택.
        s, e = q.pop()
        answer += (now - s) + e # 대기시간 + 소요시간 더해줌
        now += e # 소요시간만큼 현재 시간 ++

    return answer // div # 평균 정수로

# 덱도 언젠가 시도해보기
# 힙을 작업 선택할때도 썼어야할 것 같은데 그것도 나중에 다시