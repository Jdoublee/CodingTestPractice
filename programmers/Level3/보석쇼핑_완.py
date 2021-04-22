import heapq

def solution(gems):  
    names = len(set(gems))
    
    l = 0
    r = 0
    
    q = []
    
    cnts = {gems[0]:1} # 딕셔너리에 보석 종류와 개수 저장. 0개 되면 del, 1개 이상되면 추가.
    
    while 0 <= l < len(gems) and 0 <= r < len(gems):
        if len(cnts) < names: # 보석 종류 다 없으면 범위 늘려줌
            r += 1
            if r < len(gems): # r이 보석 전체 개수와 같으면 인덱스 에러 발생
                if gems[r] in cnts.keys():
                    cnts[gems[r]] += 1
                else:
                    cnts[gems[r]] = 1
        else: # 보석 종류 다 있으면 범위 좁혀줌
            heapq.heappush(q,(r-l+1,l+1,r+1))
            if cnts[gems[l]] == 1:
                del cnts[gems[l]] # 0개 되면 딕셔너리에서 삭제
            else:
                cnts[gems[l]] -= 1 # 개수--
            l += 1
        
    _,l,r = heapq.heappop(q)
    return [l,r]