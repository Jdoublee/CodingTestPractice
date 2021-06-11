import sys
input = sys.stdin.readline

r,c,t = map(int, input().split())
graph = []

dx = [-1,0,0,1]
dy = [0,-1,1,0]

for _ in range(r):
	graph.append(list(map(int, input().split())))

# 공기청정기 위치(행) 파악
for i in range(r):
	if graph[i][0] == -1:
		loc1 = i
		loc2 = i+1
		break

# 시간 t초 동안 반복
for _ in range(t):
    # 미세먼지 확산
	changed = [[0 for _ in range(c)] for _ in range(r)] # 확산 후 먼지 저장

	for i in range(r):
		for j in range(c):
			if graph[i][j] <= 0: # 공기청정기 또는 먼지 0이면 통과 
				continue
			
			tot = 0 # 확산된 공기 양
			
			for k in range(4):
				if 0 <= i+dx[k] < r and 0 <= j+dy[k] < c and graph[i+dx[k]][j+dy[k]] > -1:
					changed[i+dx[k]][j+dy[k]] += graph[i][j]//5
					tot += graph[i][j]//5
			
			changed[i][j] += (graph[i][j] - tot)
	
	graph = changed # 그래프 변경
	graph[loc1][0] = -1
	graph[loc2][0] = -1
	
    # 위쪽 공기청정기 작동
	tmp = graph[loc1][-1]
	graph[loc1] = [-1,0] + graph[loc1][1:-1]
	
	for i in range(loc1-1,0,-1):
		tmp2 = graph[i][-1]
		graph[i][-1] = tmp
		tmp = tmp2
	
	tmp2 = graph[0][0]
	graph[0] = graph[0][1:] + [tmp]
	
	for i in range(1,loc1):
		tmp = graph[i][0]
		graph[i][0] = tmp2
		tmp2 = tmp
	
	# 아래쪽 공기청정기 작동
	tmp = graph[loc2][-1]
	graph[loc2] = [-1,0] + graph[loc2][1:-1]
	
	for i in range(loc2+1,r-1):
		tmp2 = graph[i][-1]
		graph[i][-1] = tmp
		tmp = tmp2
	
	tmp2 = graph[r-1][0]
	graph[r-1] = graph[r-1][1:] + [tmp]
	
	for i in range(r-2,loc2,-1):
		tmp = graph[i][0]
		graph[i][0] = tmp2
		tmp2 = tmp

res = 2
for g in graph:
	res += sum(g)	
			
print(res)

# pypy3 통과 코드(파이썬 시간초과)