import sys
input = sys.stdin.readline

def init(node, start, end):
	if start == end:
		tree[node] = nums[start]
		return tree[node]
	
	mid = (start+end)//2
	tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
	return tree[node]

def sum(node, start, end, left, right):
	if left > end or right < start:
		return 0
	
	if left <= start and end <= right:
		return tree[node]
	
	mid = (start+end)//2
	return sum(node*2, start, mid, left, right) + sum(node*2+1, mid+1, end, left, right)

def update(node, start, end, index, dif):
	if index < start or index > end:
		return
	
	tree[node] += dif
	
	mid = (start+end)//2
	if start != end:
		update(node*2, start, mid, index, dif)
		update(node*2+1, mid+1, end, index, dif)

n, m, k = map(int, input().split())

nums = []
tree = [0] * (4 * n)

for _ in range(n):
	nums.append(int(input()))

init(1, 0, n-1)
	
for _ in range(m+k):
	a, b, c = map(int, input().split())
	if a == 1:
		dif = c-nums[b-1]
		nums[b-1] = c
		update(1,0,n-1,b-1,dif)
	else:
		print(sum(1,0,n-1,b-1,c-1))