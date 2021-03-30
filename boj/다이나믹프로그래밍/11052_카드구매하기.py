n = int(input())

cards = list(map(int, input().split()))

dp = [card for card in cards]

for i in range(n):
	for j in range(i): # i번째 카드보다 작은 카드들 모두 순회
		dp[i] = max(dp[i], dp[i-j-1]+cards[j]) # dp[i] 와 dp[i-(j+1)]+cards[j] 중 큰 값 선택

print(dp[-1])