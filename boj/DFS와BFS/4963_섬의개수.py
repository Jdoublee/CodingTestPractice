import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
	graph[x][y] = 2
	
	for i in range(8):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
			dfs(nx,ny)
	
    
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
			
while True:
	# h * w
	w, h = map(int, input().split())
	ans = 0
	
	if w == 0 and h == 0:
		break
	
	graph = []
	for _ in range(h):
		graph.append(list(map(int, input().split())))
		
	for i in range(h):
		for j in range(w):
			if graph[i][j] == 1:
				dfs(i,j)
				ans += 1

	print(ans)