import sys
input = sys.stdin.readline

def init(node, start, end):
	if start == end:
		tree[node] = nums[start]
		return tree[node]
		
	mid = (start+end)//2
	tree[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
	return tree[node]

def find_min(node, start, end, left, right):
	if left > end or right < start:
		return float('inf')
	
	if left <= start and end <= right:
		return tree[node]
	
	mid = (start+end)//2
	return min(find_min(node*2, start, mid, left, right), find_min(node*2+1, mid+1, end, left, right))

n, m = map(int, input().split())
nums = []

tree = [0] * 4 * n

for _ in range(n):
	nums.append(int(input()))

init(1,0,n-1)

for _ in range(m):
	a, b = map(int, input().split())
	print(find_min(1,0,n-1,a-1,b-1))