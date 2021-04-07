# 벨만-포드 알고리즘
import sys
input = sys.stdin.readline

INF = float('inf') # 이거때문에 고생했다-_ㅠ. 1e9 대입 대신 이 문장을 쓰자. 60퍼에서 자꾸 틀린 이유.

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b,c))

times = [INF] * (n+1)
times[1] = 0

for _ in range(n-1):
	for a in range(1,n+1):
		for b, c in graph[a]:
			if times[b] > times[a] + c:
				times[b] = times[a] + c
# 시간을 무한히 오래 전으로 되돌릴 수 있다면
# -> 음수 사이클 찾기
for a in range(1,n+1):
	for b, c in graph[a]:
		if times[b] > times[a] + c:
			print(-1)
			quit()

for time in times[2:]:
	if time < 1e9:
		print(time)
	else:
		print(-1)
