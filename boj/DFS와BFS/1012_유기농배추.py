# 재귀 깊이 늘려주기
# 런타임 에러 발생 :( 해결
import sys
sys.setrecursionlimit(10000)

t = int(input())
# M (가로) * N (세로)
for _ in range(t):
	m, n, k = map(int, input().split())
	cnt = 0
	
	graph = [[0 for _ in range(m)] for _ in range(n)]
	
	for _ in range(k):
		a, b = map(int, input().split())
		graph[b][a] = 1
	
	def dfs(x, y):
		graph[x][y] = -1
		dx = [-1, 0, 0, 1]
		dy = [0, -1, 1, 0]
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
				dfs(nx, ny)
	
		
	for i in range(n):
		for j in range(m):
			if graph[i][j] == 1:
				dfs(i, j)
				cnt += 1
	
	print(cnt)