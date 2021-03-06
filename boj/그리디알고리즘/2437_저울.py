import sys
input = sys.stdin.readline

n = int(input().rstrip())
weights = list(map(int, input().rstrip().split()))

weights.sort()

# 1부터 시작 or 1 나중에 더해주기
comp = 1 # comp = weights[0] # if comp > 1: print(1) 
res = 0

for i in range(n):
	print(comp)
	if comp < weights[i]: # == if weights[i] > comp + 1:
		res = comp
		break
	comp += weights[i]

if res == 0:
	res = comp

print(comp)
