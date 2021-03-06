import sys
from collections import deque

def bfs():
	queue = deque()
	queue.append([0,0,0])
	visited[0][0][0] = 1
	
	dx = [-1, 0, 0, 1]
	dy = [0, -1, 1, 0]

	while queue:
		x, y, z = queue.popleft()
		
		if x == n-1 and y == m-1:
			return visited[x][y][z]
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if 0 <= nx < n and 0 <= ny < m:
				# 벽이 아니고 방문한 적 없음(부수고 or 안부수고 둘 다 가능)
				if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
					queue.append([nx,ny,z])
					visited[nx][ny][z] = visited[x][y][z] + 1
				# 벽이고, 부수고 온 적 없으면
				if graph[nx][ny] == 1 and z == 0:
					queue.append([nx,ny,1])
					visited[nx][ny][1] = visited[x][y][z] + 1
	
	return -1
					

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

graph = []

for _ in range(n):
	graph.append(list(map(int, list(input().rstrip()))))

# 3차원 배열로 부수고/안부수고 나누어 저장
# 0 : 벽 안 부수고 이동, 1: 벽 부수고 이동 거리 저장	
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

print(bfs())