import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
	a, b = map(int, input().split())
	graph[a][b] = 1
	graph[b][a] = 1

for k in range(1,n+1):
	for a in range(1,n+1):
		for b in range(1,n+1):
			if a == b:
				continue
			
			if graph[a][k] and graph[k][b]:
				cost = graph[a][k] + graph[k][b]
				
				if graph[a][b]:
					graph[a][b] = min(graph[a][b], cost) # 원래 값이랑 비교해서 min값 대입
				else:
					graph[a][b] = cost

midx = -1
msum = 1000

for i,g in enumerate(graph):
	if i == 0:
		continue
	if sum(g) < msum:
		midx = i
		msum = sum(g)

print(midx)
