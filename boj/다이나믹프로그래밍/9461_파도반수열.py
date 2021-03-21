dp = [0] * 101

# 1 ~ 5까지는 규칙 없음
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
# 규칙 있지만 9부터 달라져서 그냥 값 넣어줌
dp[6] = 3 # dp[3] + dp[5]
dp[7] = 4 # dp[2] + dp[6] 
dp[8] = 5 # dp[1] + dp[7]

for i in range(9,101):
	dp[i] = dp[i-5] + dp[i-1]

t = int(input())

for _ in range(t):
	n = int(input())
	print(dp[n])