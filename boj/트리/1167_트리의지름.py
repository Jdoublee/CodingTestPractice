from collections import deque
import sys
input = sys.stdin.readline
INF = float('inf')

def bfs(x):
	q = deque()
	distance = [INF] * (n+1)
	
	distance[0] = -1
	distance[x] = 0
	q.append(x)
	
	while q:
		now = q.popleft()
		
		for v,c in graph[now]:
			if distance[now] + c < distance[v]:
				distance[v] = distance[now] + c
				q.append(v)
	
	return (distance.index(max(distance)), max(distance))	
	
    
n = int(input())
res = 0

graph = [[] for _ in range(n+1)]

for _ in range(n):
	li = list(map(int, input().split()))[:-1]
	for i in range(1,len(li),2):
		graph[li[0]].append((li[i], li[i+1]))
		
idx, _ = bfs(1)
_, res = bfs(idx)
print(res)		
