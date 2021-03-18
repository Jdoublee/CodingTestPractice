import sys
import heapq
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

n, m = map(int, input().split())

parent = [i for i in range(n)]
stars = []
res = 0

for _ in range(n):
	a, b = map(int, input().split())
	stars.append((a,b))

for _ in range(m):
	a, b = map(int, input().split())
	union(a-1,b-1)
	
q = []
for i in range(n):
	for j in range(i+1,n):
		heapq.heappush(q, (((stars[j][1]-stars[i][1])**2+(stars[j][0]-stars[i][0])**2)**0.5, i, j))

while q:
	c, a, b = heapq.heappop(q)
	if find(a) != find(b):
		union(a,b)
		res += c

print('%.2f' %res) # 소수점 둘째 자리까지 출력. round쓰면 4.00 -> 4.0으로 출력(틀림)