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

n = int(input())

parent = [i for i in range(n)]
p = []
res = 0

for i in range(n):
	x, y, z = map(int, input().split())
	p.append((x,y,z,i)) # 좌표 + i 번째 인덱스
	
q = []
# 아래 코드 작성 시 메모리 초과 발생
# for i in range(n):
# 	for j in range(i+1,n):
# 		heapq.heappush(q, (min(abs(p[i][0]-p[j][0]), abs(p[i][1]-p[j][1]), abs(p[i][2]-p[j][2])), i, j))
# x, y, z 기준으로 각각 정렬하여 앞뒤의 행성 간 거리 heapq에 넣어줌으로 대체
p.sort()
for i in range(n-1):
	heapq.heappush(q, (min(abs(p[i][0]-p[i+1][0]), abs(p[i][1]-p[i+1][1]), abs(p[i][2]-p[i+1][2])), p[i][3], p[i+1][3]))

p.sort(key=lambda x:x[1])
for i in range(n-1):
	heapq.heappush(q, (min(abs(p[i][0]-p[i+1][0]), abs(p[i][1]-p[i+1][1]), abs(p[i][2]-p[i+1][2])), p[i][3], p[i+1][3]))

p.sort(key=lambda x:x[2])
for i in range(n-1):
	heapq.heappush(q, (min(abs(p[i][0]-p[i+1][0]), abs(p[i][1]-p[i+1][1]), abs(p[i][2]-p[i+1][2])), p[i][3], p[i+1][3]))

while q:
	c, a, b = heapq.heappop(q)
	if find(a) != find(b):
		union(a,b)
		res += c
print(res)