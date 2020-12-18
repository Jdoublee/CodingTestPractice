n, k = map(int, input().split())

coins = []
for _ in range(n):
	coins.append(int(input()))
	
res = 0
coins.sort(reverse=True)
for i in range(n):
	if k >= coins[i]:
		res += k//coins[i]
		k %= coins[i]
	if k == 0:
		break

print(res)