from collections import deque

def solution(n, computers):
    cnt = 0
    
    graph = [[] for _ in range(n)]
    visited = [False] * n
    
    for i in range(n):
        for j in range(n):
            if i == j: # 자기자신도 1로 되어있음
                continue

            if computers[i][j] == 1:
                graph[i].append(j)
    
    queue = deque()
    
    # 모든 컴퓨터 방문할 때까지 반복 -> 중첩 while 문
    while visited.count(True) < n:
        for i in range(n):
            if not visited[i]:
                queue.append(i)
                visited[i] = True # visited True로 바꿔주기!!!!!
                cnt += 1
                break
        # BFS       
        while queue:
            now = queue.popleft()
            
            for i in graph[now]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
    
    
    return cnt