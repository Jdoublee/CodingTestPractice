from collections import deque
m, n = map(int, input().split())
# N * M
graph = []

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for _ in range(n):
	graph.append(list(map(int, input().rstrip().split())))
	
queue = deque()

for i in range(n):
	for j in range(m):
		if graph[i][j] == 1: # 익은 토마토 큐에 먼저 넣어줌(시작 노드들)
			queue.append((i,j))

while queue:
	x, y = queue.popleft()

	for k in range(4):
		nx = x + dx[k]
		ny = y + dy[k]
		if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
			graph[nx][ny] = graph[x][y] + 1 # 이동 전 노드 값 + 1 저장
			queue.append((nx,ny))

def check(graph):
	for g in graph:
		if 0 in g: # 안 익은 토마토 남아있으면 -1 리턴
			return False
	return True

if check(graph):
	print(max(map(max, graph))-1) # 최대값에서 1 뺀 값
else:
	print(-1)