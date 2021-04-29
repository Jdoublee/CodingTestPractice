import heapq
INF = float('inf')

def dijkstra(graph,n):
    distance = [INF] * (n+1)
    
    distance[1] = 0
    
    q = []
    heapq.heappush(q,(0,1))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for v,c in graph[now]:
            cost = distance[now] + c
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q,(distance[v],v))
    
    return distance
            

def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N+1)]
    
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    distance = dijkstra(graph,N)
    
    for d in distance[1:]:
        if d <= K:
            answer += 1
    
    return answer