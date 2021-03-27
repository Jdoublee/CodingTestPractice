n = int(input())

li = list(map(int, input().split()))

dp = [x for x in li]

for i in range(n):
	for j in range(i):
		if li[j] < li[i]:
			dp[i] = max(dp[i], dp[j]+li[i]) # 현재 인덱스 dp와 앞의 인덱스 dp + 자기 자신 중 큰 값 저장

print(max(dp))
