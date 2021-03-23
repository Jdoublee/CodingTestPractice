n = int(input())

arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
	if dp[i-1] > 0: # 이전 값까지의 합이 양수면 거기에 현재 값 더해줌
		dp[i] = dp[i-1] + arr[i]
	else: # 이전 값까지의 합이 음수면 현재 값 자체가 최대
		dp[i] = arr[i]

print(max(dp))