# 이분 그래프 정의
# https://ko.wikipedia.org/wiki/이분_그래프
import sys
from collections import deque

input = sys.stdin.readline

def bfs():
	queue = deque()
    # 비연결 그래프일 경우 생각해야 함.
    # 예시
    # A - B
    # C - D
    # E - F
	tocheck = v # 연결되어있는 정점 수(확인해야 될 정점)
	flag = False
	
	for i in range(1, v+1):
		if not graph[i]: # 연결된 정점 없으면 -1 처리, 체크-- (확인할 필요 없음)
			visited[i] = -1
			tocheck -= 1
		elif not flag: # 연결된 정점 있는 정점 중 첫번째 정점을 시작 정점으로.
			flag = True
			queue.append(i)
			visited[i] = 1
			tocheck -= 1
			
	while tocheck > 0: # 아직 확인해야 할 정점 남아있으면
		while queue: # 큐 확인
			now = queue.popleft()
		
			for i in graph[now]:
				if visited[i] == 0:
					if visited[now] == 1:
						visited[i] = 2
					else:
						visited[i] = 1
					queue.append(i)
					tocheck -= 1
					
				elif visited[i] == visited[now]: # 이미 방문했는데 연결된 정점과 색(숫자) 같으면 이분 그래프 아님 리턴
					return 'NO'
		
		if tocheck > 0: # 큐 다 꺼냈는데 아직 확인해야 할 정점 남아있으면
			for i in range(1, v+1):
				if visited[i] == 0: # 방문 안 한 정점 큐에 추가 
					queue.append(i)
					visited[i] = 1
					tocheck -= 1
					break
				
	return 'YES'
	

k = int(input())

for _ in range(k):
	v, e = map(int, input().split())
	
    # 1부터 시작하므로 0번은 비워둠. 공간 하나 추가로 부여.
	graph = [[] for _ in range(v+1)]
	
	visited = [0] * (v+1)
	
	for _ in range(e):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)
		
	print(bfs())