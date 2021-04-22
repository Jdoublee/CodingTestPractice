import sys
input = sys.stdin.readline

n = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
	tmp = list(map(int,input().split()))
	for j in range(n):
		if tmp[j] == 1:
			graph[i][j] = 1
			
for k in range(n):
	for a in range(n):
		for b in range(n):
			if graph[a][b] == 0 and graph[a][k] == 1 and graph[k][b] == 1:
				graph[a][b] = 1

for g in graph:
	for x in g:
		print(x, end=' ')
	print()