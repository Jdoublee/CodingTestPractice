from collections import deque

def solution(n, costs):
    answer = 0
    
    graph = [[] for _ in range(n)]
    
    costs.sort(key=lambda x:x[2]) # 비용 저렴한 순으로 정렬
    
    for a, b, c in costs:
        # bfs 수행 -> 비효율적,,, 크루스칼/프림 알고리즘 다싀
        q = deque([costs[0][0]])
        visited = [False] * n

        while q:
            now = q.popleft()

            for x in graph[now]:
                if not visited[x]:
                    visited[x] = True
                    q.append(x)

        if visited.count(False) == 0: # 다 방문했으면 종료
            return answer
        
        if not visited[a] or not visited[b]: # 두 섬 중 하나라도 방문 안 했으면 연결
            graph[a].append(b)
            graph[b].append(a)
            answer += c
    
    return answer # 마지막에 만족했을 수 있으니 리턴문 남겨두기. (연결할 수 없는 섬은 주어지지 않습니다.)