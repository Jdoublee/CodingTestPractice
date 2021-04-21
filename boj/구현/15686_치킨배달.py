from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

shops = []
houses = []

for i in range(n):
	tmp = list(map(int, input().split()))
	
	for j in range(n):
		if tmp[j] == 1:
			houses.append((i,j))
		elif tmp[j] == 2:
			shops.append((i,j))

res = float('inf')

for comb in list(combinations(shops,m)): # 조합으로 m개 치킨집 선택
	tot = 0
	for a,b in houses:
		dist = float('inf')
		for x,y in comb:
			dist = min(dist, abs(x-a)+abs(y-b)) # bfs(시간초과) -> 그냥 거리 구하는 공식으로 한 줄로 구현
		tot += dist
	res = min(res,tot)

print(res)