# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

n, m = map(int, input().split())

ice_map = []
for _ in range(n) :
	ice_map.append(list(map(int, input())))

def dfs(x, y) :
	if x < 0 or x >= n or y < 0 or y >= m :
		return
	if ice_map[x][y] == 0 :
		ice_map[x][y] = -1
		
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)
	

cnt = 0
for i in range(n) :
	for j in range(m) :
		if ice_map[i][j] == 0 :
			cnt += 1
			dfs(i, j)
	
print(cnt)
# print(ice_map)