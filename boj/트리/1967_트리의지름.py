from collections import deque
import sys
input = sys.stdin.readline
INF = float('inf')

def bfs(x):
	q = deque()
	distance = [INF] * (n+1)
	
	distance[0] = -1
	distance[x] = 0
	q.append(x)
	
	while q:
		now = q.popleft()
		
		for v,c in tree[now]:
			if distance[now] + c < distance[v]:
				distance[v] = distance[now] + c
				q.append(v)
	
	return (distance.index(max(distance)), max(distance))	
	

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
	a, b, c = map(int,input().split())
	tree[a].append((b, c))
	tree[b].append((a,c))

idx, _ = bfs(1) # 루트 1에서 가장 먼 노드의 인덱스 찾기
_, res = bfs(idx) # 해당 노드에서 가장 먼 노드 찾기
print(res) # 해당 트리의 지름
