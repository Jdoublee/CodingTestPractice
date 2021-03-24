n = int(input())

dp = [0] * 1000001
# dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4,n+1):
    # 1은 나누거나 뺴는 연산
    # 이전 값, 2나 3으로 나눈 값에 해당하는 인덱스에 해당하는 dp 값이 가장 작은 값 더해줌
	if i%6 == 0:
		dp[i] = 1 + min(dp[i//3], dp[i//2], dp[i-1])
	elif i%3 == 0:
		dp[i] = 1 + min(dp[i//3], dp[i-1])
	elif i%2 == 0:
		dp[i] = 1 + min(dp[i//2], dp[i-1])
	else:
		dp[i] = 1 + dp[i-1]

print(dp[n])