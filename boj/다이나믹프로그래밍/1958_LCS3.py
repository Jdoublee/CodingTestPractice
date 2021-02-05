a = input()
b = input()
c = input()

dp = [[[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)] for _ in range(len(c)+1)] # 귀찮더라도 이렇게 선언하자

for i in range(1, len(c)+1):
	for j in range(1, len(b)+1):
		for k in range(1, len(a)+1):
			if a[k-1] == b[j-1] == c[i-1]:
				dp[i][j][k] = dp[i-1][j-1][k-1] + 1
			else:
				dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
			
print(dp[-1][-1][-1])

# 기존 두 개짜리 LCS를 두 번 이용하면 안 되나? 했는데 안 돼~
# 3차원 배열 선언해서 이후 과정은 동일하게