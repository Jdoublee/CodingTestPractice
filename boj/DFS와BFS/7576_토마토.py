from collections import deque
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
m, n = map(int, input().split())

graph = []
for _ in range(n) :
	graph.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
	for j in range(m) :
		if graph[i][j] == 1 :
			queue.append((i,j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs() :
	while queue :
		x, y = queue.popleft()
		
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			
			if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == -1 :
				continue
			
			if graph[nx][ny] == 0 :
				queue.append((nx,ny))
				graph[nx][ny] = graph[x][y] + 1
			
def solution() :
	bfs()	
	for i in range(n):
		for j in range(m) :
			if graph[i][j] == 0 :
				return -1
	result = 0
	for k in range(n):
	    result = max(result,max(graph[k])) 
	return result - 1
print(solution())
