from collections import deque
import copy

def bfs():
	q = deque()
	q.append(n)
	check[n] = 0 # 시작위치 시간 0으로 초기화

	while q:
		x = q.popleft()
		
        # 동생 위치 도달하면 출력 후 종료
		if x == k:
			print(check[k])

			res = [] # 동생 위치까지 방문한 위치 저장
			while x != n:
				res.append(x)
				x = way[x][0]
			res.append(n)
			for r in res[::-1]: # 역으로 출력
				print(r, end=' ')
			return
		
		for i in [x-1, x+1, 2*x]:
			if 0 <= i <= 100000:
                # 방문하지 않았거나, x까지의 시간+1 보다 크거나 같은 경우 시간 업데이트 및 큐에 추가.
				if check[i] == -1 or check[i] > check[x] + 1:
					check[i] = check[x] + 1
					way[i] = [x]
					q.append(i)
				

n, k = map(int, input().split())
check = [-1] * 100001 # 시간 저장
way = [[] for _ in range(100001)] # 직전에 방문한 위치 저장
bfs()
