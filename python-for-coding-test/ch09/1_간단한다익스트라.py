import sys
input = sys.stdin.readline
INF = int(1e9)
# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결된 노드 정보
graph = [[] for i in range(n+1)]
# 방문 여부 체크
visited = [False] * (n+1)
# 최단 거리 테이블 무한대 값으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력받음
for _ in range(m) :
    # a번 노드에서 b번 노드로 가는 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중 최단 거리 가장 짧은 노드 번호 반환
def get_smallest_node() :
    min_value = INF
    idx = 0
    for i in range(1, n+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            idx = i
    return idx

def dijkstra(start) :
    distance[start] = 0
    visited[start] = True
    for j in graph[start] :
        distance[j[0]] = j[1]
    # 전체 노드 반복
    for i in range(n-1) :
        # 현재 최단 거리 가장 짧은 노드 찾아서 방문
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 노드들 확인
        for j in graph[now] :
            cost = distance[now] + j[1]
            # 현재 노드 거쳐 이동하는게 더 짧으면 값 바꿔줌
            if cost < distance[j[0]] :
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print('INFINITY')
    else :
        print(distance[i])
