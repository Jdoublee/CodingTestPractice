# 0이 포함된 인덱스의 값은 다 1 이므로 초기값 그냥 1로 처리. 밑에서 그 이후 값들 바꿔줌
dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

# 1부터 값 바꿔줌
for i in range(1,21):
	for j in range(1,21):
		for k in range(1,21):
			if i < j and j < k:
				dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
			else:
				dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]


while True:
	a, b, c = map(int, input().split())
	if a == -1 and b == -1 and c == -1:
		break
	
	if a <= 0 or b <= 0 or c <= 0:
		print('w({}, {}, {}) ='.format(a,b,c),dp[0][0][0])
	elif a > 20 or b > 20 or c > 20:
		print('w({}, {}, {}) ='.format(a,b,c),dp[20][20][20])
	else:
		print('w({}, {}, {}) ='.format(a,b,c),dp[a][b][c])
