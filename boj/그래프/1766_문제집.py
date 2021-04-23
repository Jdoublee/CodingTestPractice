from collections import deque
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1

q = []
order = 0

for i in range(1,n+1):
	if indegree[i] == 0:
		heapq.heappush(q,(order, i))
		order += 1

res = []

while q:
	od, now = heapq.heappop(q)
	res.append(now)
	
	for i in graph[now]:
		indegree[i] -= 1
		if indegree[i] == 0:
			heapq.heappush(q,(od,i))

for i in res:
	print(i, end=' ')