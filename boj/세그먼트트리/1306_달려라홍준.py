import sys
input = sys.stdin.readline

def init(node, start, end):
	if start == end:
		tree[node] = lights[start]
		return tree[node]
	
	mid = (start+end)//2
	tree[node] = max(init(node*2, start, mid), init(node*2+1, mid+1, end))
	return tree[node]

def find_max(node, start, end, left, right):
	if start > right or end < left:
		return 0
	
	if left <= start and end <= right:
		return tree[node]
	
	mid = (start+end)//2
	return max(find_max(node*2, start, mid, left, right), find_max(node*2+1, mid+1, end, left, right))


n, m = map(int, input().split())
lights = list(map(int, input().split()))

tree = [0] * 4 * n
init(1,0,n-1)

for i in range(m-1,n-m+1):
	print(find_max(1,0,n-1,i-m+1,i+m-1), end=' ')

# pypy만 통과. 파이썬은 시간초과.