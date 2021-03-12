import heapq
import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# n X m
m, n = map(int, input().split())

graph = []

for _ in range(n):
	graph.append(list(map(int, input().rstrip())))

cnt = 0
visited = [[False for _ in range(m)] for _ in range(n)]
q = []

visited[0][0] = True
heapq.heappush(q, (cnt, 0, 0))

while q:
	cnt, x, y = heapq.heappop(q)
	
	if x == n-1 and y == m-1:
		print(cnt)
		break
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
			visited[nx][ny] = True
			
			if graph[nx][ny] == 0:
				heapq.heappush(q, (cnt, nx, ny))
			else:
				# graph[nx][ny] = 0 # 굳이 안 바꿔줘도 됨
				heapq.heappush(q, (cnt+1, nx, ny)) # 벽이면 뿌시고 cnt++
		
