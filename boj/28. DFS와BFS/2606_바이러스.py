def dfs(graph, v, visited):
	visited[v] = True

	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)
	
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
	a, b = map(int, input().rstrip().split())
	graph[a].append(b)
	graph[b].append(a)

for g in graph:
	g.sort()

dfs(graph, 1, visited)

print(visited.count(True)-1) # bool 타입도 count로 셀 수 있다. 방문한 노드 - 1(시작노드 1 빼줌) 출력.