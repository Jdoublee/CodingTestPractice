import sys
input = sys.stdin.readline

def dfs(x):
	if visited[x]:
		return False
	
	visited[x] = True
	
	for v in graph[x]:
		if check[v] < 0 or dfs(check[v]):
			check[v] = x
			return True
	
	return False


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
	info = list(map(int, input().split()))
	graph[i].extend(info[1:])

check = [-1] * (m+1)
cnt = 0

for i in range(1,n+1):
	visited = [False] * (n+1)
	if dfs(i):
		cnt += 1

print(cnt)

# 이분매칭
# 파이썬 시간초과 / 파이파이 통과