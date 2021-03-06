import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def dfs(x, y, s):
	if s in 'zZ': # 두번째 포문, 적록색약인 경우 z or Z
		graph[x][y] = 'A'
	elif s == 'B':
		graph[x][y] = 'Z'
	else: # R or G (적록색약은 같은 색상으로 처리)
		graph[x][y] = 'z'
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == s:
			dfs(nx,ny,s)

n = int(input())
cnt = [0, 0]

graph = []

for _ in range(n):
	graph.append(list(input().rstrip()))

for i in range(n):
	for j in range(n):
		if graph[i][j] in 'RGB':
			dfs(i,j,graph[i][j])
			cnt[0] += 1

for i in range(n):
	for j in range(n):
		if graph[i][j] in 'zZ':
			dfs(i,j,graph[i][j])
			cnt[1] += 1

print(cnt[0], cnt[1])