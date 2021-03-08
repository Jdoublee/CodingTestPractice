import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
distance = [1e9] * (v+1)

for _ in range(e):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def dijkstra(start):
	q = []
	distance[start] = 0
	heapq.heappush(q, (distance[start], start))
	
	while q:
		d, now = heapq.heappop(q)
		
		if distance[now] < d:
			continue
		
		for v, c in graph[now]:
			cost = d + c
			if cost < distance[v]:
				distance[v] = cost
				heapq.heappush(q, (distance[v], v))

dijkstra(k)

for d in distance[1:]:
	if d == 1e9:
		print('INF')
	else:
		print(d)