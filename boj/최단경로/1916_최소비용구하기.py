import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [1e9] * (n+1)

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b,c))

s, e = map(int, input().split())

# 다익스트라
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

print(distance[e])