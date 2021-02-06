from collections import deque

def dfs(graph, v, visited):
	visited[v] = True
	print(v, end=' ')
	
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

def bfs(graph, v, visited):
	queue = deque([v]) # 큐 자료구조 구현 위해 덱 사용 -> 빨라빨라
	visited[v] = True
	
	while queue:
		now = queue.popleft()
		print(now, end=' ')
		for i in graph[now]:
			if not visited[i]:
				visited[i] = True
				queue.append(i)
				
n, m, v = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
	a, b = map(int, input().rstrip().split())
	graph[a].append(b)
	graph[b].append(a)

for g in graph: # 낮은 숫자부터 비교 -> 오름차순 정렬
	g.sort()

dfs(graph, v, visited)

visited = [False] * (n+1) # 방문 배열 다시 초기화
print()

bfs(graph, v, visited)
