from itertools import permutations

n = int(input())

nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

opp = []

maxr = -1e10
minr = 1e10

for i, op in enumerate(ops):
	if op > 0:
		opp.extend([i for _ in range(op)])

opp = list(set(permutations(opp))) # 순열 중 중복되는거 제거

for op in opp:
	now = nums[0]
	for i in range(1,n):
		if op[i-1] == 0:
			now += nums[i]
		elif op[i-1] == 1:
			now -= nums[i]
		elif op[i-1] == 2:
			now *= nums[i]
		else:
			if now < 0:
				now = -(-now // nums[i])
			else:
				now //= nums[i]
	
	maxr = max(maxr, now)
	minr = min(minr, now)

print(maxr)
print(minr)
