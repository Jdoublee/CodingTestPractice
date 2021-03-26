n = int(input())

li = list(map(int, input().split()))

dp = [1] * n # 자기 자신만 카운트한 1로 초기화

# 맨 앞 인덱스부터 자기 자신 이전 값들과 비교하여 크면 해당 인덱스dp+1 과 자기 자신 중 큰 값으로 dp 교체
# 자기 자신 이전 값들과 계속 비교해나가므로 해당 인덱스 dp보다 현재 자신dp값이 더 클 수 있으므로 max로 값 대체
for i in range(n):
	for j in range(i):
		if li[j] < li[i]:
			dp[i] = max(dp[i], dp[j]+1)

print(max(dp))