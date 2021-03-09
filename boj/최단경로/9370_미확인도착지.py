import sys
import heapq
# import copy
input = sys.stdin.readline

T = int(input())

def dijkstra(start, dist): # + visited
	dist[start] = 0
	
	q = []
	heapq.heappush(q, (dist[start], start))
	
	while q:
		d, now = heapq.heappop(q)
		
		if dist[now] < d:
			continue
		
		for v, c in graph[now]:
			cost = dist[now] + c
			if cost < dist[v]:
				dist[v] = cost
				# visited[v] = copy.deepcopy(visited[now])
				# visited[v].append(now)
				heapq.heappush(q, (dist[v], v))

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    res = []
    
    graph = [[] for _ in range(n+1)]
    distance = [1e9] * (n+1)
	# visited = [[] for _ in range(n+1)]
    # 각 정점에 도달하기까지의 경로 저장해서 비교하고싶었으나 33퍼에서 실패 :(
    # 모든 도로의 길이에 2씩 곱해주고, g-h 경로만 -1해줘서
    # 최종 최단 경로가 2의 배수인지 아닌지로 해당 경로 지나왔는지 판별
    for _ in range(m):
        a, b, d = map(int, input().split())
        
        if (a == g and b == h) or (a == h and b == g):
            d = 2*d -1 
        else:
            d *= 2
        
        graph[a].append((b, d))
        graph[b].append((a, d))
        
    for _ in range(t):
        x = int(input())
        res.append(x)
	
    dijkstra(s, distance) # + visited
	
    res.sort()
    for i in res:
        if distance[i] % 2 == 1:
		# if g in visited[i] and h in visited[i]:
            print(i, end=' ')	
    print()