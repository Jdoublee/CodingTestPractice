from collections import deque
def solution(n, edge):
    graph = {}
    
    for a, b in edge:
        if a in graph.keys():
            graph[a].append(b)
        else:
            graph[a] = [b]
            
        if b in graph.keys():
            graph[b].append(a)
        else:
            graph[b] = [a]
        
    visited = [False] * (n+1)
    distance = [0] * (n+1) # 1번 노드로부터 떨어진 거리 저장
    
    q = deque()
    q.append(1)
    visited[1] = True

    # bfs
    while q:
        now = q.popleft()
        
        for v in graph[now]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
                distance[v] = distance[now] + 1 # 이전 노드까지의 거리 + 1 저장
            
    return distance.count(max(distance)) # 1번 노드로부터 가장 멀리 떨어진 노드 개수 반환