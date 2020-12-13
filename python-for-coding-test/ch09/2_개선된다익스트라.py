import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결된 노드 정보
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 무한대 값으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력받음
for _ in range(m) :
    # a번 노드에서 b번 노드로 가는 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# get_smallest_node() 정의 안 함

def dijkstra(start) :
    q = []
    # 시작 노드 최단 경로 0 설정, 큐에 삽입
    heapq.heappush(q, (0, start)) # (거리, 노드)
    distance[start] = 0

    while q :
        # 최단 거리 가장 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있으면 무시
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 노드들 확인
        for i in graph[now] :
            cost = dist + i[1]
            # 현재 노드 거쳐 이동하는게 더 짧으면 값 바꿔줌
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print('INFINITY')
    else :
        print(distance[i])

# O(ElogV)