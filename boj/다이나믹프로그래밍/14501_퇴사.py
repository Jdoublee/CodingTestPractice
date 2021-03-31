import sys
input = sys.stdin.readline

n = int(input())

info = []

for _ in range(n):
	info.append(list(map(int, input().split())))

dp = [] # 인덱스 날짜에 받을 수 있는 최대 수익
# dp 초기값 저장. 해당 날짜에 일할 수 있으면(n+1일 이전) 해당 인덱스에 수익 저장
for i in range(n):
	if info[i][0] + i <= n:
		dp.append(info[i][1])
	else:
		dp.append(0)


for i in range(n):
	for j in range(i):
		if info[j][0] + j <= i and dp[i] > 0: # j번째 날에 일하고 끝나는 날짜가 i번째 날 이전이고 i번째 날에 일 할 수 있으면
			dp[i] = max(dp[i], dp[j]+info[i][1]) # 원래 i번째 날까지의 수익과 j번째 날까지의 수익+i번째 날의 상담 비용 중 최대값 저장

print(max(dp))