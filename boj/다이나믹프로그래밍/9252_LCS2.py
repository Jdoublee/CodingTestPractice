a = input().rstrip()
b = input().rstrip()

la = len(a) + 1
lb = len(b) + 1

dp = [[0] * lb for _ in range(la)]

for i in range(1, la):
	for j in range(1, lb):
		if a[i-1] == b[j-1]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

# 뒤에서부터 비교
# 현재 값이 왼쪽 값 & 위쪽 값과 다른 경우 해당 부분수열에 포함
if dp[-1][-1] > 0:
	res = []
	i = la - 1
	j = lb - 1
	while i > 0 and j > 0:
		if dp[i][j] == dp[i][j-1]:
			j -= 1
		elif dp[i][j] == dp[i-1][j]:
			i -= 1
		else:
			res.append(a[i-1])
			i -= 1
			j -= 1
	res.reverse()
	print(''.join(res))