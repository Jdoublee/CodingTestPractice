import heapq
import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def dijkstra():
	distance[0][0] = graph[0][0] # 시작 값 처리 
	q = []
	heapq.heappush(q, (distance[0][0], 0, 0))
	
	while q:
		dist, x, y = heapq.heappop(q)
		
		if distance[x][y] < dist:
			continue
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if 0 <= nx < n and 0 <= ny < n:
				cost = dist + graph[nx][ny] # (x,y) 까지의 최단 거리(비용) + (nx, ny)의 비용
				if cost < distance[nx][ny]:
					distance[nx][ny] = cost
					heapq.heappush(q, (distance[nx][ny], nx, ny))
	
i = 1
while True:
	n = int(input())
	
	if n == 0:
		break
	
	graph = []
	for _ in range(n):
		graph.append(list(map(int, input().split())))
	
	distance = [[1e9 for _ in range(n)] for _ in range(n)]
	
	dijkstra()
	print("Problem {}: {}".format(i,distance[-1][-1]))
	i += 1