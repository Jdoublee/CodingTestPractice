import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

graph = []

for _ in range(n):
	graph.append(list(map(int, input().split())))

moves = list(map(int, input().split()))

# 1 2 3 4 이동 방향 저장 (0 더미)
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

# 1 2 3 4 각 방향으로 굴렸을 때 (0 더미) 위치 이동 정보 리스트에 저장 
# 0 1 2 3 4 5 (인덱스)
# 밑 앞 위 뒤 오 왼
dm = [[],[4,1,5,3,2,0],[5,1,4,3,0,2],[3,0,1,2,4,5],[1,2,3,0,4,5]]

dice = [0,0,0,0,0,0] # 아래 앞 위 뒤 오 왼

for move in moves:
	nx = x + dx[move]
	ny = y + dy[move]
	
	if nx < 0 or nx >= n or ny < 0 or ny >= m: # 지도 범위 밖 무시
		continue

    # 주사위 정보 업데이트
	tmp = []
	for i in dm[move]:
		tmp.append(dice[i])
	
	dice = tmp
	
    # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면,
	if graph[nx][ny] == 0:
        # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
		graph[nx][ny] = dice[0]

    # 이동한 칸에 쓰여 있는 수가 0이 아닌 경우에는
	else:
        # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며,
		dice[0] = graph[nx][ny]
        # 칸에 쓰여 있는 수는 0이 된다.
		graph[nx][ny] = 0 # 이거 빼먹었다... 잘 읽자
	
	print(dice[2])
	x,y = nx,ny # 현재 좌표 변경
		
# 주사위 그림 그려서 이해하는 과정 필요