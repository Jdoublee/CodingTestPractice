from collections import deque
m, n, h = map(int, input().split())
# n행 * m열 * h 층 
graph = []
# 고려해야할 좌표 쌍은 6개!
dx = [-1, 0, 0, 1, 0, 0]
dy = [0, -1, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for _ in range(h):
	tmp = []
	for _ in range(n):
		tmp.append(list(map(int, input().rstrip().split())))
	graph.append(tmp)

def check(graph):
	for grap in graph:
		for g in grap:
			if 0 in g:
				return False
	return True
	
queue = deque()
# 순서 잘 생각하기
for i in range(h):
	for j in range(n):
		for k in range(m):
			if graph[i][j][k] == 1:
				queue.append((i,j,k))

while queue:
	x, y, z = queue.popleft()

	for k in range(6):
		nx = x + dx[k]
		ny = y + dy[k]
		nz = z + dz[k]
		if 0 <= nz < m and 0 <= ny < n and 0 <= nx < h and graph[nx][ny][nz] == 0:
			graph[nx][ny][nz] = graph[x][y][z] + 1
			queue.append((nx,ny,nz))

if check(graph):
	res = 0
	for grap in graph:
		for g in grap:
			res = max(res, max(g))
	print(res-1)
else:
	print(-1)