import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	coins = list(map(int, input().split()))
	m = int(input())
	
	dp = [0] * (m+1)
	
	dp[0] = 1 # 해당 동전 1개일때 더해지므로
		
	for coin in coins:
		for i in range(coin,m+1):
			dp[i] += dp[i-coin]
	
	print(dp[-1])