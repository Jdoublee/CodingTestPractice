import sys
input = sys.stdin.readline

def dfs(i):
	if visited[i]: # 해당 소 이미 처리했다면 축사 탐색 실패
		return False
	
	visited[i] = True
	
	for x in graph[i]: # 해당 소 희망 축사 리스트
		if stable[x] < 0 or dfs(stable[x]): # 축사 비어있거나 원래(차지했던) 소가 다른 축사 이용 가능하면
			stable[x] = i # 축사 사용 처리 후 리턴
			return True

	return False


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
	info = list(map(int, input().split()))
	
	for x in info[1:]:
		graph[i].append(x)

cnt = 0
stable = [-1] * (m+1) # 축사

for i in range(1,n+1):
	visited = [False] * (n+1) # 소
	if dfs(i):
		cnt += 1

print(cnt)

# 이분매칭 : 소(n) -> 축사(m)
