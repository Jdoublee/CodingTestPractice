from collections import deque

n, k = map(int, input().split())

visited = [False] * 100001

def bfs(s, e):
	queue = deque()
	
	queue.append((s, 0)) # 큐에 들어갈 떄의 cnt 같이 튜플 형태로 넣어줌. 전체 큐 푸시팝 수 아닌 해당 위치 통한 이동 시간 세기 위해서.
	
	while queue:
		i, cnt = queue.popleft() # cnt도 같이 pop해서 +1 후 다음 이동 위치에 추가

		if not visited[i]:
			visited[i] = True
			
			if i == e:
				return cnt
		
			cnt += 1
		
			if i-1 >= 0 :
				queue.append((i-1, cnt))
			if i+1 <= 100000:
				queue.append((i+1, cnt))
			if i*2 <= 100000:
				queue.append((i*2, cnt))
		
	return cnt

print(bfs(n, k))