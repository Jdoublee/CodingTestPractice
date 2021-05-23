from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
	q = deque()
	q.append((s[0],s[1],0))
	visited[s[0]][s[1]] = True
	flag = False
	dist = 1000
	candidates = []
	
	while q:
		x, y, d = q.popleft()
		if dist < d:
			return candidates, dist+1
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] <= body:
				if 0 < graph[nx][ny] < body:
					if not flag:
						dist = d
						flag = True
					
					candidates.append((nx,ny))
				else:
					q.append((nx,ny,d+1))
				visited[nx][ny] = True
	if dist < 1000:
		return candidates, dist+1	
	
	return False, False


n = int(input())
graph = []
shark = (-1,-1)
body = 2
time = 0

for i in range(n):
	graph.append(list(map(int, input().split())))
	if 9 in graph[i]:
		shark = (i,graph[i].index(9))
	
dx = [-1,0,0,1]
dy = [0,-1,1,0]
cnt = 0

while True:
	visited = [[False for _ in range(n)] for _ in range(n)]
	
	cand, d = bfs(shark)
	
	if not cand:
		break
	
	cnt += 1
	
	cand.sort(key=lambda x:(x[0],x[1]))
	x,y = cand[0]
	graph[shark[0]][shark[1]] = 0
	shark = (x,y)
	graph[shark[0]][shark[1]] = 9
	if cnt == body:
		cnt = 0
		body += 1
	time += d
	
print(time)

# 더럽다...
# 구현 문제는 문제를 잘 읽자