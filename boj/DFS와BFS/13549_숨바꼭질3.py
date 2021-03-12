from collections import deque

def bfs():
	q = deque()
	q.append(n)
	check[n] = 0 # 시작위치 시간 0으로 초기화

	while q:
		x = q.popleft()
		
        # 동생 위치 도달하면 출력 후 종료
		if x == k:
			print(check[k])
			return
		
		for i in [x-1, x+1, 2*x]:
			if 0 <= i <= 100000:
                # 방문하지 않았거나, x까지의 시간+1 보다 큰경우 시간 업데이트 및 큐에 추가.
				if check[i] == -1 or check[i] > check[x]+1:
					if i == 2*x:
						check[i] = check[x]
					else:
						check[i] = check[x] + 1
					q.append(i)
				
		

n, k = map(int, input().split())
check = [-1] * 100001 # 시간 저장
bfs()
