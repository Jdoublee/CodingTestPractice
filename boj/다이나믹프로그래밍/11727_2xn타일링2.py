n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    # 2개 붙이는 방법 2가지로 증가. *2 해줌.
	dp[i] = (dp[i-2]*2 + dp[i-1]) % 10007

print(dp[n])