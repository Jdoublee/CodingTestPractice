import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
	x, y = map(int, input().split())
	
	graph[x].append(y)
	graph[y].append(x)

queue = [a]
visited[a] = True

ans = -1

while queue:
	ans += 1
	if b in queue:
		break
	tmp = []
	
	for q in queue:
		for v in graph[q]:
			if not visited[v]:
				visited[v] = True
				tmp.append(v)
	
	if not tmp:
		ans = -1
	queue = tmp
				
print(ans)
# 트리구조 활용