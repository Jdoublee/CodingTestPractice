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

v, e = map(int, input().split())
res = 0

parent = [i for i in range(v+1)]
edges = []

for _ in range(e):
	a, b, c = map(int, input().split())
	edges.append((a,b,c))

edges.sort(key=lambda x:x[2]) # cost 순으로 정렬

for a, b, c in edges:
	if find(a) != find(b):
		union(a, b)
		res += c

print(res) # 변수명 오타 주의