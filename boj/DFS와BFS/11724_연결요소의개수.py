import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 위 세 줄 없으면 시간초과 발생

n, m = map(int, input().split())
ans = 0

def dfs(s):
	visited[s] = True
	
	for v in graph[s]:
		if not visited[v]:
			dfs(v)

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
	u, v = map(int, input().split())
	
	graph[u].append(v)
	graph[v].append(u)

for i in range(1, n+1):
	if not visited[i]:
		dfs(i)
		ans += 1

print(ans)