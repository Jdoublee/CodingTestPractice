import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
	a, b, c = map(int, input().split())
	if graph[a-1][b-1] > 0:
		graph[a-1][b-1] = min(graph[a-1][b-1], c)
	else:
		graph[a-1][b-1] = c

for k in range(n):
	for a in range(n):
		for b in range(n):
			if a == b:
				continue
			if graph[a][k] and graph[k][b]:
				cost = graph[a][k] + graph[k][b]
				if graph[a][b]:
					graph[a][b] = min(graph[a][b], cost)
				else:
					graph[a][b] = cost
			
			
for g in graph:
	for x in g:
		print(x, end=' ')
	print()

# INF 안 쓰고 0으로 편하게 출력하려니 시간이 더 오래 걸린덧