import sys
sys.setrecursionlimit(10**6)

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

G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
res = 0

for _ in range(P):
	g = int(input())
	
	if find(g) == 0: # 부모가 0 이면 더이상 도킹할 게이트 없단 뜻이므로 종료
		break
	
	union(parent[g], parent[g]-1) # 현재 게이트의 부모 게이트를 직전 게이트와 연결 -> 동일한 숫자 게이트 입력으로 들어올 시 직전 게이트 비었나 확인
	res += 1

print(res)