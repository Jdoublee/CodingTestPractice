# 개복치 이썬이를 위해 아래 세 줄 잊지말기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
	if parent[x] != x:
		parent[x] = find(parent[x])
	return parent[x]

def union(a, b):
	a = find(a)
	b = find(b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

t = int(input())

for _ in range(t):
	n, m = map(int, input().split())
	res = 0
	
	parent = [i for i in range(n+1)]
	
	for _ in range(m):
		a, b = map(int, input().split())
		if find(a) != find(b):
			union(a, b)
			res += 1
			
	print(res)