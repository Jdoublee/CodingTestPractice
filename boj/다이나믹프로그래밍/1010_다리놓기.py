import sys
input = sys.stdin.readline

t = int(input())

dp = [[0 for _ in range(31)] for _ in range(31)]

# n이 1인 경우는 다리 놓을 수 있는 경우의 수 m과 같다
for i in range(1,31):
	dp[1][i] = i

for i in range(2,31):
	for j in range(i,31): # n <= m 이므로 i부터 채우면 된다
		for k in range(j-1,0,-1):
			dp[i][j] += dp[i-1][k]
            # n개 중 첫번째 사이트가 m개중 첫번째, 두번째, ... j-1번째와 연결되었다면, n-1개와 m-1, m-2, ... 개를 연결하는 경우의 수 다 더해주면 된다
            # 그림 그려서 첫번째 사이트를 첫번째, 두번째, ... 각 연결하고 남은 거 수만큼 더해주면 되는데
            # 말로 설명하기 힘들다
            # 그림을 그려보자


for _ in range(t):
	n, m = map(int, input().split())
	print(dp[n][m])
