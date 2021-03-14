import heapq
import sys
input = sys.stdin.readline # 이거 안 써줘서 시간초과의 늪에 빠졌다. 범위 잘 보고 해당 문 작성.

def dijkstra(c, graph, distance):		
	q = []
	distance[c] = 0
	heapq.heappush(q, (0, c))
	
	while q:
		dist, now = heapq.heappop(q)
		
		if distance[now] < dist:
			continue
		
		for v, s in graph[now]:
			cost = distance[now] + s
			if cost < distance[v]:
				distance[v] = cost
				heapq.heappush(q, (distance[v], v))
	res = [0, 0]
	for dst in distance:
		if dst < 1e9:
			res[0] += 1
			res[1] = max(res[1], dst)
	print(res[0], res[1])

t = int(input())

for _ in range(t):
	n, d, c = map(int, input().split())
	
	graph = [[] for _ in range(n+1)]
	distance = [1e9] * (n+1)
	
	for _ in range(d):
		a, b, s = map(int, input().split())
		graph[b].append((a, s))
	
	dijkstra(c, graph, distance)
