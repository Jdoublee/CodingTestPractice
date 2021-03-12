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
			print(q.count(k)+1) # 큐 내에 동생 위치 개수 + 1 (pop한거)
			return
		
		for i in [x-1, x+1, 2*x]:
			if 0 <= i <= 100000:
                # 방문하지 않았거나, x까지의 시간+1 보다 크거나 같은 경우 시간 업데이트 및 큐에 추가.
				if check[i] == -1 or check[i] >= check[x]+1: # x까지의 시간+1 보다 같은 경우도 큐에 추가해줘야 하므로 포함(방법 수 셀 때 필요)
					check[i] = check[x] + 1
					q.append(i)
				
		

n, k = map(int, input().split())
check = [-1] * 100001 # 시간 저장
bfs()
