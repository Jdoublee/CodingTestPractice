import sys
input = sys.stdin.readline

n = int(input())
wine = []

for _ in range(n):
	wine.append(int(input()))

if n < 3:
	print(sum(wine))
	quit()

dp = [0] * n

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0]+wine[2], wine[1]+wine[2])

if n == 3:
	print(max(dp))
	quit()

dp[3] = max(dp[0]+wine[2]+wine[3], dp[1]+wine[3])

for i in range(4,n):
	dp[i] = max(dp[i-4]+wine[i-1]+wine[i], dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i])
    # oxxo'o'(계단 오르기에서 하나 더 추가됨. 두개 뛰어넘는 경우) 또는 oxo'o' 또는 _ox'o'
    # 1000 1000 1 1 1000 1000 인 경우 ooxxoo가 최대
	
print(max(dp))