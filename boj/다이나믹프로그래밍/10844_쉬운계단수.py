n = int(input())

# 계단수의 끝자리 수 개수 저장
dp = [0 for _ in range(10)]

# 1자리 수의 계단수는 1~9 1개씩
for i in range(1,10):
	dp[i] = 1

for i in range(2,n+1):
	tmp = [0 for _ in range(10)]
	for j in range(10):
        # 0이나 9로 끝나는 경우엔 계단수 하나밖에 못 만듦. 10 -> 101
		if j == 0:
			tmp[1] += dp[j]
		elif j == 9:
			tmp[8] += dp[j]
        # 나머지 경우엔 두가지 만듦. 65 -> 654, 656
		else:
			tmp[j-1] += dp[j]
			tmp[j+1] += dp[j]
	dp = tmp

print(sum(dp)%1000000000)