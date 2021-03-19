import sys
import heapq
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x,y,cnt):
	visited[x][y] = True
	graph[x][y] = cnt
	
	q = deque()
	q.append((x,y))
	
	while q:
		x, y = q.popleft()
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
				visited[nx][ny] = True
				graph[nx][ny] = cnt
				q.append((nx,ny))


def check(x,y):
	now = graph[x][y]
    # 상하좌우 한 방향으로 계속 이동. 끝까지 혹은 다른 섬 발견할때까지
	for i in range(4):
		t = 0
		nx = x + dx[i]
		ny = y + dy[i]
		while 0 <= nx < n and 0 <= ny < m:
			if graph[nx][ny] == 0: # 0 이면 t++ & 좌표 한 방향으로 더 이동하여 while문 반복
				nx += dx[i]
				ny += dy[i]
				t += 1
				continue
			if graph[nx][ny] != now and t > 1: # 현재 섬과 다른 인덱스 & 거리 1보다 크면 heapq에 넣어주고 탈출
				heapq.heappush(q, (t, now, graph[nx][ny]))
			break # 현재 섬과 같은 인덱스 해당될 경우에도 탈출
	

def find(x):
	if parent[x] != x:
		parent[x] = find(parent[x])
	return parent[x]

def union(a,b):
	a = find(a)
	b = find(b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b



n, m = map(int, input().split())
graph = []

for _ in range(n):
	graph.append(list(map(int, input().split())))
# 1. 섬 인덱스 붙여주기 (bfs)
visited = [[False for _ in range(m)] for _ in range(n)] # bfs 이용해서 섬 인덱스 붙여주기 위해 선언

cnt = 0 # 섬 인덱스. 1부터 시작
for i in range(n):
	for j in range(m):
		if graph[i][j] == 1 and not visited[i][j]:
			cnt += 1
			bfs(i,j,cnt)
# 2. 섬과 섬 연결 가능한지 확인 (재귀 이동)
q = []
for i in range(n):
	for j in range(m):
		if graph[i][j] > 0:
			check(i,j)
# 3. 모든 섬을 연결하는 다리 길이의 최솟값 구하기 (union-find MST)
parent = [i for i in range(cnt+1)] 
res = 0	# 다리 길이 저장 변수
while q:
	c, a, b = heapq.heappop(q)
	if find(a) != find(b):
		union(a,b)
		res += c
# 4. 모든 섬 연결했는지 확인
for i in range(2,cnt+1): # 0 제외. 1은 가장 작은 수로 자기 자신 부모 가능하므로 제외.
	if parent[i] < i:
		continue
	else: # 부모가 자신이면 다른 섬과 연결 안 됐다는 뜻
		res = -1
		break
print(res)

# 구현 긴 문제 풀 때는 변수명 잘 확인하고 문제 잘 읽기