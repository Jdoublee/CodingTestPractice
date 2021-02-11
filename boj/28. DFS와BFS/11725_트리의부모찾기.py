import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
	a, b = map(int, input().split())
	
	graph[a].append(b)
	graph[b].append(a)

visited[1] = 1
queue = deque([1])

while queue:
	now = queue.popleft()
	
	for v in graph[now]:
		if not visited[v]:
			visited[v] = now
			queue.append(v)
			
for i in range(2, n+1):
	print(visited[i])