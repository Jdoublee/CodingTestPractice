import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def dfs(x, y, num):
	comp[x][y] = -1
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= nx < n and 0 <= ny < n and comp[nx][ny] > num:
			dfs(nx,ny,num)


n = int(input())
ans = 1

graph = []

for _ in range(n):
	graph.append(list(map(int, input().split())))

maxn = max(map(max, graph))
minn = min(map(min, graph))

for num in range(minn, maxn):
	comp = copy.deepcopy(graph) # 깊은 복사!!
	cnt = 0
	
	for i in range(n):
		for j in range(n):
			if comp[i][j] > num:
				dfs(i,j,num)
				cnt += 1
	ans = max(ans, cnt)

print(ans)