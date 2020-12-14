INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())
# 2차원 리스트 선언 및 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 대각선 값(자기 자신으로 가는 값)은 0으로 초기화
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b :
            graph[a][b] = 0

# 각 간선에 대한 정보 입력 및 초기화
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 결과 출력
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if graph[a][b] == INF :
            print('INFINITY', end=' ')
        else :
            print(graph[a][b], end=' ')
    print()