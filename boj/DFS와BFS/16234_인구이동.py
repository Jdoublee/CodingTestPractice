from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
	visited = [(x,y)] # 방문 나라 저장
	tot = 0
	
	q = deque()
	q.append((x,y))
	
	while q:
		x,y = q.popleft()
		tot += graph[x][y]
		check[x][y] = True
		
		if y < n-1 and border[x][y] and (x,y+1) not in visited:
			visited.append((x,y+1))
			q.append((x,y+1))

		if y > 0 and border[x][y-1] and (x,y-1) not in visited:
			visited.append((x,y-1))
			q.append((x,y-1))
		
		if x < n-1 and border2[x][y] and (x+1,y) not in visited:
			visited.append((x+1,y))
			q.append((x+1,y))
		
		if x > 0 and border2[x-1][y] and (x-1,y) not in visited:
			visited.append((x-1,y))
			q.append((x-1,y))
	
	return tot, visited


n, l, r = map(int, input().split())

graph = []
cnt = 0

for _ in range(n):
	graph.append(list(map(int, input().split())))

while True:
	border = [[False for _ in range(n-1)] for _ in range(n)] # 같은 행
	border2 = [[False for _ in range(n)] for _ in range(n-1)] # 같은 열

	for i in range(n):
		for j in range(n-1):
			if l <= abs(graph[i][j+1] - graph[i][j]) <= r:
				border[i][j] = True
	
	for j in range(n):
		for i in range(n-1):
			if l <= abs(graph[i+1][j] - graph[i][j]) <= r:
				border2[i][j] = True
	
	check = [[False for _ in range(n)] for _ in range(n)]
	flag = False
	
	for i in range(n):
		for j in range(n):
			if not check[i][j]:
				tot, visited = bfs(i,j)
				
				if len(visited) > 1:
					flag = True
					
					for x,y in visited:
						graph[x][y] = tot//len(visited)
					
	if not flag:
		break
	cnt += 1

print(cnt)
