import sys
input = sys.stdin.readline

n = int(input())

rgb = []

for _ in range(n):
	rgb.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(3)] # 각 배열의 i번째 인덱스를 r, g, b 로 칠했을 때의 최소 비용

dp[0][0] = rgb[0][0]
dp[1][0] = rgb[0][1]
dp[2][0] = rgb[0][2]

for i in range(1,n):
	dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + rgb[i][0] # 바로 앞 집이 g 또는 b로 칠했고(둘 중 최소), 지금 집 r로 칠함
	dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + rgb[i][1] # 바로 앞 집이 r 또는 b로 칠했고, 지금 집 g로 칠함
	dp[2][i] = min(dp[0][i-1], dp[1][i-1]) + rgb[i][2] # 바로 앞 집이 r 또는 g로 칠했고, 지금 집 b로 칠함
	
print(min(dp[0][-1], dp[1][-1], dp[2][-1]))