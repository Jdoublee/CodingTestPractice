import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, area):
	graph[x][y] = -1
	area += 1
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
			area = dfs(nx, ny, area)
	
	return area

# m * n
m, n, k = map(int, input().split())
cnt = 0
res = []

graph = [[0 for _ in range(n)] for _ in range(m)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for _ in range(k):
	lx, ly, rx, ry = map(int, input().split())
	
	for x in range(lx, rx):
		for y in range(ly, ry):
			graph[y][x] = 1

for i in range(m):
	for j in range(n):
		if graph[i][j] == 0:
			area = 0
			res.append(dfs(i,j, area))
			cnt += 1

print(cnt)	
res.sort()
for r in res:
	print(r, end=' ')