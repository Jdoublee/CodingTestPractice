from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
	graph.append(list(map(int, input().rstrip())))

def bfs(x, y):
	queue = deque()
	queue.append((x,y))
	
	dx = [-1, 0, 0, 1]
	dy = [0, -1, 1, 0]
	
	while queue:
		x, y = queue.popleft()
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
				graph[nx][ny] = graph[x][y] + 1 # 이전 노드에서 현재 노드로 이동 시, (이전 노드 + 1) 값 저장 -> 방문한 칸 수. 시작 노드 1부터.
				queue.append((nx,ny))
# for g in graph:
# 	print(g)
bfs(0,0)
# for g in graph:
# 	print(g)
print(graph[-1][-1])