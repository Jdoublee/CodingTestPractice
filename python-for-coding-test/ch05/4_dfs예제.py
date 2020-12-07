def dfs(graph, v, visited) :
    # 현재 노드 방문 처리
    visited[v] = True

    print(v, end=' ')

    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

# 인접 리스트
graph = [
    [],
    [2, 3, 8], # 1
    [1, 7], # 2
    [1, 4, 5], # 3
    [3, 5], # 4
    [3, 4], # 5
    [7], # 6
    [2, 6, 8], # 7
    [1, 7] # 8
]

# 각 노드 방문 정보
visited = [False] * 9

dfs(graph, 1, visited)