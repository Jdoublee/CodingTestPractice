import sys
import heapq

input = sys.stdin.readline
INF = float('inf') # 무한 값 INF 변수 설정

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b,c))

start, dest = map(int, input().split())

distance = [INF] * (n+1)
record = [[] for _ in range(n+1)] # 경로 저장

def dijkstra(s):
	distance[s] = 0
	q = []
	heapq.heappush(q, (distance[s], s))
	
	while q:
		d, now = heapq.heappop(q)
		
		if distance[now] < d:
			continue
		
		for b, c in graph[now]:
			if distance[b] > d + c:
				distance[b] = d + c
				record[b] = record[now] + [now] # 경로 업데이트
				heapq.heappush(q, (distance[b], b))
	
dijkstra(start)

for i in range(1,n+1):
	record[i].append(i) # 도착지 자기자신 추가

print(distance[dest])
print(len(record[dest]))
for x in record[dest]:
	print(x, end=' ')