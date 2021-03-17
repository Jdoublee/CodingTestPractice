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
stars = []
res = 0

for _ in range(n):
	a, b = map(float, input().split())
	stars.append((a,b))

# 각 별과 나머지 별에 대한 거리 정보 모두 싸그리 구해서 heapq에 저장
# 입력 데이터 적어서 가능
q = []
for i in range(n):
	for j in range(i+1,n):
		heapq.heappush(q, (((stars[j][1]-stars[i][1])**2+(stars[j][0]-stars[i][0])**2)**0.5, i, j)) # sqrt랑 **0.5의 값이 다른 이유는,,,?

while q:
	c, a, b = heapq.heappop(q)
	if find(a) != find(b):
		union(a,b)
		res += c

print(round(res, 2)) # 절대/상대 오차는 10-2까지 허용한다. -> 소수점 아래 둘째자리까지 출력. 반올림 함수 round 사용