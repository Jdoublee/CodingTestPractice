# python3로 돌리면 시간ㄴ초과 -> pypy3는 통과 코드
import sys
import copy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 0
cnt = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

graph = []

for _ in range(n):
	graph.append(list(map(int, input().split())))

while True:
	comp = copy.deepcopy(graph)
	queue = deque()

	for i in range(n):
		for j in range(m):
			if comp[i][j] > 0:
				queue.append([i,j])
				comp[i][j] = 0
				break
		if queue:
			break
	
	if not queue:
		break
	
	while queue:
		x, y = queue.popleft()
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if 0 <= nx < n and 0 <= ny < m and comp[nx][ny] > 0:
				queue.append([nx,ny])
				comp[nx][ny] = 0
	
	cnt += 1
	
	for i in range(n):
		for j in range(m):
			if comp[i][j] > 0:
				ans = cnt
				break
		if ans:
			break
	
	if ans:
		break
	
	tmp = copy.deepcopy(graph)
	
	for i in range(n):
		for j in range(m):
			if graph[i][j] > 0:
				for k in range(4):
					nx = i + dx[k]
					ny = j + dy[k]
					
					if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
						tmp[i][j] -= 1
				if tmp[i][j] < 0:
					tmp[i][j] = 0
	
	graph = copy.deepcopy(tmp)

print(max(ans-1, 0))