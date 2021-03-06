import sys
input = sys.stdin.readline # 3884ms -> 160ms로.

n = int(input())

weights = []
for _ in range(n):
	weights.append(int(input()))
	
weights.sort(reverse=True)
res = 0

for i in range(len(weights)):
	res = max(res, weights[i]*(i+1))

print(res)