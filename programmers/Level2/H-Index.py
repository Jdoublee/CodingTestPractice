def solution(citations):
    answer = 0
    citations.sort()
    print(citations)
    
    li = [0 for _ in range(citations[-1]+1)] # 0 ~ 인용된 횟수 최대값까지의 리스트 만들어줌
    # li = [0] * (citations[-1]+1)
    for c in set(citations):
        li[c] = citations.count(c) # 만들어준 리스트에 해당 인용횟수 count 해서 넣어줌
    
    for c in range(citations[-1]):
        h = c
        hc = sum(li[c:]) # h번 이상 인용된 논문 수
        nhc = sum(li[:c+1]) # h번 이하 인용된 논문 수
        if hc >= h and  h >= nhc : # 문제 조건 만족하는지
            answer = h # if answer<h else answer
    print(li)
    
    
    return answer