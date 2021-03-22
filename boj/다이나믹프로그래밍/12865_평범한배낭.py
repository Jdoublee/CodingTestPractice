n, k = map(int, input().split())

wv = []
dp = [[0 for _ in range(k+1)] for _ in range(n+1)] # n+1 * k+1 크기의 dp 배열 선언

for _ in range(n):
	w, v = map(int, input().split())
	wv.append((w,v))

# 입력으로 들어온 물건 하나 하나 처리
for i in range(n):
	for j in range(k+1):
        # 해당 물건 무게가 j보다 작으면 해당 물건 들어오기 전 가치와 현재 무게(j)에서 해당 물건 무게 뺸 가치 + 현재 물건 가치 중 큰 값을 현재 dp 위치에 저장
		if wv[i][0] <= j:
			dp[i+1][j] = max(dp[i][j], dp[i][j-wv[i][0]]+wv[i][1])
        # 해당 물건 무게가 j보다 크면 해당 물건 들어오기 전 가치 그대로 저장
		else:
			dp[i+1][j] = dp[i][j]
		
# for d in dp:
# 	print(d)
print(dp[n][k])
# 다 시 보 기