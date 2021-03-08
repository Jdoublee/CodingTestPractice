import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 1 -> 모든 노드 거리 저장
distance = [1e9] * (n+1)
# v1 -> 모든 노드 거리 저장
distance1 = [1e9] * (n+1)
# v2 -> 모든 노드 거리 저장
distance2 = [1e9] * (n+1)

for _ in range(e):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
	graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 기존 다익스트라 + 최단 거리 테이블 인자로 받아줌
def dijkstra(start, dist):
	dist[start] = 0
	q = []
	heapq.heappush(q, (dist[start], start))
	
	while q:
		d, now = heapq.heappop(q)
		
		if dist[now] < d:
			continue
		
		for v, c in graph[now]:
			cost = dist[now] + c
			if cost < dist[v]:
				dist[v] = cost
				heapq.heappush(q, (dist[v], v))
# 다익스트라 3번 시행
# 1 -> v1 / v2 구하기 위해
dijkstra(1, distance)
# v1 -> v2 / N 구하기 위해
dijkstra(v1, distance1)
# v2 -> v1 / N 구하기 위해
dijkstra(v2, distance2)

# 1 -> v1 -> v2 -> N 과 1 -> v2 -> v1 -> N 중 최단거리 res에 저장
res = min(distance[v1]+distance1[v2]+distance2[n], distance[v2]+distance2[v1]+distance1[n])

# res가 1e9 보다 크거나 같으면 가능한 경로 없다는 의미로 -1 저장.
# res == 1e9로 두면 안 된다 -> 각각의 경로가 불가능한, 신장 트리가 아닌 경우 존재(90~100% TC)
if res >= 1e9:
	res = -1
	
print(res)
