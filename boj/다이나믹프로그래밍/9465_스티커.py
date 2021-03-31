import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	stickers = []
	for _ in range(2):
		stickers.append(list(map(int, input().split())))
	
	dp = [[0 for _ in range(n)] for _ in range(2)]
	
	dp[0][0] = stickers[0][0]
	dp[1][0] = stickers[1][0]
	
	if n == 1:
		print(max(dp[0][0], dp[1][0]))
		continue
	
	dp[0][1] = dp[1][0] + stickers[0][1]
	dp[1][1] = dp[0][0] + stickers[1][1]
	
	for i in range(2,n):
		dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i] # i번째 열의 0행 스티커 선택할 경우
		dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i] # i번째 열의 1행 스티커 선택할 경우
        # 해당 스티커 + i-1열의 대각선 스티커와 i-2열의 대각선 위치 스티커 중 최댓값
		
	print(max(dp[0][-1], dp[1][-1]))