# 행이 3개인 2차원 인접 리스트 선언
graph = [[] for _ in range(3)]

# 0번 노드에 연결된 노드 번호와 거리(weight) append
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)