board = []
nums = []
res = []

def check():
	cnt = 0
	bingos = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14],
	[15, 16, 17, 18, 19], [20, 21, 22, 23, 24], [0, 5, 10, 15, 20], [1, 6, 11, 16, 21],
	[2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [0, 6, 12, 18, 24],
	[4, 8, 12, 16, 20]]
	
	for bingo in bingos:
		flag = True
		for b in bingo:
			if b not in res:
				flag = False
				break
		if flag:
			cnt += 1
	
	return cnt


for _ in range(5):
	board.extend(list(map(int, input().split())))

for _ in range(5):
	nums.extend(list(map(int, input().split())))

for i in range(25):
	now = board.index(nums[i])
	res.append(now)
	if check() >= 3: # 2줄 -> 4줄 되는 경우 있으므로 같거나 큰 경우로 조건 확인
		print(i+1)
		break