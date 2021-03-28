t = int(input())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

# dp[n]은 
# dp[n-1] + 1
# dp[n-2] + 2
# dp[n-3] + 3
for i in range(4,11):
	dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
	n = int(input())
	
	print(dp[n])