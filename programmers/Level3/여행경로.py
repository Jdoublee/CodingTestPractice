def solution(tickets):    
    tck = dict()
    
    for t1, t2 in tickets:
        if t1 in tck.keys():
            tck[t1].append(t2)
        else:
            tck[t1] = [t2]
    
    for k in tck.keys():
        tck[k].sort()
    
    st = ['ICN']
    res = []
    
    while st:
        top = st[-1]
        
        if top not in tck.keys() or not tck[top]:
            res.append(st.pop())
        else:
            st.append(tck[top].pop(0))
    
    return res[::-1]


    # 1. { 시작점 : [도착점], ... } 형태의 인접 리스트 그래프 생성
    # 2. ‘도착점’의 리스트 정렬

    # 3. DFS 알고리즘을 사용해 모든 점 순회
    #     3-1. 스택에서 가장 위 데이터(top) 가져옴
    #     3-2-1. 가져온 데이터(top)가 그래프에 없거나, 티켓을 모두 사용한 경우, path에 저장
    #     3-2-2. 아니라면, 가져온 데이터(top)을 시작점으로 하는 도착점 데이터 중 가장 앞 데이터(알파벳순으로 선택해야하므로)를 가져와 stack에 저장
    # 4. path를 역순으로 출력
