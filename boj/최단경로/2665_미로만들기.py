import heapq
import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n = int(input())

graph = []

for _ in range(n):
	graph.append(list(map(int, input().rstrip())))

visited = [[False for _ in range(n)] for _ in range(n)] # 비용 대신 방문 여부 저장
q = []
visited[0][0] = True
cnt = 0
heapq.heappush(q, (cnt, 0, 0)) # cnt 기준 정렬

while q:
	cnt, x, y = heapq.heappop(q)
	
	if x == n-1 and y == n-1: # 최종 목적지 도달 시 cnt 출력 및 종료
		print(cnt)
		break
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
			visited[nx][ny] = True
			
			if graph[nx][ny] == 1:
				heapq.heappush(q, (cnt, nx, ny))
			else: # 검은 방인 경우 흰 방으로 바꿔주고 cnt++
				graph[nx][ny] = 0
				heapq.heappush(q, (cnt+1, nx, ny))
