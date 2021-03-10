import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
graphx = [[] for _ in range(n+1)]

distance = [1e9] * (n+1)
distancex = [1e9] * (n+1)

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
	graphx[b].append((a, c)) # 단방향 그래프 역으로 받아서 x까지 가는 경로 구함

def dijkstra(s, graph, distance):
	q = []
	distance[s] = 0
	heapq.heappush(q, (distance[s], s))
	
	while q:
		dist, now = heapq.heappop(q)
		
		if distance[now] < dist:
			continue
		
		for v, c in graph[now]:
			cost = distance[now] + c
			if cost < distance[v]:
				distance[v] = cost
				heapq.heappush(q, (distance[v], v))

dijkstra(x, graph, distance) # x 에서 출발하여 모든 노드까지의 최단 경로
dijkstra(x, graphx, distancex) # 모든 노드에서 출발하여 x까지의 최단 경로

res = [(d1+d2) for d1,d2 in zip(distance[1:], distancex[1:])]

print(max(res))