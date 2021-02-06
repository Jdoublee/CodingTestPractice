n = int(input())
cnt = 0

nums = []

graph = []

for _ in range(n):
	graph.append(list(input().rstrip()))

def dfs(i, j, num):
	graph[i][j] = '-1' # 방문 처리
	num += 1 # 단지내 집 수 
	dx = [-1, 0, 0, 1]
	dy = [0, -1, 1, 0]
	
	for k in range(4):
		x = i + dx[k]
		y = j + dy[k]
		
		if 0 <= x < n and 0 <= y < n:
			if graph[x][y] == '1':
				num = dfs(x, y, num)
	 
	return num # 단지내 집 수 반환해줌
		
for i in range(n):
	for j in range(n):
		if graph[i][j] == '1':
			num = 0
			num = dfs(i, j, num)
			cnt += 1
			nums.append(num)

print(cnt)	
nums.sort()
for num in nums:
	print(num)