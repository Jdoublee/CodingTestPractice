n = int(input())

dp = [[0,0] for _ in range(91)]

dp[1][0] = 0 # 0으로 끝나는 n자리 수 개수. 0으로 끝나는 수 뒤에는 0, 1 둘 다 추가 가능
dp[1][1] = 1 # 1로 끝나는 n자리 수 개수. 1로 끝나는 수 뒤에는 0만 추가 가능

for i in range(2, n+1):
	dp[i][0] = dp[i-1][0] + dp[i-1][1]
	dp[i][1] = dp[i-1][0]

print(sum(dp[n]))