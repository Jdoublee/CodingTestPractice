from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []

for _ in range(r):
	graph.append(list(input().rstrip()))

dx = [-1,0,0,1]
dy = [0,-1,1,0]

res = 0
q = set()
q.add((0, 0, graph[0][0]))

while q:
	x,y,check = q.pop()
	res = max(res,len(check))
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in check:
			q.add((nx,ny,check+graph[nx][ny]))

print(res)

# dfs로는 시간초과 계속 나서 bfs로 풀이
# pypy3 25%에서 시간 초과