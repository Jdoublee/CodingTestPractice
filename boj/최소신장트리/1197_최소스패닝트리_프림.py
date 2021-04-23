import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

for _ in range(e):
	a, b, c = map(int, input().split())
	graph[a].append((c, b))
	graph[b].append((c, a))

res = 0
q = []
heapq.heappush(q, (0,1))

while q:
	cost, now = heapq.heappop(q)
	if visited[now]:
		continue
	
	visited[now] = True
	res += cost
	
	for c, node in graph[now]:
		if not visited[node]:
			heapq.heappush(q,(c,node))

print(res)