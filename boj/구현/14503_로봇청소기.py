n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = []

for _ in range(n):
	graph.append(list(map(int, input().split())))

res = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph[r][c] = -1
res += 1
	
while True:
	check = False
	
	for i in range(4):
		nx = r + dx[(d+3-i)%4]
		ny = c + dy[(d+3-i)%4]
		
		if graph[nx][ny] == 0:
			check = True
			graph[nx][ny] = -1
			res += 1
			d = (d+3-i)%4
			r = nx
			c = ny
			break
		
	if check:
		continue
	
	nx = r + dx[(d+2)%4]
	ny = c + dy[(d+2)%4]
	
	if graph[nx][ny] == 1:
		break
	else:
		r = nx
		c = ny
		
print(res)
