from collections import deque

def bfs():
	queue = deque()
	
	queue.append([na, nb])
	visited[na][nb] = 1 # 시작 위치 1값 주고 시작(방문 + 첫 칸 의미)
	
	while queue:
		x, y = queue.popleft()
		
		if x == ga and y == gb: # 도착지 도달시 바로 리턴
			return visited[x][y]
		
		for i in range(8):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0: # 범위 내 & 방문 안 한 칸이면
				visited[nx][ny] = visited[x][y] + 1
				queue.append([nx,ny])

	return visited[ga][gb]
		

t = int(input())

# 나이트 이동 가능 방향 8가지
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(t):
	n = int(input())
	na, nb = map(int, input().split()) # 시작
	ga, gb = map(int, input().split()) # 도착
	
	visited = [[0 for _ in range(n)] for _ in range(n)]
	
	print(bfs() - 1) # 첫 칸 1부터 시작해서 최종값에서 1 다시 빼줌