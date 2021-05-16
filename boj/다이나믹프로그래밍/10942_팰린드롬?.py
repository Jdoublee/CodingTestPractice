import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)] # dp[i][j] : i ~ j 까지 팰린드롬:1 아니면 0

# 문자열
# 1개
for i in range(n):
	dp[i][i] = 1

# 2개
for i in range(n-1):
	if nums[i] == nums[i+1]:
		dp[i][i+1] = 1

# 3개 이상
for i in range(2,n):
	for j in range(n-i):
		if nums[j] == nums[j+i] and dp[j+1][j+i-1]: # 양 끝값이 같고, 그 사이의 값이 팰린드롬 만족하면
			dp[j][j+i] = 1 # 새로운 구간도 팰린드롬

m = int(input())

for _ in range(m):
	s, e = map(int, input().split())
	
	print(dp[s-1][e-1])


# nums == nums[::-1] 은 시간초과