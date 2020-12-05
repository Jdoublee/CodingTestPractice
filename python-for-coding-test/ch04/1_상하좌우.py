n = int(input())
li = list(input().split())

# 거지같이 구현만 해보았다.
now = [1,1]
for ch in li :
	bef_0 = now[0]
	bef_1 = now[1]
	if ch == 'L' :
		now[1] -= 1
	elif ch == 'R' :
		now[1] += 1
	elif ch == 'U' :
		now[0] -= 1
	else :
		now[0] += 1
	
	if now[0] < 1 or now[0] > n :
		now[0] = bef_0
	elif now[1] <1 or now[1] > n :
		now[1] = bef_1

print(now[0], now[1])
		
# 깔끔하게
n = int(input())
li = input().split()

x, y = 1, 1
# L, R, U, D 순서대로 이동 방향 리스트에 저장
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moving = ['L', 'R', 'U', 'D']

for m in li :
	for i in range(len(moving)) :
		if m == moving[i] :
			nx = x + dx[i]
			ny = y + dy[i]
	if nx < 1 or ny < 1 or nx >n or ny > n :
		continue
	
	x, y = nx, ny

print(x, y)