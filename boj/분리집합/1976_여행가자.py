import sys
input = sys.stdin.readline
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
	

n = int(input())
m = int(input())

parent = [i for i in range(n)] # 0부터 채워줌

for i in range(n):
	li = list(map(int, input().split()))
	
	for j in range(len(li)):
		if li[j] == 1:
			union(i,j)
			
plan = list(map(int, input().split()))

res = True
for i in range(m-1):
	if find(plan[i]-1) == find(plan[i+1]-1): # 0부터 parent 저장해줬으므로 입력받은 값-1 해서 처리
		continue
	else:
		res = False
		break

if res:
	print('YES')
else:
	print('NO')
	